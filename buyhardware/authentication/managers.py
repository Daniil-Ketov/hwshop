from django.contrib.auth.models import BaseUserManager


class UserManger(BaseUserManager):
    def _create_user(self, login, email, password, **extra_fields):
        if not email:
            raise ValueError('У пользователя должен быть задан email')

        if not extra_fields.get('phone_number'):
            raise ValueError('У пользователя должен быть задан номер телефона')

        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(login, email, password, **extra_fields)

    def create_superuser(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Администратор обязан иметь поле персонал=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Администратор обязан иметь поле администратор=True')

        return self._create_user(login, email, password, **extra_fields)
