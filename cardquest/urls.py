from django.urls import path
from . import views
from cardquest.views import HomePageView, TrainerList


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
]
