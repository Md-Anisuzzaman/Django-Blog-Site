from django.shortcuts import render, redirect
from .models import BlogPost, Bookmark
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Bookmark
from blog.forms import BlogForm, BlogFeedbackForm
from account.models import Account
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test


def is_admin(user):
    return user.role == 'admin'

@user_passes_test(is_admin)
def allBlogs(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'allblogs.html', context)


def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST,request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                # Check if the post should be published or unpublished
                if 'Published' in request.POST:
                    blog_post.publish('Published')  # Publish the post
                else:
                    blog_post.publish('Unpublished')  # Unpublish the post
                return redirect('home')
        else:
            form = BlogForm()
    else:
        return redirect('login')
    return render(request, 'createblog.html', {'form': form})


def blog_edit(request, id):
    blog = get_object_or_404(BlogPost, pk=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'editblog.html', {'form': form})


def delete_blog(request, id):
    blog = get_object_or_404(BlogPost, pk=id).delete()
    return redirect('home')


def single_user_blog(request):
    user = request.user
    blogs = BlogPost.objects.filter(author=user)
    return render(request, 'userblog.html', {'blogs': blogs})


# def blog_details(request, id):
#     blog = get_object_or_404(BlogPost, pk=id)
#     return render(request, 'blogdetails.html', {'blog': blog})


def blog_details(request, id):
    blog = get_object_or_404(BlogPost, pk=id)

    if request.method == 'POST':
        feedback_form = BlogFeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.blog = blog
            feedback.user = request.user
            feedback.save()
            # Redirect back to the same page
            return redirect('details', id=id)

    else:
        feedback_form = BlogFeedbackForm()

    context = {
        'blog': blog,
        'feedback_form': feedback_form,
    }

    return render(request, 'blogdetails.html', context)


def add_bookmark(request, blog_id):
    if request.user.is_authenticated:
        blog = BlogPost.objects.get(pk=blog_id)
        bookmark, created = Bookmark.objects.get_or_create(
            user=request.user, blog=blog)
        if created:
            messages.success(request, "Blog bookmarked successfully.")
            return redirect('bookmark_list')
        else:
            messages.info(request, "You have already bookmarked this blog.")
    else:
        messages.warning(request, "You must be logged in to bookmark a blog.")
    return redirect('details', id=blog_id)


def bookmark_list(request):
    if request.user.is_authenticated:
        bookmarks = Bookmark.objects.filter(user=request.user)
        return render(request, 'bookmark.html', {'bookmarks': bookmarks})
    else:
        messages.warning(
            request, "You must be logged in to view your bookmarks.")
        # Redirect to the login page or handle as needed
        return redirect('login')
    

def remove_bookmark(request, id):
    if request.user.is_authenticated:
        try:
            blog = BlogPost.objects.get(pk=id)
            bookmark = Bookmark.objects.get(user=request.user, blog=blog)
            bookmark.delete()
            messages.success(request, "Bookmark removed successfully.")
            return redirect('bookmark_list', id=id)
        except (BlogPost.DoesNotExist, Bookmark.DoesNotExist):
            messages.warning(request, "Bookmark not found.")
    else:
        messages.warning(request, "You must be logged in to remove a bookmark.")
    return redirect('details', id=id)