from django.contrib import admin
from post.models import Post, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags",)
    readonly_fields = ('created_at', 'update_at')

    def get_text(self, instance):
        pass

