from django.contrib import admin

from .models import UserProfile

# Register your models here.
# admin.site.register(UserProfile)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','team','empId','role')
    search_fields = ('user__username',)