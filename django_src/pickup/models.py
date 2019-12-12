from django.conf import settings
from django.db import models
from django.utils import timezone

class item(models.Model):
    RollNo    = models.CharField(max_length=30)
    Item_Name = models.CharField(max_length=200)
    Shipper_Name = models.CharField(max_length=200)
    Handed_To  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Arrival_Date = models.DateTimeField(default=timezone.now)
    Recieved_Date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.RollNo + " " + self.Item_Name

