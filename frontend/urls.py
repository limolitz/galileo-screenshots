from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('screenshots/new/', views.ScreenshotCreate.as_view(), name='request'),
    path('screenshots/list/', views.ListPageView.as_view(), name='list'),
]
