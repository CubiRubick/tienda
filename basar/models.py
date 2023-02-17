from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)

class personalinfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=120, null=True, blank=True)
    lastname = models.CharField(max_length=120, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    borndate = models.DateField(null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    colony = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.firstname

    def __unicode__(self):
        return self.firstname

class productinfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    personalinfo = models.ForeignKey(personalinfo, related_name='perfonalinfo', on_delete=models.PROTECT, null=True, blank=True)
    nameproduct = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    units = models.IntegerField(null=True, blank=True)
    review = models.IntegerField(null=True, blank=True)
    image = models.ImageField(default=None, null=True, blank=True)
    in_existence = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.nameproduct

    def __unicode__(self):
        return self.nameproduct


