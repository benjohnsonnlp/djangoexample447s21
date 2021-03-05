from django.db import models


class CatFact(models.model):
    text = models.TextField()
    image_url = models.TextField()
