# api_calls/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('make-api-calls/', views.make_api_calls, name='make_api_calls'),
]
