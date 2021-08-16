from  django.urls import path
from . import views

app_name='twcl'
urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('/', views.showHome, name='home')
]