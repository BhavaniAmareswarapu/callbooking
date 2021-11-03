from django.db import models

class advisor(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    adv_id=models.IntegerField()
    profile_pic=models.ImageField(null="True",blank="True")
    def __str__(self):
        return self.firstname