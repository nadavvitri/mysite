# Generated by Django 5.2.4 on 2025-07-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_slug_attachments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='file',
            field=models.FileField(upload_to='posts/attachments/'),
        ),
    ]
