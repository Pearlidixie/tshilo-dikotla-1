from django.contrib import admin

from tshilo_dikotla.apps.td.base_model_admin import BaseModelAdmin

from .models import (
    ChronicConditions, Contraceptives, DiseasesAtEnrollment, HouseholdGoods,
    PriorArv, AutopsyInfoSource, Supplements, InfantVaccines,
    HealthCond, DelComp, ObComp, LabDelDx, MaternalRelatives, MaternalMedications, Rations, Foods,
    Malformations)


class RationsAdmin(BaseModelAdmin):
    pass
admin.site.register(Rations, RationsAdmin)


class FoodsAdmin(BaseModelAdmin):
    pass
admin.site.register(Foods, FoodsAdmin)


class ChronicConditionsAdmin(BaseModelAdmin):
    pass
admin.site.register(ChronicConditions, ChronicConditionsAdmin)


class ContraceptivesAdmin(BaseModelAdmin):
    pass
admin.site.register(Contraceptives, ContraceptivesAdmin)


class DiseasesAtEnrollmentAdmin(BaseModelAdmin):
    pass
admin.site.register(DiseasesAtEnrollment, DiseasesAtEnrollmentAdmin)


class HouseholdGoodsAdmin(BaseModelAdmin):
    pass
admin.site.register(HouseholdGoods, HouseholdGoodsAdmin)


class MaternalMedicationsAdmin(BaseModelAdmin):
    pass
admin.site.register(MaternalMedications, MaternalMedicationsAdmin)


class PriorArvAdmin(BaseModelAdmin):
    pass
admin.site.register(PriorArv, PriorArvAdmin)


class AutopsyInfoSourceAdmin(BaseModelAdmin):
    pass
admin.site.register(AutopsyInfoSource, AutopsyInfoSourceAdmin)


class SupplementsAdmin(BaseModelAdmin):
    pass
admin.site.register(Supplements, SupplementsAdmin)


class InfantVaccinesAdmin(BaseModelAdmin):
    pass
admin.site.register(InfantVaccines, InfantVaccinesAdmin)


class HealthCondAdmin(BaseModelAdmin):
    pass
admin.site.register(HealthCond, HealthCondAdmin)


class DelCompAdmin(BaseModelAdmin):
    pass
admin.site.register(DelComp, DelCompAdmin)


class ObCompAdmin(BaseModelAdmin):
    pass
admin.site.register(ObComp, ObCompAdmin)


class LabDelDxAdmin(BaseModelAdmin):
    pass
admin.site.register(LabDelDx, LabDelDxAdmin)


class MaternalRelativesAdmin(BaseModelAdmin):
    pass
admin.site.register(MaternalRelatives, MaternalRelativesAdmin)

class MalformationsAdmin(BaseModelAdmin):
    pass
admin.site.register(Malformations, MalformationsAdmin)
