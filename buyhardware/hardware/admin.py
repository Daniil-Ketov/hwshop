from django.contrib import admin
from hardware.models import Hardware, HardwareType


@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'short_desc', 'price')
    list_filter = ('type',)
    sortable_by = ('price',)
    search_fields = ('name',)
    readonly_fields = ('pic_preview',)


@admin.register(HardwareType)
class HardwareTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'description')
