# Generated by Django 3.1.12 on 2021-07-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiraticketing', '0002_jirasetting_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='jirasetting',
            name='setting_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
