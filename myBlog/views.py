from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home(request, cat_name=None):
    category = None
    blogs = None
    if cat_name:
        category = get_object_or_404(Category, name=cat_name)
        blogs = BlogPost.objects.filter(categories=category)
    else:
        blogs = BlogPost.objects.all()

    categories = Category.objects.all()

    context = {
        'blogs': blogs,
        'categories': categories
    }
    return render(request, 'home.html', context)


# def home_view(request):
#     searchTerm = request.GET.get('searchTerm','')
#     # blogs = BlogPost.objects.filter(title__icontains=searchTerm)

#     if searchTerm:
#         # Perform a case-insensitive search on the 'title' field
#         blog_posts = BlogPost.objects.filter(title__icontains=searchTerm)
#     else:
#         blog_posts = []
   
#     # Get the selected filter option from the request
#     filter_by = request.GET.get('filter_by')

#     # Category filtering
#     cat_name = request.GET.get('cat_name')
#     category = None

#     # Check if cat_name is provided and try to get the category
#     if cat_name:
#         category = get_object_or_404(Category, name=cat_name)

#     # Apply both filters based on user selection
#     if filter_by == 'Author':
#         # Check if the user's role is 'author'
#         if request.user.role == 'author':
#             blogs = BlogPost.objects.filter(author=request.user)
#         else:
#             # If the user's role is not 'author', show all blogs
#             blogs = BlogPost.objects.all()
#     elif filter_by == 'Date':
#         blogs = BlogPost.objects.order_by('-created_date')
#     else:
#         # No filter option selected, check if a category is selected
#         if category is not None:
#             blogs = BlogPost.objects.filter(categories=category)
#         else:
#             # If no category is selected and no filter is applied, show all blogs
#             blogs = BlogPost.objects.all()

#     categories = Category.objects.all()

#     context = {
#         'searchTerm': searchTerm,
#         'blog_posts':blog_posts,
#         'blogs': blogs,
#         'categories': categories,
#     }

#     return render(request, 'home.html', context)

def home_view(request):
    searchTerm = request.GET.get('searchTerm', '')
    blog_posts = BlogPost.objects.all()

    if searchTerm:
        blog_posts = blog_posts.filter(title__icontains=searchTerm)

    # Get the selected filter option from the request
    filter_by = request.GET.get('filter_by')

    # Category filtering
    cat_name = request.GET.get('cat_name')
    category = None

    if cat_name:
        category = get_object_or_404(Category, name=cat_name)

    if filter_by == 'Author':
        if request.user.role == 'author':
            blog_posts = blog_posts.filter(author=request.user)
    elif filter_by == 'Date':
        blog_posts = blog_posts.order_by('-created_date')
    elif category:
        blog_posts = blog_posts.filter(categories=category)

    # Set the number of blog posts per page (e.g., 2)
    per_page = 2

    # Create a Paginator instance
    paginator = Paginator(blog_posts, per_page)

    # Get the current page number from the request
    page = request.GET.get('page')

    try:
        # Get the blog posts for the current page
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results
        blogs = paginator.page(paginator.num_pages)

    categories = Category.objects.all()

    context = {
        'searchTerm': searchTerm,
        'blog_posts': blog_posts,
        'blogs': blogs,
        'categories': categories,
    }

    return render(request, 'home.html', context)
