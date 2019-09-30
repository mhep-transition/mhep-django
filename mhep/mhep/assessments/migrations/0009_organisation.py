# Generated by Django 2.2.4 on 2019-09-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0008_assessment_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]