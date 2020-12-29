from django.urls import path
from .views import CategoryArchive, like_comment, CategoryDetail, SignInView, LogoutView, SignUpView, PostArchive, \
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

    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('like_comment/', like_comment, name='like_comment'),
    path('comments/', create_comment, name='add_comment'),
]
