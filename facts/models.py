from django.db import models


class CatFact(models.Model):
    text = models.TextField()
    image_url = models.TextField()
