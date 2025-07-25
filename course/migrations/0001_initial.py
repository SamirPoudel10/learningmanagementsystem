# Generated by Django 5.2.4 on 2025-07-16 03:29

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name_plural': '2. Course Categories',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled', models.IntegerField(default=0)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('learning_outcomes', models.JSONField()),
                ('thumbnail', models.ImageField(upload_to='course_images/')),
                ('teacher', models.ManyToManyField(to='Student.teacher')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursecategory')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.rating')),
            ],
            options={
                'verbose_name_plural': '3. Course ',
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='LectureVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', cloudinary.models.CloudinaryField(max_length=255)),
                ('video_length', models.TimeField(default='00:00:00')),
                ('thumbnail', models.ImageField(upload_to='videos/thumbnail/')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='course.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='Student_enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('dropped', 'Dropped')], default='active', max_length=20)),
                ('grade', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='course.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
