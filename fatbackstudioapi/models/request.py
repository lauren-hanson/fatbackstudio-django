from django.db import models

class Request(models.Model):
    clientId = models.ForeignKey("Client", on_delete=models.CASCADE)
    genreId = models.ForeignKey("Genre", on_delete=models.CASCADE)
    startDate = models.DateField(max_length=55)
    endDate = models.DateField(max_length=55)
    numOfSongs = models.CharField(max_length=55)
    musicianRequest = models.BooleanField()
    photoRequest = models.BooleanField()
    videoRequest = models.BooleanField()
    dateCompleted = models.DateField()
 
