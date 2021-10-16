from django.db import models

class Blogger (models.Model):
    first_name = models.CharField(max_length=200, default='kkkk')
    last_name = models.TextField(max_length=500, default='kkkk')
    age = models.IntegerField(null=True)
    region = models.TextField(max_length=50, null=True)
    district = models.TextField(max_length=50, null=True)
    city = models.TextField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
