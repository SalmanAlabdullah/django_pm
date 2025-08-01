from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_per_page = 6
    list_editable = ['status']


