# Generated by Django 5.1.6 on 2025-04-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
