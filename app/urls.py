from django.urls import path
from django.urls import path
from . import views
app_name = 'colorpicker'
urlpatterns = [
    path('', views.color, name='color'),
]
