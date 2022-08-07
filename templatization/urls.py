"""templatization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from dynamic import views as dynamic_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dynamic.urls')),
    path('smart/',dynamic_views.smart,name="smart"),
    path('digital/',dynamic_views.digital,name="digital"),
    path('covenient/',dynamic_views.convenient,name="convenient"),
    path('safe/',dynamic_views.safe,name="safe"),
    path('sustainable/',dynamic_views.sustainable,name="sustainable"),
    path('access_control/',dynamic_views.access_control,name="access_control"),
    path('availability/',dynamic_views.availability,name="availability"),
    path('digital_dashboard/',dynamic_views.digital_dashboard,name="digital_dashboard"),
    path('mobile_application/',dynamic_views.mobile_application,name="mobile_application"),
    path('sustainable/',dynamic_views.sustainable,name="sustainable"),
    path('guidance/',dynamic_views.guidance,name="guidance")
    
]
