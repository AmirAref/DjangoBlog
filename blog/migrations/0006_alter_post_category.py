# Generated by Django 3.2.12 on 2022-06-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
