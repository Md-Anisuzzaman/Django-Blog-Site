
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from .models import RegistrationModel
from django.contrib.auth.hashers import check_password


def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = RegistrationModel.objects.get(email=email)
        if check_password(password, user.password):
            login(request,user)
            return redirect('home')
        else:
            error_message = "Invalid email or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = RegistrationModel.objects.get(email=email)
#         except RegistrationModel.DoesNotExist:
#             error_message = "Invalid email or password. Please try again."
#             return render(request, 'login.html', {'error_message': error_message})

#         if check_password(password, user.password):
#             login(request, user)  # Log the user in
#             return redirect('home')
#         else:
#             error_message = "Invalid email or password. Please try again."
#             return render(request, 'login.html', {'error_message': error_message})
#     else:
#         return render(request, 'login.html')
