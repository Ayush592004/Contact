from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=300)
    email = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return 'Message By ' + self.fname + ' ' + self.lname + ' - ' + self.email
    