from django.contrib import admin
from .models import  Lecture


@admin.register(Lecture)
class LecturesAdmin(admin.ModelAdmin):
    list_display = ('title','description','lecture_name')
    search_fields = ('title',)
