# Generated by Django 4.2.1 on 2023-10-09 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appfierros', '0015_alter_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_added',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(auto_now_add=True, default='17:51:17'),
            preserve_default=False,
        ),
    ]
