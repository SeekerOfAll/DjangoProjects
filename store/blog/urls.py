from django.urls import path

from .api import post_list, post_detail, comment_list, comment_detail
from .views import CategoryArchive, like_comment, CategoryDetail, PostArchive, \
    PostDetail, create_comment

urlpatterns = [
    # path('', home, name='posts_archive'),
    path('', PostArchive.as_view(), name='posts_archive'),  # class base view

    # path('posts/<slug:pk>/', post_single, name='post_single'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post_single'),  # class base view

    # path('categories/', categories_archive, name='categories_archive'),
    path('categories/', CategoryArchive.as_view(), name='categories_archive'),  # class base view

    # path('categories/<slug:pk>/', category_single, name='category_single'),
    path('categories/<slug:slug>/', CategoryDetail.as_view(), name='category_single'),  # class base view

    path('like_comment/', like_comment, name='like_comment'),
    path('comments/', create_comment, name='add_comment'),
    path('api/posts/', post_list, name='post_list'),
    path('api/posts/<int:pk>/', post_detail, name='post_detail'),
    path('api/comments/', comment_list, name='comment_list'),
    path('api/comments/<int:pk>/', comment_detail, name='comment_detail'),
]
