from django.contrib import admin
from Order.models import Order, BasketItem, Basket, Payment, OrderItem
from django.utils.translation import ngettext
from django.contrib import messages


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['create_at', 'update_at', 'description']}),
                 ('Related Table Information', {'fields': ['user'], 'classes': ['collapse']}),
                 ]
    list_display = ('user', 'create_at', 'update_at', 'description')
    list_filter = ['user']
    search_fields = ['user']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Order was successfully Entered.',
            '%d Order was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Order as Entered"
    actions = [make_published]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['count', 'price']}),
                 ('Related Table Information', {'fields': ['order', 'shop_product']}),
                 ]
    list_display = ('order', 'shop_product', 'count', 'price')
    list_filter = ['price', 'count', 'order']
    search_fields = ['order']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d OrderItem was successfully Entered.',
            '%d OrderItem was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected OrderItem as Entered"
    actions = [make_published]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['amount']}),
                 ('Related Table Information', {'fields': ['user', 'order'], 'classes': ['collapse']}),
                 ]
    list_display = ('user', 'order', 'amount')
    list_filter = ['user', 'amount']
    search_fields = ['user', 'order']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Payment was successfully Entered.',
            '%d Payment was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Payment as Entered"
    actions = [make_published]


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['user']})]
    list_display = ('user',)
    list_filter = ['user']
    search_fields = ['user']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Basket was successfully Entered.',
            '%d Basket was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Basket as Entered"
    actions = [make_published]


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['price']}),
                 ('Related Table Information', {'fields': ['basket', 'shop_product']}),
                 ]
    list_display = ('shop_product', 'basket', 'price')
    list_filter = ['basket', 'shop_product']
    search_fields = ['basket', 'shop_product']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d BasketItem was successfully Entered.',
            '%d BasketItem was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected BasketItem as Entered"
    actions = [make_published]
