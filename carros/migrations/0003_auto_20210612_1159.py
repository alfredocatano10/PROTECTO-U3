# Generated by Django 3.1.7 on 2021-06-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0002_auto_20210612_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aceites',
            name='imagen',
            field=models.ImageField(default='', upload_to='imagen'),
        ),
        migrations.AlterField(
            model_name='baterias',
            name='imagen',
            field=models.ImageField(default='', upload_to='imagen'),
        ),
        migrations.AlterField(
            model_name='filtros',
            name='imagen',
            field=models.ImageField(default='', upload_to='imagen'),
        ),
    ]
