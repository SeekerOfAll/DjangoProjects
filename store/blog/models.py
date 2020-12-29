from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .validators import validate_password, validate_username


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True
                               , related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.slug


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    content = models.TextField(_("Content"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)
    draft = models.BooleanField(_("Draft"), default=True, db_index=True)
    image = models.ImageField(_("Image"), upload_to='post/images')
    category = models.ForeignKey(Category, related_name='posts', verbose_name="Category",
                                 on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, related_name='posts', related_query_name='children', verbose_name=_("Author"),
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-publish_time']

    def __str__(self):
        return self.title


class PostSetting(models.Model):
    post = models.OneToOneField(
        "Post", verbose_name=_("post"), related_name='post_setting', on_delete=models.CASCADE)
    comment = models.BooleanField(_("comment"))
    author = models.BooleanField(_("author"))
    allow_discussion = models.BooleanField(_("allow discussion"))

    class Meta:
        verbose_name = _("PostSetting")
        verbose_name_plural = _("PostSettings")


class Comment(models.Model):
    content = models.TextField(_("Content"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    post = models.ForeignKey("blog.Post", verbose_name=_("Post"), related_name="comments",
                             related_query_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("Confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["-create_at"]

    def __str__(self):
        return self.post.title

    @property
    def like_count(self):
        q = CommentLike.objects.filter(comment=self, condition=True)
        return q.count()

    @property
    def dislike_count(self):
        q = self.comment_like.filter(condition=False)
        return q.count()


class CommentLike(models.Model):
    condition = models.BooleanField(_("Condition"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    comment = models.ForeignKey("blog.Comment", verbose_name=_("Comment"), related_name='comment_like',
                                related_query_name='comment_like', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)

    class Meta:
        unique_together = [['author', 'comment']]
        verbose_name = _("CommentLike")
        verbose_name_plural = _("CommentLikes")

    def __str__(self):
        return str(self.condition)


class Register(models.Model):
    username = models.CharField(verbose_name=_('username'), max_length=150,
                                validators=[validate_username])
    email = models.EmailField(verbose_name=_('email'), max_length=150)
    password = models.CharField(verbose_name=_('password'), max_length=150, validators=[validate_password])
    password2 = models.CharField(verbose_name=_('password2'), max_length=150)
    first_name = models.CharField(verbose_name=_('first_name'), max_length=150)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=150)
