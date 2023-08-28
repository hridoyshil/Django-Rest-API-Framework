from django.urls import path
from app import views

urlpatterns = [
    # path("myapi/", views.api_list),
    # path("apidetails/<int:pk>/", views.api_detail),
    # path("myapi/", views.Blog_list.as_view()),
    # path("detail/<int:pk>/", views.apiDetail.as_view()),
    path("gav/", views.ContactList.as_view()),
    path("mydetail/<int:pk>/", views.ContactDetail.as_view()),
]
