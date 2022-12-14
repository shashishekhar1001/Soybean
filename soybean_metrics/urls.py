from django.urls import include, path
from . import views

app_name = 'soybean_metrics'
urlpatterns = [
    path('', views.soybean_metrics_home, name='soybean_metrics_home'),
    path('get_purchase', views.get_purchase, name='get_purchase'),
]