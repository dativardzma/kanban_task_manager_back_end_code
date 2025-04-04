# Generated by Django 5.1.7 on 2025-03-19 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('chose', models.CharField(choices=[('todo', 'ToDo'), ('doing', 'Doing'), ('done', 'Done')], default='ToDo', max_length=50)),
                ('subtasks', models.ManyToManyField(to='kanbanapp.subtask')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanbanapp.table')),
            ],
        ),
    ]
