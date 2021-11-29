from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_post', 'user', 'date_create')
    list_display_links = ('id', 'title_post')
    search_fields = ('title_post', 'content')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('author', 'title')}


admin.site.register(Post, PostAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Image)
admin.site.register(Category)

