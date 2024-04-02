from django.urls import path
from sql.views import *
app_name='anything'
urlpatterns=[
    path('kavitha/',kavitha,name='kavitha'),
]