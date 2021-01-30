from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    content = models.CharField(max_length=150)
    date_posted = models.DateTimeField()
    completed = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

