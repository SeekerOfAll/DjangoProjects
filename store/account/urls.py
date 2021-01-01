from django.urls import path

from account.api import user_list, user_detail
from account.views import SignInView, LogoutView, SignUpView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('api/users/', user_list, name='comment_list'),
    path('api/users/<int:pk>/', user_detail, name='comment_detail'),

]
