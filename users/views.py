from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    # Check if value the user input is valid or net
    if form.is_valid():
      # Save the user to the database
      form.save()

      username = form.cleaned_data.get('username')
      messages.success(request, f'Youre account has been created! You can now log in')
      # After customer register, redirect them to login page
      return redirect('login') 
  else:
    form = UserRegisterForm()
  context = {
    'form': form
  }

  return render(request, 'users/register.html', context)

@login_required # User needs to login before seeing their profile page
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,
    request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid:
      u_form.save()
      p_form.save()
      messages.success(request, f'Your account has been updated!')
      return redirect('profile')
         
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm()         

  context = {
    'u_form': u_form,
    'p_form': p_form,
  }
  return render(request, 'users/profile.html', context)
