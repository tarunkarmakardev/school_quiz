# Generated by Django 3.1.5 on 2021-01-08 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0007_auto_20210108_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizscore',
            name='time_taken',
        ),
        migrations.CreateModel(
            name='student_attempts_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_taken', models.CharField(max_length=100, verbose_name='Time Taken to complete the test')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]