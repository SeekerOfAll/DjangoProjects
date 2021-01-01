from django.contrib import admin
from .models import Product, ShopProduct, Comment, Image, Brand, Category, ProductMeta, Likes
from django.utils.translation import ngettext
from django.contrib import messages


class ChildrenInLine(admin.TabularInline):
    model = Category
    extra = 1
    show_change_link = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'slug', 'detail', 'image']}),
                 ('Related Table Information', {'fields': ['brand', 'category'], 'classes': ['collapse']}),
                 ]
    list_display = ('name', 'detail', 'brand', 'category')
    list_filter = ['name', 'slug']
    search_fields = ['name', 'slug', 'brand', 'category']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Product was successfully Entered.',
            '%d Product was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Product as Entered"
    actions = [make_published]


@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['price', 'quantity']}),
                 ('Related Table Information', {'fields': ['product', 'shop'], 'classes': ['collapse']})]
    list_display = ('quantity', 'price', 'product', 'shop')
    list_filter = ['price', 'quantity']
    search_fields = ['product', 'shop']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d price and quantity was successfully Entered.',
            '%d price and quantity was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected price and quantity as Entered"
    actions = [make_published]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['text', 'rate']}),
                 ('Related Table Information', {'fields': ['user', 'product'], 'classes': ['collapse']}),
                 ]
    list_display = ('user', 'product', 'text', 'rate')
    list_filter = ['rate', 'user']
    search_fields = ['user', 'product']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Comment was successfully Entered.',
            '%d Comment was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Comment as Entered"
    actions = [make_published]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['image']}),
                 ('Related Table Information', {'fields': ['product'], 'classes': ['collapse']}),
                 ]
    list_display = ('product', 'image')
    list_filter = ['product']
    search_fields = ['product']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Image was successfully Entered.',
            '%d Image was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Image as Entered"
    actions = [make_published]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    field = ['name', 'slug', 'detail', 'image']
    list_display = ('name', 'slug', 'detail')
    list_filter = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Brand was successfully Entered.',
            '%d Brand was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Brand as Entered"
    actions = [make_published]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'slug', 'detail', 'image']}),
                 ('Related Table Information', {'fields': ['parent'], 'classes': ['collapse']}),
                 ]
    list_display = ('name', 'slug', 'detail', 'parent')
    list_filter = ['name', 'slug']
    search_fields = ['name', 'slug']
    inlines = [ChildrenInLine]
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Category was successfully Entered.',
            '%d Category was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Category as Entered"
    actions = [make_published]


@admin.register(ProductMeta)
class ProductMetaAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['label', 'value']}),
                 ('Related Table Information', {'fields': ['product'], 'classes': ['collapse']}),
                 ]
    list_display = ('label', 'value', 'product')
    list_filter = ['label']
    search_fields = ['label']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d ProductMeta was successfully Entered.',
            '%d ProductMeta was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected ProductMeta as Entered"
    actions = [make_published]


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    field = ['user', 'product', 'condition']
    list_display = ('user', 'product', 'condition')
    list_filter = ['condition']
    search_fields = ['condition']
    list_per_page = 5
