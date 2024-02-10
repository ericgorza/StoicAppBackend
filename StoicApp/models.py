from django.db import models

# Create your models here.
class Filosofo(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Phrases(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    phrase = models.CharField(max_length=600)
    philosopher = models.ForeignKey(Filosofo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.philosopher.name} - {self.phrase}"

class Picture(models.Model):
    img_url = models.URLField()
    philosopher = models.ForeignKey(Filosofo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.philosopher} img'