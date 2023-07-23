# Generated by Django 4.2.1 on 2023-05-31 23:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0024_alter_comment_date_alter_friend_since_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 31, 18, 57, 8, 544722)
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
        ),
        migrations.AlterField(
            model_name="friend",
            name="since",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 31, 18, 57, 8, 544722)
            ),
        ),
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 31, 18, 57, 8, 544722)
            ),
        ),
    ]
