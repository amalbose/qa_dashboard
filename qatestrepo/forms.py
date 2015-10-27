from django import forms

from .models import QATestPlan


class QATestPlanForm(forms.ModelForm):
    ''' Form for testplan '''
    class Meta:
        model = QATestPlan
        fields = ['testplan_name','owner','team','release']
        
    def clean_release(self):
        rel = self.cleaned_data.get('release');
        if not "Release" in rel:
            raise forms.ValidationError("Use Release<NO> form");
        return rel;