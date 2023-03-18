from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.managers import UserManger


class User(AbstractBaseUser, PermissionsMixin):

    login = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('логин'),
        help_text=_('Логин пользователя')
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name=_('электронная почта'),
        help_text=_('Электронная почта пользователя')
    )

    phone_number = models.CharField(
        max_length=16,
        unique=True,
        verbose_name=_('номер телефона'),
        help_text=_('Телефонный номер пользователя')
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('статус активности'),
        help_text=_('Определяет активен ли пользователь')
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('статус персонала'),
        help_text=_('Определяет является ли пользователь персоналом')
    )

    is_superuser = models.BooleanField(
        default=False,
        verbose_name=_('статус администратора'),
        help_text=_('Определяет является ли пользователь администратором')
    )

    objects = UserManger()

    EMAIL_FIELD = 'email'

    USERNAME_FIELD = 'login'

    REQUIRED_FIELDS = ['phone_number', 'email']

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class Client(models.Model):

    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('id пользователя'),
        help_text=_('Id связанного пользователя клиента')
    )

    legal_name = models.CharField(
        max_length=100,
        verbose_name=_('имя'),
        help_text=_('Имя юридического лица клиента')
    )

    legal_address = models.CharField(
        max_length=100,
        verbose_name=_('юр. адрес'),
        help_text=_('Юридический адрес клиента')
    )

    postal_address = models.CharField(
        max_length=50,
        verbose_name=_('почтовый адрес'),
        help_text=_('Почтовый адрес клиента')
    )

    tin = models.CharField(
        unique=True,
        max_length=10,
        verbose_name=_('инн'),
        help_text=_('ИНН клиента')
    )

    def __str__(self):
        return self.legal_name

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')


class Manager(models.Model):

    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('id пользователя'),
        help_text=_('Id связанного пользователя менеджера')
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name=_('имя'),
        help_text=_('Имя менеджера')
    )

    second_name = models.CharField(
        max_length=50,
        verbose_name=_('фамилия'),
        help_text=_('Фамилия менеджера')
    )

    patronymic = models.CharField(
        max_length=50,
        verbose_name=_('отчество'),
        help_text=_('Отчество менеджера')
    )

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = _('Менеджер')
        verbose_name_plural = _('Менеджеры')


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created and not instance.is_staff and not instance.is_superuser:
        Client.objects.create(user_id=instance)


@receiver(post_save, sender=User)
def create_manager(sender, instance, created, **kwargs):
    if created and instance.is_staff and not instance.is_superuser:
        Manager.objects.create(user_id=instance)
