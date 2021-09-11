from django.db import models

class User(models.Model):
    Company_Name = models.CharField(max_length=200)
    InterestRateAfterDefault = models.FloatField()
    InitialLoanAmount = models.FloatField()
    LoanRateAfterDefault = models.FloatField()
    OverAllRating = models.FloatField()
    FinalAmount = models.FloatField()
    