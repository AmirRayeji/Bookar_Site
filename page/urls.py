from django.urls import path

from page import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]

