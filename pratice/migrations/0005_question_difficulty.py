# Generated by Django 4.2.7 on 2024-01-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratice', '0004_question_question_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], default='easy', max_length=200),
        ),
    ]
