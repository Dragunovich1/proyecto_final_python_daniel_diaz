# Generated by Django 4.2.5 on 2023-09-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfierros', '0004_post_post_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='ford', max_length=255),
        ),
    ]