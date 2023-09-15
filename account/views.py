from django.shortcuts import render, redirect
from .forms import RegistrationForm
from account.models import Account
from blog.models import BlogPost, BlogFeedback, Bookmark
from category.models import Category
from django.contrib import messages, auth
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            password = form.cleaned_data['password']
            # username = email.split('@')[0]
            user = Account.objects.create_user(
                email=email, username=username, password=password, role=role)
            auth.login(request, user)
            user.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Authenticate the user
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                # If 'next' is not provided, redirect to a default route
                return redirect('home')  # Repl
        else:
            messages.error(
                request, 'Invalid login credentials. Please try again.')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)  # Log the user out
    return redirect('home')


def user_profile(request):
    user = request.user
    blogs = BlogPost.objects.filter(author=user)
    context = {
        'user': user,
        'blogs': blogs
    }
    return render(request, 'userProfile.html', context)


def dashboard(request):
    totalBlogs = BlogPost.objects.count()
    totalBlogFeedback = BlogFeedback.objects.count()
    totalUser = Account.objects.count()
    totalBookMarks = Bookmark.objects.count()
    totalCategory = Category.objects.count()
    user = request.user
    myBlogs = BlogPost.objects.filter(author=user).count()

    context = {
        "totalBlogs": totalBlogs,
        "totalBlogFeedback": totalBlogFeedback,
        "totalUser": totalUser,
        "totalBookMarks": totalBookMarks,
        "totalCategory": totalCategory,
        "myBlogs": myBlogs,
    }

    return render(request, 'dashboard.html', context)
