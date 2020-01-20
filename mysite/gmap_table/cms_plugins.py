
import requests
import json
import re

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import select_template

from gmap_table import settings as gmapTableSettings
from gmap_table.models import GmapTable, GmapPostion
from boto.ec2 import instance


class Spot(object):
    def __init__(self, region, name, tel, email, coordinate):
        self.region = region
        self.name = name
        self.tel = tel
        self.email = email
        self.coordinate = coordinate

class PositionInline(admin.StackedInline):
    model = GmapPostion
    # form = FormFieldInlineForm
    extra = 1


    def get_positions(self, request, obj=None):
        fields = (
            ('region', 'name', 'tel', 'email', 'coordinate')
        )


        fieldsets = (
            (None, {
                'fields': fields
            }),
        )
        return fieldsets



class GmapTablePlugin(CMSPluginBase):
    model = GmapTable
    module = _("GMap Table")
    name = _("GMap Table")
    inlines = (PositionInline, )
    render_template = gmapTableSettings.GMAP_TABLE_DEFAULT_TEMPLATE

    def get_render_template(self, context, instance, placeholder):
        return select_template([
            instance.renderTemplate,
            gmapTableSettings.GMAP_TABLE_DEFAULT_TEMPLATE,
        ])

    def render(self, context, instance, placeholder):

        spotList = []
        for position in instance.positions.all():
            spot = Spot(
                position.region, 
                position.name,
                position.tel,
                position.email,
                position.coordinate,
            )
        
            spotList.append(spot)
        context.update({
            'spotList': spotList,
            'apiKey': instance.apiKey,
            'gmapId': instance.pk
        })

        return context




plugin_pool.register_plugin(GmapTablePlugin)
