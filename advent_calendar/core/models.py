from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from filer.fields.image import FilerImageField


class Day(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name='Число месяца',
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    )
    month = models.PositiveSmallIntegerField(
        verbose_name='Месяц',
        validators=[MinValueValidator(1), MaxValueValidator(12)],
    )
    candy = FilerImageField(
        verbose_name='Сладость',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'дни'
    
    def __str__(self):
        return f' День {self.number} месяца {self.month}'
