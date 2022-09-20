from django.db import models


class Employee(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Работник"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ('id', )


    def __str__(self):
        return self.name