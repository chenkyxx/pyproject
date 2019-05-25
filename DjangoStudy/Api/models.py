from django.db import models

# Create your models here.


class IMG(models.Model):
    img = models.BinaryField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Test(models.Model):
    photo = models.BinaryField()

    class Meta:
        db_table = "test"



