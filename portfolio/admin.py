from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Service)
admin.site.register(Topic)
admin.site.register(Portfolio)
admin.site.register(Client)
admin.site.register(OurTeam)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Sponsor)

class AdminMe(admin.ModelAdmin):
    list_display = ['compled','happy','perspective']
admin.site.register(MyProject,AdminMe)

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','website']
admin.site.register(Contact,AdminContact)