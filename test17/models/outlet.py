from django.db import models


class Outlet(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Торговая точка'
    )
    employee = models.ForeignKey(
        'test17.Employee',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'
        ordering = ('id', )