# Generated by Django 4.1.6 on 2023-02-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createproduct',
            name='producttype',
            field=models.CharField(choices=[('oyoq kiyim', 'oyoq kiyim'), ('shim', 'shim'), ("ko'ylak", "ko'ylak"), ('futbolka', 'futbolka'), ('kamar', 'kamar')], default='nomalum', max_length=200),
        ),
    ]
