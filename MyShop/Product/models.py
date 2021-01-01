from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# Create your models here.

class Product(models.Model):
    brand = models.ForeignKey('Product.Brand', verbose_name=_("Brand"), related_name='Product',
                              related_query_name='Product', on_delete=models.CASCADE)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    category = models.ForeignKey('Product.Category', verbose_name=_("Category"), related_name='Product',
                                 related_query_name='Product', on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=150)
    image = models.ImageField(_('Image'), upload_to='product/image/', max_length=100)
    detail = models.CharField(_('Detail'), max_length=150)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name

    @property
    def like_count(self):
        q = Likes.objects.filter(comment=self, condition=True)
        return q.count()

    @property
    def dislike_count(self):
        q = Likes.objects.filter(comment=self, condition=False)
        return q.count()


class ShopProduct(models.Model):
    shop = models.ForeignKey('Account.Shop', verbose_name=_('Shop'), related_name='ShopProduct',
                             related_query_name='ShopProduct', on_delete=models.CASCADE)
    product = models.ForeignKey('Product.Product', verbose_name=_('Product'), related_name='ShopProduct',
                                related_query_name='ShopProduct', on_delete=models.CASCADE)
    price = models.CharField(_('Price'), max_length=50)
    quantity = models.CharField(_('Quantity'), max_length=50)

    class Meta:
        verbose_name = _('shop_product')
        verbose_name_plural = _('shops_products')

    def __str__(self):
        return self.price


class Comment(models.Model):
    text = models.TextField(_('Text'), blank=True, help_text="Enter Your Comment")
    rate = models.IntegerField(_('Rate'), blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name='Comment',
                             related_query_name='Comment', on_delete=models.CASCADE)
    product = models.ForeignKey("Product.Product", verbose_name=_("Product"), related_name='Comment',
                                related_query_name='Comment', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.product.name


class Image(models.Model):
    product = models.ForeignKey("Product.Product", verbose_name=_("Product"), related_name='Image',
                                related_query_name='Image', on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='image/image/', max_length=100)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    detail = models.TextField(_('Detail'), blank=False, help_text="Enter Your Brand Detail")
    image = models.ImageField(_('Image'), upload_to='brand/image/', max_length=100)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    detail = models.TextField(_('Detail'), blank=True, help_text="Enter Your Category Detail")
    image = models.ImageField(_('Image'), upload_to='category/image/', max_length=100)
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True
                               , related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class ProductMeta(models.Model):
    product = models.ForeignKey("Product.Product", verbose_name=_("Product"), related_name='ProductMeta',
                                related_query_name='ProductMeta', on_delete=models.CASCADE)
    label = models.CharField(_('Label'), max_length=50)
    value = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = _('product_meta')
        verbose_name_plural = _('product_metas')

    def __str__(self):
        return self.label


class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE,
                             related_name='like', related_query_name='like')
    product = models.ForeignKey('Product.Product', verbose_name=_("product"), on_delete=models.CASCADE,
                                related_name='product',related_query_name='product')
    condition = models.BooleanField(_("Condition"))

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')

    def __str__(self):
        return self.product.name


class Page(models.Model):
    pass

    class Meta:
        pass

    def __str__(self):
        pass


class Off(models.Model):
    pass

    class Meta:
        pass

    def __str__(self):
        pass
