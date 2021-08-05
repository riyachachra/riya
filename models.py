from django.db import connections
from django.db import models
 
class Users(models.Model):
    username = models.CharField(max_length = 30)
    userid = models.IntegerField(max_length= 8)
    userlocation = models.CharField(max_length=30) 

 class Meta:
    db_table = "user_details"   