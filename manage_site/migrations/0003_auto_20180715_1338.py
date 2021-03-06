# Generated by Django 2.0.6 on 2018-07-15 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_site', '0002_indexcoremembers_indexcourse_indexhonorwall_indeximgshow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexcoremembers',
            options={'verbose_name': '核心成员展示', 'verbose_name_plural': '核心成员展示'},
        ),
        migrations.AlterModelOptions(
            name='indexhonorwall',
            options={'verbose_name': '荣誉墙', 'verbose_name_plural': '荣誉墙'},
        ),
        migrations.AlterField(
            model_name='indexcourse',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程名称'),
        ),
    ]
