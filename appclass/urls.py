from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyFormView.as_view(), name='home'),
]