from django.contrib import admin
from main.models import HeadphoneMain, History
from import_export.admin import ImportExportModelAdmin
from import_export import resources

### Register your models here. ###

### 관리자 화면 기능 upgrade ###

# admin.site.register(HeadphoneMain) -> 데코레이터 형태로 바꾸어 사용안함

@admin.register(HeadphoneMain)
class HeadphoneMainAdmin(admin.ModelAdmin):
    list_display = ['hp_model', 'hp_serial', 'hp_pDate', 'hp_pDetail', 'hp_rDate', 'hp_rDetail', 'hp_receiver', 'hp_checker']
    list_filter = ['hp_serial']
    search_fields = ('hp_serial',)
      
@admin.register(History)
class HistoryAdmin(ImportExportModelAdmin):
    resources_class = History
    list_display = ['h_model', 'h_serial', 'h_pDate', 'h_pDetail', 'h_rDate', 'h_rDetail', 'h_receiver', 'h_checker'] 
    list_filter = ['h_serial']
    search_fields = ('h_serial',)

# admin.site.register(History, HistoryAdmin) admin customize를 위해 decorator 형으로 바꿈

### 관리자 화면 텍스트 편집 ###
admin.site.site_header = "헤드폰 지급/반납 관리자"
admin.site.site_title = "헤드폰 지급/반납 관리 포탈"
admin.site.index_title = "Welcome to Headphone Manager Portal"