from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()

      return redirect('twcl:home')
  else:
    form = UserCreationForm()

  return render(request, 'twcl/signup.html', {'form': form})

def show_home_view(request):
  return render(request, 'twcl/home.html')
