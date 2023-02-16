from .views import (homeDash,)
from django.urls import path


app_name = 'basar'
urlpatterns = [
    path('', homeDash.as_view(), name='dash'),

]