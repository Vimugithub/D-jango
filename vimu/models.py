from django.db import models


# Create your models here.


class contact1(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=75)
    phone_No=models.CharField(max_length=13)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=255)


