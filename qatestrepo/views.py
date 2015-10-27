from django.shortcuts import render

from .forms import QATestPlanForm

# Create your views here.
def home(request):
    form = QATestPlanForm(request.POST or None);
    
    context = {
    "title" : "Create new testplan", "form" : form
    }
    ret_page = 'testplanform.html';
    
    if form.is_valid():
        form.save(commit=True);
        ret_page = 'thankyou.html';
        context = {
            "title" :"Thank You"
        }
    return render(request,ret_page , context);
