from django.urls import path
from products import views
from .views import detail_page

# app_name = 'products'

urlpatterns = [
    path('', views.home_page, name='index'),
    path('register/', views.user_create, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    # path('phone/', PhoneView.as_view(), name="phone"), 
    # path('televizor/', TVView.as_view(), name='televizor'),
    # path('washing/', Washingview.as_view(), name='washing'),
    # path('kompyuter/', Kompyuterview.as_view(), name='kompyuter'),
    path('products/<slug:slug>/', views.detail_page, name='detail'),
    path('edit-task/<slug:slug>/<int:id>/', views.edit_comment, name='edit_comment'),
    path('delete-task/<slug:slug>/<int:id>/', views.delete_comment, name='delete-comment'),
    path('create-post/', views.create_post, name='create-post'),
]
