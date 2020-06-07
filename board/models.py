from django.db import models


# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField