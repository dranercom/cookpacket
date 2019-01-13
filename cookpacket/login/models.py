from django.db import models
# Create your models here.
class Login(models.Model):
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def authenticate(emai_id,password):
        self.save()
        return 
