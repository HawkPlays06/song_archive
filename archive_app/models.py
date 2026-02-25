from django.db import models

# Create your models here.
class account(models.Model):
    account_ID = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=255, null=False)
    e_mail = models.EmailField(max_length=255, null=False)
    DOB = models.DateField(null=False)
    date_of_creation = models.DateField(auto_now_add=True)