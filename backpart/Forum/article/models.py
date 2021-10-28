from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    password = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.TextField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    author = models.TextField()
    assigned = models.IntegerField()

    def __str__(self):
        return self.body