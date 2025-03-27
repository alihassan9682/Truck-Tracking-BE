from django.urls import path
from .views import signuppage, loginpage, person_data

urlpatterns = [
    path("signup/",signuppage.as_view(),name = "signup"),
    path("login/",loginpage.as_view(),name = "login"),
    path("get_person_detail/",person_data.as_view(),name = "details"),
]
