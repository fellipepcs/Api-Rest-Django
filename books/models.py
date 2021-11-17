from uuid import uuid4
from datetime import datetime

from django.db import models


class Books(models.Model):
    idbook = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now=True)
    estadoLivro = models.CharField(max_length=50)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    dataDeCriação = models.DateTimeField()
