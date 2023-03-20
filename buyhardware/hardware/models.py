from django.db import models
from django.utils.translation import gettext_lazy as _


class HardwareType(models.Model):

    type = models.CharField(
        primary_key=True,
        max_length=100,
        verbose_name=_('тип'),
        help_text=_('Тип оборудования')
    )

    description = models.CharField(
        max_length=300,
        verbose_name=_('описание'),
        help_text=_('Описание типа')
    )

    class Meta:
        verbose_name = _('Тип оборудования')
        verbose_name_plural = _('Типы оборудования')


class Hardware(models.Model):

    hardware_id = models.AutoField(
        primary_key=True,
        verbose_name=_('id'),
        help_text=_('Id оборудования')
    )

    hardware_type = models.ForeignKey(
        HardwareType,
        max_length=50,
        on_delete=models.CASCADE,
        verbose_name=_('тип'),
        help_text=_('Тип оборудования')
    )

    short_desc = models.CharField(
        max_length=200,
        verbose_name=_('краткое описание'),
        help_text=_('Краткое описание характеристик оборудования')
    )

    full_desc = models.CharField(
        max_length=1000,
        verbose_name=_('полное описание'),
        help_text=_('Полное описание характеристик оборудования')
    )

    price = models.DecimalField(
        max_digits=65535,
        decimal_places=65535,
        verbose_name=_('стоимость'),
        help_text=_('Стоимость оборудования')
    )

    pic = models.ImageField(
        upload_to='hardware',
        default='default.png',
        width_field=1000,
        height_field=800,
        verbose_name=_('превью'),
        help_text=_('Превью оборудования')
    )

    class Meta:
        verbose_name = _('Оборудование')
        verbose_name_plural = _('Оборудование')
