from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Order(models.Model):
    create_at = models.DateTimeField(_("create at"), )
    update_at = models.DateTimeField(_("update at"), )
    description = models.TextField(_("description"), )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.CASCADE,
                             related_name='order',
                             related_query_name='order')

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return self.user.first_name


class OrderItem(models.Model):
    count = models.IntegerField(_("count"), )
    price = models.IntegerField(_("price"), )
    order = models.ForeignKey("Order.Order", verbose_name=_('order'), on_delete=models.CASCADE,
                              related_name='orderItem', related_query_name='orderItem')
    shop_product = models.ForeignKey("Product.ShopProduct", verbose_name=_('shop_product'), on_delete=models.CASCADE,
                                     related_name='shop_product', related_query_name='shop_product')

    class Meta:
        verbose_name = _('orderItem')
        verbose_name_plural = _('orderItems')

    def __str__(self):
        return self.price

    @property
    def total_price(self):
        return self.price * self.count


class Payment(models.Model):
    amount = models.IntegerField(_('amount'), )
    order = models.OneToOneField('Order.Order', verbose_name=_('order'), on_delete=models.CASCADE,
                                 related_name='payment', related_query_name='payment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE,
                             related_name='payment', related_query_name='payment')

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return self.amount


class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE,
                                related_name='basket', related_query_name='basket')

    class Meta:
        verbose_name = _('basket')
        verbose_name_plural = _('baskets')

    def __str__(self):
        return self.user.first_name


class BasketItem(models.Model):
    price = models.IntegerField(_('price'), )
    basket = models.ForeignKey('Order.Basket', verbose_name=_('basket'), on_delete=models.CASCADE,
                               related_name='basketItem', related_query_name='basketItem')
    shop_product = models.ForeignKey('Product.ShopProduct', verbose_name=_('shop_product'), on_delete=models.CASCADE,
                                     related_name='basketItem', related_query_name='basketItem')

    class Meta:
        verbose_name = _('basketItem')
        verbose_name_plural = _('basketItems')

    def __str__(self):
        return self.price
