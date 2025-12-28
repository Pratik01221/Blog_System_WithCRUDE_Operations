from django.contrib import admin
from .models import About, Sociallinks

# Register your models here.

class Aboutadmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count ==0:
            return True
        return False

admin.site.register(About, Aboutadmin)
admin.site.register(Sociallinks)