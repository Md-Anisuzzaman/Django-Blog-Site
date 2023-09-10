from django.contrib import admin
from .models import BlogPost
from .models import BlogFeedback, Bookmark


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categories', 'status',
                    'created_date', 'modified_date', 'published_date')
    list_display_links = ('title',)


class BlogFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'rating', 'review')


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'timestamp')


admin.site.register(BlogPost, BlogsAdmin)
admin.site.register(BlogFeedback, BlogFeedbackAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
