# Generated by Django 3.1.5 on 2021-01-07 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createquiz',
            options={'verbose_name': 'Create a Quiz', 'verbose_name_plural': 'Create a Quiz'},
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name': 'Create Quiz questions', 'verbose_name_plural': 'Create Quiz questions'},
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='quiz',
        ),
    ]
