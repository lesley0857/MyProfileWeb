from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=150, blank=False)
    mobile = models.PositiveIntegerField(blank=False, null=True)
    github = models.CharField(max_length=100, blank=False,null=True)
    instagram = models.CharField(max_length=100, blank=False,null=True)
    facebook = models.CharField(max_length=100, blank=False,null=True)
    linkedin = models.CharField(max_length=100, blank=False,null=True)
    twitter = models.CharField(max_length=100, blank=False,null=True)
    location = models.TextField(max_length=100, blank=False,null=True)
    file = models.FileField(upload_to='images', null=True, blank=True)
    herofile = models.FileField(upload_to='images', null=True, blank=True)
    university = models.CharField(max_length=300, blank=False,null=True)
    discipline = models.CharField(max_length=300, blank=False,null=True)
    high_school = models.CharField(max_length=300, blank=False,null=True)


    def __str__(self):
        return f'{self.name}'
    
class Technologies(models.Model):
    name = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='technologies')
    description = models.TextField(max_length=100, blank=False)
    level = models.TextField(max_length=3, blank=False, null=True)
    file = models.TextField(max_length=15000, blank=False,null=True)

    def __str__(self):
        return f'{self.name}'
    
class Services(models.Model):
    name = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='services')
    level = models.TextField(max_length=3, blank=False, null=True)

    def __str__(self):
        return f'{self.name}'
    
class Projects(models.Model):
    name = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='projects')
    description = models.TextField(max_length=400, blank=False)
    project_link = models.CharField(max_length=150, blank=False,null=True)
    website_link = models.CharField(max_length=150, blank=True,null=True)
    file = models.CharField(max_length=150, blank=False,null=True)

    def __str__(self):
        return f'{self.name}'
    
class Clients(models.Model):
    RATING = (('1', '1'), ('2',
              '2'), ('3', '3'), ('4', '4'), ('5', '5'),)
    name = models.CharField(max_length=150, blank=False)
    seller_profile = models.ManyToManyField(
        Profile, blank=True, related_name='clients')
    description = models.TextField(max_length=100, blank=False)
    rating = models.CharField(max_length=1, choices=RATING,default='RATING[2]',blank=False, null=True,)
    role = models.CharField(max_length=150, blank=False,null=True)
    file = models.FileField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'