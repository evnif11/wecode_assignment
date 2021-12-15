from django.db import models
class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        db_table = "actors"

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actor = models.ManyToManyField(Actor)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'movies'
