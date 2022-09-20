from django.db import models


class Visit(models.Model):
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name="created_at"
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='updated_at'
    )
    outlet = models.ForeignKey(
        'test17.Outlet',
        on_delete=models.DO_NOTHING,
        related_name='outlet',
        verbose_name='Торговая точка',
        blank=True,
        null=True
    )


    def __str__(self):
        return self.outlet

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural ='Посещения'
        ordering = ('id', )