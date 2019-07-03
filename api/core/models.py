from django.db import models

# Create your models here.

class Produto(models.Model):
    cliente = models.IntegerField()
    descricao = models.CharField(max_length=50)
    

    def __str__(self):
        return descricao
