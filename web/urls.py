from django.urls import path
from web.views import *
app_name='learn'
urlpatterns=[
    path('siva/',siva,name='siva'),
]