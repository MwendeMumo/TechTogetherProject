# Generated by Django 3.2.7 on 2021-09-12 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='FinalAmount',
            new_name='Final_Loan_Amount',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='InitialLoanAmount',
            new_name='Initial_Interest_Rate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='InterestRateAfterDefault',
            new_name='Initial_Loan_Amount',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='LoanRateAfterDefault',
            new_name='Loan_Duration',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='OverAllRating',
            new_name='Loan_Rate_After_Default',
        ),
        migrations.AddField(
            model_name='user',
            name='Overall_Rating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
