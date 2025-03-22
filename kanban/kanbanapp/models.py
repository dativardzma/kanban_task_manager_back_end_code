from django.db import models

# Create your models here.
class Table(models.Model):
    title = models.CharField(max_length=250)
    columns = models.JSONField(default=list)

    def __str__(self):
        return f'{self.title}, {self.columns}'
    

class SubTask(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    STATUS_CHOICES = [
        ('ready', 'Ready'),
        ('not ready', 'Not Ready')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Not Ready")

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    subtasks = models.ManyToManyField(SubTask)

    def __str__(self):
        return self.title