from django.contrib import admin

# Register your models here.
from .models import add_post_content,User,Follow,like

admin.site.register(User)
admin.site.register(add_post_content)
admin.site.register(Follow)
admin.site.register(like)