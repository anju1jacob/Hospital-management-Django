"""
URL configuration for hospitalmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from hospital import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("loging", views.loging, name="loging"),
    path("Logout", views.Logout, name="Logout"),
    path("welcome", views.welcome, name="welcome"),
    path("waitinglist", views.waitinglist, name="waitinglist"),

# Admin module paths
    path("admin_home", views.admin_home, name="admin_home"),
    path("admin_doctor", views.admin_doctor, name="admin_doctor"),
    path("admin_view_doctor", views.admin_view_doctor, name="admin_view_doctor"),
    path("admin_add_doctor", views.admin_add_doctor, name="admin_add_doctor"),
    path("admin_edit_doctor/<int:id>", views.admin_edit_doctor, name="admin_edit_doctor"),
    path("admin_update_doctor/<int:id>", views.admin_update_doctor, name="admin_update_doctor"),
    path("admin_delete_doctor/<int:id>", views.admin_delete_doctor, name="admin_delete_doctor"),
    path("admin_view_doctor_Specialisation", views.admin_view_doctor_Specialisation, name="admin_view_doctor_Specialisation"),
    
    path("admin_patient", views.admin_patient, name="admin_patient"),
    path("admin_add_patient", views.admin_add_patient, name="admin_add_patient"),
    path("admin_view_patient", views.admin_view_patient, name="admin_view_patient"),
    path("admin_delete_patient/<int:id>", views.admin_delete_patient, name="admin_delete_patient"),
    path("admin_edit_patient/<int:id>", views.admin_edit_patient, name="admin_edit_patient"),
    path("admin_update_patient/<int:id>", views.admin_update_patient, name="admin_update_patient"),

    path("admin_appointment", views.admin_appointment, name="admin_appointment"),
    path("admin_add_appointment", views.admin_add_appointment, name="admin_add_appointment"),
    path("admin_view_appointment", views.admin_view_appointment, name="admin_view_appointment"),


    # doctor module paths

    path("doctor_home", views.doctor_home, name="doctor_home"),
    path("doctor_patient", views.doctor_patient, name="doctor_patient"),
    path("doctor_view_patient", views.doctor_view_patient, name="doctor_view_patient"),
    path("doctor_appointment", views.doctor_appointment, name="doctor_appointment"),
    path("doctor_view_appointment", views.doctor_view_appointment, name="doctor_view_appointment"),
    path("doctor_delete_appointment", views.doctor_delete_appointment, name="doctor_delete_appointment"),
    path("delete_appointment/<int:id>", views.delete_appointment, name="delete_appointment"),
    path("doctor_signup", views.doctor_signup, name="doctor_signup"),

    # patient module path

    path("patient_home", views.patient_home, name="patient_home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)