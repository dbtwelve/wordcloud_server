# Generated by Django 3.2 on 2021-05-03 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcloudAPI', '0011_remove_wordcloud_image_alter_imageupload_createdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='createDate',
            field=models.DateField(default=datetime.datetime(2021, 5, 3, 15, 39, 7, 969463)),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='updateDate',
            field=models.DateField(default=datetime.datetime(2021, 5, 3, 15, 39, 7, 969496)),
        ),
    ]
