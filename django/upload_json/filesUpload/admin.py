from django.contrib import admin
from .models import FileData


class JsonFileUpload(admin.ModelAdmin):
    pass

admin.site.register(FileData)
# Register your models here.
