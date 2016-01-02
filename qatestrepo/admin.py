from django.contrib import admin

# Register your models here.
from .models import QATestPlan
from .forms import QATestPlanForm

class QATestPlanAdmin(admin.ModelAdmin):
    list_display = ["__str__","created_time", "testplan_owner", "release"]
#    class Meta:
#        model = QATestPlan
    form = QATestPlanForm
        

admin.site.register(QATestPlan, QATestPlanAdmin)
