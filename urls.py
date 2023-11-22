"""cyberfraudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from workstationapp import views as workstationapp_views
from usersapp import views as usersapp_views
from mainapp import views as mainapp_views

urlpatterns = [
    path('admin/', admin.site.urls),

#mainapp views
   path('',mainapp_views.main_home,name='main_home'),
   path('main-about',mainapp_views.main_about,name='main_about'),
   path('main-contact',mainapp_views.main_contact,name='main_contact'),
   path('main-features',mainapp_views.main_features,name='main_features'),
   
   path('main-portfolio',mainapp_views.main_portfolio,name='main_portfolio'),
   path('main-pricing',mainapp_views.main_pricing,name='main_pricing'),
   path('main-services',mainapp_views.main_services,name='main_services'),
   path('main-testimonials',mainapp_views.main_testimonials,name='main_testimonials'),
   path('main-userregistration',usersapp_views.main_userregistration,name='main_userregistration'),
   path('main-user-login',usersapp_views.main_user_login,name='main_user_login'),
   path('main-workstationlogin',mainapp_views.main_workstationlogin,name='main_workstationlogin'),
   path('attacker',mainapp_views.attacker,name='attacker'),
   path('enyc/<int:id>/',mainapp_views.enyc,name='enyc'),
#workstation views
    path('index',workstationapp_views.workstation_index,name='workstation_index'),
    path('workstation-analysisreport',workstationapp_views.workstation_analysisreport,name='workstation_analysisreport'),
    path('workstation-dashboard',workstationapp_views.workstation_dashboard,name='workstation_dashboard'),
    path('workstation-dynamicanalysis',workstationapp_views.workstation_dynamicanalysis,name='workstation_dynamicanalysis'),
    path('workstation-staticanalysis',workstationapp_views.workstation_staticanalysis,name='workstation_staticanalysis'),
    path('markedassafe/<int:id>/',workstationapp_views.markedassafe,name='markedassafe'),
    path('markedasransomware/<int:id>/',workstationapp_views.markedasransomware,name='markedasransomware'),
    path('workstation-safefile',workstationapp_views.workstation_safefile,name='workstation_safefile'),
    path('workstation-ransomwarefile',workstationapp_views.workstation_ransomwarefile,name='workstation_ransomwarefile'),
    path('execute/<int:id>/',workstationapp_views.execute,name='execute'),

#usersapp views

   path('user-about-us',usersapp_views.users_about,name='users_about'),
   path('user-contact',usersapp_views.users_contact,name='users_contact'),
   path('user-dashboard',usersapp_views.users_dashboard,name='users_dashboard'),
   path('user-features',usersapp_views.users_features,name='users_features'),
   path('user-index',usersapp_views.users_index,name='users_index'),
   path('user-myfile',usersapp_views.users_myfile,name='users_myfile'),
   path('user-myprofile',usersapp_views.users_myprofile,name='users_myprofile'),
   path('user-portfolio',usersapp_views.users_portfolio,name='users_portfolio'),
   path('user-pricing',usersapp_views.users_pricing,name='users_pricing'),
   path('user-services',usersapp_views.users_services,name='users_services'),
   path('user-testimonials',usersapp_views.users_testimonials,name='users_testimonials'),
   path('user-uploaddata',usersapp_views.users_uploaddata,name='users_uploaddata'),

   



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


