from django.urls import path,include
from .views import HomePage
app_name='main_app'
urlpatterns = [
    path("",HomePage.as_view(),name='home'),
]
