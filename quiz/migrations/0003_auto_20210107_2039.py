# Generated by Django 3.1.5 on 2021-01-07 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210107_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateQuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='quesiton')),
                ('correct_answer', models.CharField(max_length=20, verbose_name='Correct answer')),
                ('incorrect_answers', models.CharField(max_length=20, verbose_name='Incorrect answers (comma seperated)')),
            ],
            options={
                'verbose_name': 'Create Quiz questions',
                'verbose_name_plural': 'Create Quiz questions',
            },
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
        migrations.RenameField(
            model_name='createquiz',
            old_name='quiz_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='createquiz',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='createquizquestion',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.createquiz'),
        ),
    ]
