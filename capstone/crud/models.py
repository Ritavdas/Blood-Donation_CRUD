from django.db import models
import datetime
# Create your models here.


class Donors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=1000)
    zipcode = models.IntegerField()
    gender = models.CharField(max_length=10)
    group = models.CharField(max_length=20)
    weight = models.FloatField()
    fainting = models.BooleanField(default=False)
    bruise = models.BooleanField(default=False)
    vein = models.BooleanField(default=False)
    dob = models.DateField(default=datetime.date.today)
    total = models.BooleanField()
    pic = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        db_table = 'blood_donor'
