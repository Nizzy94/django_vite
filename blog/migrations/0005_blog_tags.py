# Generated by Django 4.0.1 on 2022-01-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_alter_blog_body_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='blogs', to='blog.Tag'),
        ),
    ]
