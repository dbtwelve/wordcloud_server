# Generated by Django 4.0.dev20210427084335 on 2021-05-01 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcloudAPI', '0005_imageupload_wcimageurl_alter_imageupload_createdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='createDate',
            field=models.DateField(default=datetime.datetime(2021, 5, 1, 13, 27, 26, 929277)),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='updateDate',
            field=models.DateField(default=datetime.datetime(2021, 5, 1, 13, 27, 26, 929312)),
        ),
    ]
