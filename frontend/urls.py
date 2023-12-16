
from django.urls import  path
from . import views


urlpatterns = [
        path('',views.home,name="home"),
        path('login/',views.signIn,name="login"),
        path('logout/',views.Logout,name="logout"),
        path('register/',views.register,name="register"),
        path('tools/',views.tools,name="tools"),
]
