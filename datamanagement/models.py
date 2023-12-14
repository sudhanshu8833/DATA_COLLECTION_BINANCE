from django.db import models
from django.db.models.fields import DateField, IntegerField
from django.contrib.auth.models import User
# Create your models here.






class strategy(models.Model):
    username=models.CharField(max_length=10,default="NONE")
    angel_api_keys=models.CharField(max_length=100,default='NONE')
    angel_client_id=models.CharField(max_length=10,default='NONE')
    angel_password=models.CharField(max_length=100,default='NONE')
    angel_token=models.CharField(max_length=100,default='NONE')

    lots=models.IntegerField(default=1)
    paper=models.BooleanField(default=False)
    bot=models.BooleanField(default=True)
    weekly_expiry=models.CharField(default="NONE",max_length=10)
    monthly_expiry=models.CharField(default="NONE",max_length=10)
    bots_started=models.IntegerField(default=0)
    shift_position=models.CharField(default="on",max_length=10)
    squareoff_request=models.CharField(default="nothing",max_length=10)


