from django.db import models
from django.utils.translation import gettext_lazy as _


class Astronaut(models.Model):
    MAX_HEIGHT = 220
    MIN_HEIGHT = 100

    first_name = models.CharField(verbose_name=_("First Name"), max_length=30)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=30)
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"), blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Astronaut')
        verbose_name_plural = _('Astronauts')
