from django.urls import path
from app import views

urlpatterns = [
    path("myapi/", views.api_list),
    path("apidetails/<int:pk>/", views.api_detail),
]
