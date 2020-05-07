from django.contrib import admin
from main.models import HeadphoneMain, History
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
admin.site.register(HeadphoneMain)
        
class HistoryAdmin(ImportExportModelAdmin):
    resources_class = History

admin.site.register(History, HistoryAdmin)