from django.urls import path
from.import views


urlpatterns=[
path('', views.home,name='home'),

path('business', views.business,name='business'),
path( 'businesspage', views.businesspage,name=' businesspage'),
path('register', views.register,name='register'),

path('login', views.login, name='login'),

path('logout', views.logout, name='logout'),
path('businessdetailsupdate', views.businessdetailsupdate, name='businessdetailsupdate'),
path('update', views.update,name='update'),
path('updatestatus', views.updatestatus,name='updatestatus'),
]