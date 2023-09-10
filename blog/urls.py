from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.allBlogs, name="allblogs"),
    path('userblog/', views.single_user_blog, name="userblog"),
    path('create', views.create_blog, name="create"),
    path('edit/<int:id>/', views.blog_edit, name="edit_blog"),
    path('delete/<int:id>/', views.delete_blog, name="delete_blog"),
    path('details/<int:id>/', views.blog_details, name="details"),
    path('details/<int:blog_id>/add-bookmark/', views.add_bookmark, name="add_bookmark"),
    path('details/<int:id>/remove-bookmark/', views.remove_bookmark, name="remove_bookmark"),
    path('bookmarks/', views.bookmark_list, name="bookmark_list"),
  
]
#   path('bookmark/<int:id>/', views.add_bookmark, name="bookmark"),