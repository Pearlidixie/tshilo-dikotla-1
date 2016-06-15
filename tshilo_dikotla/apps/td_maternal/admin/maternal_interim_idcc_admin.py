from collections import OrderedDict

from django.contrib import admin

from edc_export.actions import export_as_csv_action

from tshilo_dikotla.apps.td.base_model_admin import BaseModelAdmin

from ..forms import MaternalInterimIdccForm
from ..models import MaternalInterimIdcc
from .base_maternal_model_admin import BaseMaternalModelAdmin


class MaternalInterimIdccAdmin(BaseMaternalModelAdmin):

    form = MaternalInterimIdccForm

    radio_fields = {'info_since_lastvisit': admin.VERTICAL}

    list_display = ('report_datetime', 'recent_cd4', 'recent_vl', 'recent_hepb', 'recent_hepc',)

    list_filter = ('info_since_lastvisit', 'recent_cd4_date', 'recent_vl_date', 'recent_hepb_date', 
                   'recent_hepc_date')

admin.site.register(MaternalInterimIdcc, MaternalInterimIdccAdmin)