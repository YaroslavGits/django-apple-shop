from django.contrib import admin
from .models import *

# Register your models here.
class SabscriberAdmin(admin.ModelAdmin):
    class Meta:
        model = Sabscriber
    search_fields = ["sabscriber_name", "sabscriber_email"]
    fields = ["sabscriber_name", "sabscriber_email"]


admin.site.register(Sabscriber, SabscriberAdmin)