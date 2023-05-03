from django.contrib import admin
from .models import Category, News, Contacts, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'updated_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time', 'category']
    prepopulated_fields = {
        "slug": ('title',)}
    date_hierarchy = "publish_time"
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['name']


admin.site.register(Contacts)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user',  'body']
    actions = ['disable_comments', 'activated_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def activated_comments(self, request, queryset):
        queryset.update(active=True)
