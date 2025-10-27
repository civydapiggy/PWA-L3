from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('complete/<int:pk>/', views.OrderCompleteView.as_view(), name='order-complete'),
]