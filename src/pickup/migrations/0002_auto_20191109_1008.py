# Generated by Django 2.2.7 on 2019-11-09 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pickup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='arriveDate',
            new_name='Arrival_Date',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='handedTo',
            new_name='Handed_To',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='companyName',
            new_name='Item_Name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='pickDate',
            new_name='Recieved_kDate',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='rollNo',
            new_name='RollNo',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='itemnName',
            new_name='Shipper_Name',
        ),
    ]
