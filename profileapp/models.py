from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=150, blank=False)
    mobile = models.PositiveIntegerField(blank=False, null=True)
    github = models.CharField(max_length=100, blank=False)
    instagram = models.CharField(max_length=100, blank=False)
    facebook = models.CharField(max_length=100, blank=False)
    twitter = models.CharField(max_length=100, blank=False)
    location = models.TextField(max_length=100, blank=False)
    file = models.FileField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    
class Technologies(models.Model):
    name = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='technologies')
    description = models.TextField(max_length=100, blank=False)
    level = models.TextField(max_length=3, blank=False, null=True)
    file = models.CharField(max_length=1500, blank=False,null=True)

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
    description = models.TextField(max_length=100, blank=False)
    project_link = models.CharField(max_length=150, blank=False,null=True)
    website_link = models.CharField(max_length=150, blank=True,null=True)
    file = models.CharField(max_length=150, blank=False,null=True)

    def __str__(self):
        return f'{self.name}'