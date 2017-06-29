from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)