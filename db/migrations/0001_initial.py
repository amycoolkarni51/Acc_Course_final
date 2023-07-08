# Generated by Django 4.1.2 on 2023-07-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('EmailId', models.EmailField(max_length=254)),
                ('Location', models.TextField(max_length=100)),
                ('Message', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Course_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_desc', models.CharField(max_length=1000)),
                ('syllabus_pdf', models.CharField(max_length=1000)),
                ('introduction_link', models.CharField(max_length=1000)),
                ('pdf_link', models.CharField(max_length=1000)),
                ('video_link', models.CharField(max_length=1000)),
                ('select_course', models.CharField(max_length=1000)),
                ('filename', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmailId', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=20)),
                ('EmailId', models.EmailField(max_length=254)),
                ('Mobile', models.BigIntegerField()),
                ('Gender', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=30)),
                ('Qualification', models.CharField(max_length=30)),
                ('Profession', models.CharField(max_length=30)),
                ('Courses', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'registeration',
            },
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=20)),
                ('EmailId', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
                ('Confirm_Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'signup',
            },
        ),
    ]