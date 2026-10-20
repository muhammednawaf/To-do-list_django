from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
