from django.contrib import admin

from .models import Group, Post, Comment, Follow


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = 'none'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'author', 'post',)
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = 'none'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following',)
    empty_value_display = 'none'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
