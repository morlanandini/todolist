from django.db import models

# Create your models here.
class user_registration(models.Model):
    user_name=models.CharField(max_length=10,unique=True)
    user_email=models.EmailField(max_length=30,unique=True)
    user_password=models.CharField(max_length=30)

    def __str__(self):
        return self.user_name

class todolist_info(models.Model):
    user_obj=models.ForeignKey(to=user_registration,on_delete=models.CASCADE)
    date_event = models.CharField(max_length=11)
    event_name=models.CharField(max_length=30)
    event_description=models.CharField(max_length=300)
