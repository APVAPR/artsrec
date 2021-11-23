from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_post', 'user', 'date_create')
    list_display_links = ('id', 'title_post')
    search_fields = ('title_post', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Category)

