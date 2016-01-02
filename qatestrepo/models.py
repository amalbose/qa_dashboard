from django.db import models

from projectadmin.models import UserProfile


class QATestPlan(models.Model):
    plan_id         = models.AutoField(primary_key=True);
    testplan_id     = models.CharField(max_length=50,blank=True, null=True);
    testplan_name   = models.CharField(max_length=200);
    testplan_owner  = models.ForeignKey(UserProfile,related_name='+',blank=True, null=True);
    owner           = models.ForeignKey(UserProfile,blank=True, null=True,related_name='+');
    release         = models.CharField(max_length=100, blank=True);
    build           = models.CharField(max_length=100, blank=True);
    team            = models.CharField(max_length=100, blank=True);
    created_time    = models.DateTimeField(auto_now_add=True, auto_now=False);
    modified_time   = models.DateTimeField(auto_now_add=False, auto_now=True);
    active          = models.BooleanField(default='Yes')
    def __str__(self):
        return self.testplan_name;