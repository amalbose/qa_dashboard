from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    supervisorId    = models.ForeignKey(User, related_name='+',blank=True, null=True, verbose_name="Supervisor")
    team            = models.CharField(max_length=200);
    empId           = models.CharField(max_length=10);
    
    NORMAL = 'NR'
    ADMIN = 'AD'
    ROOT = 'SU'
    ROLE_CHOICES = (
        (NORMAL, 'Normal User'),
        (ADMIN, 'Admin User'),
        (ROOT, 'Super User'),
    )
    role            = models.CharField(max_length=2,
                                      choices=ROLE_CHOICES,
                                      default=NORMAL);

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username
