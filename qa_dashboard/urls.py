"""qa_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin

from projectadmin import views as pView
from qatestrepo import views as tpView

urlpatterns = [
               
    url(r'^$',              pView.home,        name='home'),
    url(r'^login/',         pView.login,       name='login'),
    url(r'^logout/',        pView.logout,      name='logout'),
    url(r'^register/',      pView.register,    name='register'),
    
    url(r'^restricted/',    pView.restricted,  name='restricted'), # FIXME

    url(r'^testplan/$',         tpView.addTestPlan,     name='testplan'),
#     url(r'^testplan/(?P<pk>\d+)',  tpView.UpdateTestPlanView.as_view() ,    name='editTestPlan'),
    url(r'^testplans/',         tpView.showTestPlans,   name='testplans'),
    url(r'^testplan/(?P<id>\d+)/$',  tpView.editTestPlan ,    name='editTestPlan'),

    url(r'^admin/',     include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
