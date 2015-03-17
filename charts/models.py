from django.db import models


class Entry(models.Model):
    region = models.CharField(max_length=30, db_index=True)
    city = models.CharField(max_length=30, db_index=True)
    value = models.FloatField()

    @classmethod
    def create(cls, region, city, value):
        return cls(region=region, city=city, value=value)
