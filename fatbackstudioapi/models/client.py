from django.db import models

class Client(models.Model):
    phoneNumber = models.CharField(max_length=55)
    userId = models.ForeignKey("User", on_delete=models.CASCADE)
   
