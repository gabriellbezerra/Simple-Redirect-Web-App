from django.db import models

# Create your models here.
class LINK(models.Model):
    encurtado_url = models.CharField(primary_key=True, max_length=20)
    original_url = models.CharField(max_length=100)