from django.contrib import admin
from . import models

# Register your models here.


class ImageInline(admin.TabularInline):
    model = models.Image
    row_id_fields = ['image']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'slug', 'price', 'newest', 'most_populer'
    ]
    list_filter = [
        'created', 'updated', 'newest', 'most_populer'
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }

    search_fields = ['title', 'description']

    list_editable = ['slug', 'price', 'newest', 'most_populer']

    inlines = [ImageInline]


admin.site.register(models.Like)
admin.site.site_header = 'TimeZone'
