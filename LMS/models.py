from django.db import models
from . import calculations
# Create your models here.
class borrowers(models.Model):
    #customer_id=models.UUIDField()
    
    prefix=models.CharField(max_length=3)
    name=models.CharField(max_length=100)
    principal_amt=models.IntegerField()
    date_of_borrowing=models.DateField()
    duration=models.IntegerField()
    int_rate=models.DecimalField(decimal_places=2,max_digits=4)
    paid_amt=models.IntegerField()
    

    def emi(self):
        eo=calculations.emi_cal(self.principal_amt,self.int_rate,self.duration)
        return eo

    def remains(self):
        bal=calculations.balance_remain(self.date_of_borrowing,self.emi(),self.paid_amt,self.duration)
        return bal

  
    
   


