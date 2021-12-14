from django.db import models
from django.db.models.deletion import CASCADE

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "owners"


class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Meta:
        db_table = "dogs"
