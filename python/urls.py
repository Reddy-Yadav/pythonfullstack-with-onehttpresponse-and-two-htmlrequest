from django.urls import path
from python.views import *
app_name='thatthing'
urlpatterns=[
    path('reddy/',reddy,name='reddy'),
]