from django.urls import path
from django.urls import path
from . import views
app_name = 'colorpicker'
urlpatterns = [
    path('', views.color, name='color'),
    path('token',views.get_csrf_token,name='token')
]
