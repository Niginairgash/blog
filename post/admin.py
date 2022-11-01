from django.contrib import admin
from post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

