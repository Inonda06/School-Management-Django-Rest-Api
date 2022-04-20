from django.contrib import admin
from .models import WaitListEnty

@admin.register(WaitListEnty)
class WaitListAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    list_filter = ('email',)

