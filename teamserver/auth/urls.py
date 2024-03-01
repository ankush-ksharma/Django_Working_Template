from django.urls import path
from auth import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', views.handlelogin, name="hanglelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
]
