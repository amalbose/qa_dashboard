from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import QATestPlanForm
from .models import QATestPlan

# Create your views here.
def home(request):
    context = {
    "title" : "Create new testplan"
    }
    return render(request, "home.html" , context);

def showTestPlans(request):
    query_results = QATestPlan.objects.all()
    context = {
    "title" : "QA TestPlans", "results" : query_results
    }
    return render(request, 'showtestplans.html' , context);

def editTestPlan(request, id):
    instance = get_object_or_404(QATestPlan, plan_id=id)
    form = QATestPlanForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/testplans")
#     return direct_to_template(request, 'my_template.html', {'form': form}     
    context = {
    "title" : "QA TestPlans", "form" : form
    }
    return render(request, 'edittestplan.html' , context);

def addTestPlan(request):
    form = QATestPlanForm(request.POST or None);
    context = {
    "title" : "Create Testplan", "form" : form
    }
    ret_page = 'testplanform.html';
    if form.is_valid():
        form.save(commit=True);
        return HttpResponseRedirect("/testplans")
    return render(request, ret_page , context);
