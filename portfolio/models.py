from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Service(models.Model):
    icon = models.ImageField(upload_to='media/service')
    name= models.CharField(max_length=200,blank=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name= models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Portfolio(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200,null=True)
    photo = models.ImageField(upload_to='media/portfolio',null=True)
    video_url = models.CharField(max_length=200)
    url = models.URLField()
    body = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=200)
    Job = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/clients')
    body = models.TextField()

    def __str__(self):
        return self.name


class MyProject(models.Model):
    compled = models.CharField(max_length=200)
    happy = models.CharField(max_length=200)
    perspective = models.CharField(max_length=200)



class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    ids = models.CharField(max_length=200,null=True,blank=True)
    job = models.CharField(max_length=200)

    gmail = models.EmailField(max_length=200,null=True,blank=True)
    insta = models.URLField(max_length=200,null=True,blank=True)
    telegram = models.URLField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='media/team')

    def __str__(self):
        return self.name




class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    text = models.TextField()



class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/blog')
    tags = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    logo = models.ImageField(upload_to='media/sponsor')

    def __str__(self):
        return self.name





