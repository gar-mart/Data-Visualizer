from django.urls import path
from . import views



urlpatterns = [
    path('visualize/', views.visualize, name="visualize"),
    path('regression/', views.regression, name="regression"),
    path('get_user_table_columns/', views.get_user_table_columns, name='get_user_table_columns'),
    path('view_table/<int:ug_table_id>/<int:page>/', views.view_table, name='view_table'),



]

