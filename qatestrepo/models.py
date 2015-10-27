from django.db import models

class QATestPlan(models.Model):
    testplan_name   = models.CharField(max_length=200);
    owner           = models.CharField(max_length=200);
    release         = models.CharField(max_length=100, blank=True);
    team            = models.CharField(max_length=100, blank=True);
    createdTime     = models.DateTimeField(auto_now_add=True, auto_now=False);
    modifiedTime    = models.DateTimeField(auto_now_add=False, auto_now=True);
    
    def __str__(self):
        return self.testplan_name;