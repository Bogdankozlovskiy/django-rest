from django.contrib import admin
from .models import Visit


class VisitAdmin(admin.ModelAdmin):
    readonly_fields = ['date_of_ring_for_visit']


admin.site.register(Visit, VisitAdmin)
# Register your models here.
