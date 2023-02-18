from .views import (homeDash,registerDash)
from django.urls import path


app_name = 'basar'
urlpatterns = [
    path('', homeDash.as_view(), name='dash'),
    path('register/', registerDash.as_view(), name='register'),

]