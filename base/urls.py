from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='about'),
    path('education/', views.education, name='education'),
    path('experience', views.experience, name='experience')
]
