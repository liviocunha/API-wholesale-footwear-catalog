from django.contrib import admin
from .models import Category, Collection, Size, Status, Footwear, Photo


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class FootwearAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'abc_curve', 'status' )
    search_fields = ('code',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('code_footwear', 'url', 'extension')
    search_fields = ('code_footwear',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Footwear, FootwearAdmin)
admin.site.register(Photo, PhotoAdmin)
