from django.db import models
import random


class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                self.id = random.randint(1000, 99999)
                if not Category.objects.filter(id=self.id).exists():
                    break
        super().save(*args, **kwargs)
