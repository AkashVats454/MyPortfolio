from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('',views.HomeTemplateView.as_view(),),
    path('user_info/', views.user_info, name='user_info'),
]
