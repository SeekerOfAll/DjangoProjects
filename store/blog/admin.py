from django.contrib import admin
from .models import Post, Category, Comment, CommentLike, PostSetting
from django.utils.translation import ngettext
from django.contrib import messages


class ChildrenItemInline(admin.TabularInline):
    model = Category
    fields = ('title', 'slug')
    extra = 1
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'parent')
    search_fields = ('slug', 'title')
    list_filter = ('parent',)
    # prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10
    inlines = [ChildrenItemInline]


class PostSettingInline(admin.TabularInline):
    model = PostSetting
    show_change_link = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'create_at', 'update_at', 'publish_time', 'draft', 'category', 'author')
    search_fields = ('title',)
    list_filter = ('draft', 'category', 'author')
    date_hierarchy = 'publish_time'
    inlines = [PostSettingInline]
    list_per_page = 5


    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d post was successfully marked as published.',
            '%d posts were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected stories as published"
    actions = [make_published]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'is_confirmed', 'like_count', 'dislike_count')
    search_fields = ('content',)
    list_filter = ('is_confirmed',)
    date_hierarchy = 'create_at'


class CommentLikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CommentLike, CommentLikeAdmin)
admin.site.register(Category, CategoryAdmin)
