
from django.db import models

from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

# This might need to be adjusted to fit in any project
from gmap_table import settings

# Create your models here.


class GmapTable(CMSPlugin):
    apiKey = models.CharField(max_length=100)
    renderTemplate = models.CharField(
        _('GMap Table Template'), max_length=150, blank=True,
        choices=settings.GMAP_TABLE_TEMPLATES,
        default=settings.GMAP_TABLE_DEFAULT_TEMPLATE,
    )
    
    class Meta:
        verbose_name = _("GMap Table")
        verbose_name_plural = _("GMap Table")

class GmapPostion(models.Model):
    gmap = models.ForeignKey(GmapTable, related_name="positions")
    region = models.CharField(max_length=60)
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    coordinate = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = _('Positions')
        verbose_name = _('Positions')
    
