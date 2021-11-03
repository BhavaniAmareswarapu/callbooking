from django.db import models
from webapp.models import advisor
class Booking(models.Model):
    bookedfor = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    firstname= advisor.firstname
    adv_id= advisor.adv_id
    pic= advisor.profile_pic
    def __str__(self):
        return self.firstname
        return self.adv_id
        return self.pic
        return self.created_at
        return self.bookedfor
