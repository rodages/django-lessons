from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField(default=None)
    worth_a_watch = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"
