
from django.db import models
from django.utils import timezone
# Create your models here.
# class LogMessage(models.Model):
#     message = models.CharField(max_length=300)


class LogMessage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    class_field = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged", default=timezone.now)
    
    
    def __str__(self):
        date = timezone.localtime(self.log_date)
        # return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
        return f"{self.log_date.strftime('%d %b %Y %H:%M:%S')} - {self.name} - {self.class_field} - {self.message} "



    id = models.AutoField(primary_key=True)  # Add this line for the primary key
