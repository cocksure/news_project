from django.contrib import admin
from .models import Category, News,Contacts


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'updated_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {
        "slug": ('title',)}
    date_hierarchy = "publish_time"
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['name']


admin.site.register(Contacts)