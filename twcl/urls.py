from  django.urls import path
from . import views

app_name='twcl'
urlpatterns = [
  path('signup/', views.signup_view, name='signup'),
  path('', views.show_home_view, name='home')
]
