from django.contrib import admin

from .models import Comment, Group, Post
from yatube_api.settings import EMPTY_VALUE_DISPLAY


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    посты
    """
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        'image'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    отоброжение групп.
    """
    list_display = ('title',)
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    отображение комментариев
    """
    list_display = (
        'post',
        'text',
        'author',
        'created'
    )
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = EMPTY_VALUE_DISPLAY
