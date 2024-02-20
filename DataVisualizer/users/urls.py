from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
   
   # path('upload/', views.upload, name="upload"),
    path('upload/', views.upload, name='upload'),

    path('profiles/', views.profiles, name="profiles"),


    path('register/', views.register, name='register'),
    path('my_assets/', views.my_assets, name='my_assets'),
    


]


