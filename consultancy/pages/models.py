from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
class Uploaderform(models.Model):
    #TIMESTAMP_AS_ID = models.CharField(max_length=350)
    FIRSTNAME       = models.CharField(max_length=350)
    LASTNAME        = models.CharField(max_length=350)
    QUALIFICATION   = models.CharField(max_length=150)
    PHONENO          = models.CharField(max_length=150)
    EMAIL           = models.CharField(max_length=150)
    COUNTRY          = models.CharField(max_length=150)
    RESUMEUPLOAD     = models.CharField(max_length=150)

    #FILENAME        = models.CharField(max_length=150)
    #FILE            = SizedBinaryField(3)
    #STATUS          = models.CharField(default='SUBMITTED', max_length=15)
    #CLOSEDON        = models.DateTimeField(default=None,blank=True, null=True)

    #objects = UserManager()


class contactusform(models.Model):
    FIRSTNAME       = models.CharField(max_length=350)
    LASTNAME        = models.CharField(max_length=350)
    PHONENO         = models.CharField(max_length=150)
    EMAIL           = models.CharField(max_length=150)
    MESSAGE         =  models.CharField(max_length=150)



