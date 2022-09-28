from email.policy import default
from django.db import models

# Create your models here.
class PokemonData(models.Model):
   # date = models.DateTimeField(default="2022-15-20 12:00")
    json_data = models.JSONField()

    def __str__(self):
        return self.json_data


class Pokemon(models.Model):
    name = models.CharField(max_length=240, unique=True)
    url = models.CharField(max_length=240)
    image_url = models.CharField(max_length=240)

    def __str__(self):
        return self.name
