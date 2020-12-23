from django.urls import path, re_path
from .views import CategoryArchive, CategoryDetail, login_view, logout_view, register_view, PostArchive, PostDetail

urlpatterns = [
    # path('', home, name='posts_archive'),
    path('', PostArchive.as_view(), name='posts_archive'),  # class base view

    # path('posts/<slug:pk>/', post_single, name='post_single'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post_single'),  # class base view

    # path('categories/', categories_archive, name='categories_archive'),
    path('categories/', CategoryArchive.as_view(), name='categories_archive'),  # class base view

    # path('categories/<slug:pk>/', category_single, name='category_single'),
    path('categories/<slug:slug>/', CategoryDetail.as_view(), name='category_single'),  # class base view

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
