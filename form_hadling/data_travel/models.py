from django.db import models

# Create your models here.

class D_travel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
