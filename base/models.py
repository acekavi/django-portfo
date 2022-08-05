from django.db import models
import uuid

# Create your models here.
# class Project(models.Model):
#     languages = (
#         ('Python', 'Python'),
#         ('Js', 'Javascript'),
#         ('C#', 'C#'),
#         ('Java', 'Java'),
#     )
    
#     name = models.CharField(max_length=100)
#     lastCommit= models.DateField()
#     mainStack = models.CharField(max_length=6, choices=languages)
#     description = models.CharField(max_length=250)
#     details = models.TextField(default="None")
#     bannerImg = models.URLField()
#     github = models.URLField()
     
#     def __str__(self):
#         return self.name


class Design(models.Model):
    # tools = (
    #     ('AI', 'Illustrator'),
    #     ('PS', 'Photoshop'),
    #     ('Fi', 'Figma'),
    #     ('xD', 'Adobe xD'),
    #     ('Un', 'Unity'),
    # )

    artType = (
        ('Logo', 'Logo'),
        ('Vector', 'Vector'),
        ('User Interface', 'User Interface'),
        ('Product Design', 'Product'),
        ('Manipulation', 'Manipulation'),
    )
    
    id = models.UUIDField (primary_key = True ,default = uuid.uuid4, editable = False )
    name = models.CharField(max_length=250)
    behance = models.URLField( null=True )
    toolsUsed = models.CharField(default="AI,PS", max_length=20, verbose_name="AI,PS,Fi,xD,Un")
    artworkType = models.CharField(max_length=15, choices=artType)
    bannerImg = models.URLField()

    def __str__(self):
        return self.name