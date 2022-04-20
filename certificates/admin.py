from django.contrib import admin
from .models import  Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter =('name',)

