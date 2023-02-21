from .views import (homeDash, register_request)
from django.urls import path


app_name = 'basar'
urlpatterns = [
    path('', homeDash.as_view(), name='dash'),
    path('register/', register_request, name='register'),

]