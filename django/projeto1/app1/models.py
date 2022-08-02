from django.db import models

# Create your models here.
class login_senha(models.Model):
    username=models.CharField(max_length=30)
    password=models.DecimalField(decimal_places=0, max_digits=8)

    def __str__(self):
        return self.username
