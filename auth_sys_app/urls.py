from django.urls import path
from . import views

urlpatterns=[
    path('signup/',views.register_view,name='register'),
    path('home/',views.home_view,name='home'),
    path('signin/',views.signin_view,name='login'),
    path('about/',views.about_view,name='about'),
    path('signout/',views.signout_view,name='logout')
]