
from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=250)
    balance = models.DecimalField(max_digits=19,decimal_places=6,default=0)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()
    login_streak = models.IntegerField(default=0)
    puzzle_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)



class Token(models.Model):
    ac_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token_count = models.IntegerField(default=0)
    puzzle_1 = models.IntegerField(default=0)
    puzzle_2 = models.IntegerField(default=0)
    puzzle_3 = models.IntegerField(default=0)
    puzzle_4 = models.IntegerField(default=0)
    puzzle_5 = models.IntegerField(default=0)

    def __str__(self):
        return str(self.ac_id)