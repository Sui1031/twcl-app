from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == 'POST':
    Form = UserCreationForm(request.POST)
    if Form.is_valid():
      Form.save()

      return redirect('twcl:home')
  else:
    Form = UserCreationForm()

  return render(request, 'twcl/signup.html', {'form': Form})

def showHome(request):
  return render(request, 'twcl/home.html')
