from django.db import models

class Hunt(models.Model):
    name = models.CharField()


class Treasure(models.Model):
    name = models.CharField()
    description = models.CharField()
    point_value = models.IntegerField()
    limit = models.IntegerField(default=1)
    hunt = models.ForeignKey(Hunt, on_delete=models.CASCADE)