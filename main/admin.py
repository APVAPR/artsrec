from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Category)

