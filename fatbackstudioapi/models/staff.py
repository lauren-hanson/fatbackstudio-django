from django.db import models

class Staff(models.Model):
    startDate = models.DateField(max_length=55)
    userId = models.ForeignKey("User", on_delete=models.CASCADE)
    titleId = models.ForeignKey("Title", on_delete=models.CASCADE)
    imageUrl = models.CharField(max_length=55)
