"""
URL configuration for carsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import LabGroupMembersView, SignUpView

app_name = 'carapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('lab_group_members/', LabGroupMembersView.as_view(), name='lab_group_members'),
    path('<int:cartype_no>/', views.cardetail, name='cardetail'),
    path('info_display/', views.info_display, name='info_display'),
    path('aboutus/', views.aboutUs, name='aboutUs'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('orderhere/', views.orderhere, name='orderhere'),
    path('vsearch/', views.vsearch, name='vsearch'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.login_here, name='login'),
    path('logout/', views.logout_here, name='logout'),
]
