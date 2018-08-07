from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_screenshot, name='request'),
    path('list/', views.ListPageView.as_view(), name='list'),
    path('view/<int:pk>/', views.view_screenshot, name='view'),
]
