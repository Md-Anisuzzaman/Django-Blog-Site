from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from category.models import Category
from django.utils import timezone
from django.conf import settings
from account.models import Account
import random


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True, null=False,
                          blank=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=99999)
    status_choices = (
        ('Published', 'Published'),
        ('Unpublished', 'Unpublished'),
    )
    status = models.CharField(max_length=20, choices=status_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    # Define the upload path
    image = models.ImageField(
        upload_to='photos/blogPhoto', null=True, blank=True)

    def publish(self, status=None):
        if self.status == 'Published':
            self.published_date = timezone.now()
        elif self.status == 'Unpublished':
            self.published_date = None
        self.save()

    def __str__(self):
        return self.title

    def calculate_average_rating(self):
        total_feedback = self.feedback.all().count()
        if total_feedback > 0:
            sum_ratings = sum(
                [feedback.rating for feedback in self.feedback.all()])
            return sum_ratings / total_feedback
        else:
            return 0


class BlogFeedback(models.Model):
    blog = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='feedback')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, message=_("Rating must be 0 or higher.")),
            MaxValueValidator(6, message=_("Rating must be 6 or lower."))
        ])
    review = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s feedback on {self.blog.title}"

class Bookmark(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s bookmark of {self.blog.title}"