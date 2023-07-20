# Generated by Django 4.2.2 on 2023-07-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='_class',
            new_name='student_class',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('P', 'PRESENT'), ('A', 'ABENT')], default='A', max_length=10, verbose_name='attendance status'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], default='F', max_length=1, verbose_name='gender of the student'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], default='F', max_length=10, verbose_name='gender of the teacher'),
        ),
    ]
