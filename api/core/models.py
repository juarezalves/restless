from django.db import models

# Create your models here.

class Produto(models.Model):

    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
