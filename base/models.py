from django.db import models

# Create your models here.
class Project(models.Model):
    languages = (
        ('Python', 'Python'),
        ('Js', 'Javascript'),
        ('C#', 'C#'),
        ('Java', 'Java'),
    )
    
    Name = models.CharField(max_length=250)
    firstCommit= models.DateField()
    lastCommit= models.DateField()
    mainStack = models.CharField(max_length=6, choices=languages)
    description = models.CharField(max_length=500)
    details = models.TextField(default="None")
    bannerImg = models.URLField()
    github = models.URLField()
     
    def __str__(self):
        return self.name