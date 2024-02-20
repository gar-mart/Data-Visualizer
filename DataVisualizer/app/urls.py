from django.urls import path 
from . import views
from . import models

urlpatterns = [
    path('',views.simple_view),
    path('variable',views.variable_view),
    path('list',views.list_patients,name='list_patients'),
    path('listcars',views.list_cars,name='list_cars'),
    path('addcar',views.add_car,name='add_car'),
    path('deletecar',views.delete_car,name='delete_car'),
    path('stocks',views.stocks,name='stocks')

]

