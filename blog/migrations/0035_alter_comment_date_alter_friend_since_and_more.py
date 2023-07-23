# Generated by Django 4.2.1 on 2023-06-02 02:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0034_alter_comment_date_alter_friend_since_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 1, 21, 17, 1, 610626)
            ),
        ),
        migrations.AlterField(
            model_name="friend",
            name="since",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 1, 21, 17, 1, 610626)
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 1, 21, 17, 1, 610626)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 1, 21, 17, 1, 610626)
            ),
        ),
        migrations.CreateModel(
            name="FriendRequest",
            fields=[
                ("key", models.AutoField(primary_key=True, serialize=False)),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 6, 1, 21, 17, 1, 612132)
                    ),
                ),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
