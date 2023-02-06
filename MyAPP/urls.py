from django.urls import path
from . import views


urlpatterns =[

    path('' , views.index, name = 'index'),
    path('register' , views.register, name = 'register'),
    path('login' , views.login, name = 'login'),
    path('logout' , views.logout, name = 'logout'),
    path('post/<str:pk>' , views.post, name = 'post'),
     path('IMS_ClockingView' , views.IMS_ClockingView, name = 'IMS_ClockingView'),
      path('IMS_EmpDashboard' , views.IMS_EmpDashboard, name = 'IMS_EmpDashboard'),
       path('IMS_EmpProfile' , views.IMS_EmpProfile, name = 'IMS_EmpProfile'),
        path('IMS_Landing' , views.IMS_Landing, name = 'IMS_Landing'),
         path('IMS_Login' , views.IMS_Login, name = 'IMS_Login'),
          path('IMS_Register' , views.IMS_Register, name = 'IMS_Register'),
  
]