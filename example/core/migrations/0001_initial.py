# Generated by Django 4.1.1 on 2022-12-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122)),
                ('lname', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('message', models.CharField(max_length=122)),
            ],
        ),
    ]
