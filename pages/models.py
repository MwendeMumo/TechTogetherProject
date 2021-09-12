from django.db import models

class User(models.Model):
    Company_Name = models.CharField(max_length=200)
    Initial_Loan_Amount = models.FloatField()
    Initial_Interest_Rate = models.FloatField()
    Loan_Rate_After_Default = models.FloatField()
    Loan_Duration = models.FloatField()
    Final_Loan_Amount = models.FloatField()
    Overall_Rating = models.FloatField()

    def get_absolute_url(self):
        return u'/list/' 