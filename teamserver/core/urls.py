from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects', views.projects, name="projects"),
    path('agents', views.agents, name="agents"),
    path('team', views.team, name="team"),
    path('test', views.test, name="test"),
]
