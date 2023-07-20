from django.db import models

class Artist(models.Model):
    name= models.CharField(max_length=100 , unique=True)        
    genre= models.CharField(max_length=50)
    biography= models.TextField()

class Album(models.Model):
    title= models.CharField(max_length=100 , unique=True)
    artist= models.ForeignKey(Artist , on_delete= models.SET_NULL , null=True, related_name= 'albums')
    release_date= models.DateField()
    cover_image= models.ImageField(upload_to="images/")
    discription= models.TextField()


class Song(models.Model):
    title= models.CharField(max_length=100)
    album= models.ForeignKey(Album , on_delete= models.CASCADE , related_name= 'songs')
    duration= models.DurationField()
    track_number= models.IntegerField()
    lyrics= models.TextField(unique=True)
    class Meta:
        unique_together= ['album' , 'track_number']
        unique_together= ['album' , 'title']

        




        
