# Generated by Django 5.0.2 on 2024-07-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_inq_contactno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inq',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]