
from django.conf import settings as _settings
from django.utils.translation import ugettext_lazy as _

class Settings(object):

    GMAP_TABLE_DEFAULT_TEMPLATE = \
        "gamp_table/Default.html"

    GMAP_TABLE_TEMPLATES = [
        (GMAP_TABLE_DEFAULT_TEMPLATE, _("Default")),
    ]

    if hasattr(_settings, 'GMAP_TABLE_TEMPLATES'):
        for ele in _settings.GMAP_TABLE_TEMPLATES:
            if not ele[0] == "gmap_table/Default.html":
                GMAP_TABLE_TEMPLATES.append(ele)

settings = Settings()
