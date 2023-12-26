# Generated by Django 3.2.16 on 2023-11-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_template', '0002_alter_subjecttemplategroup_expired_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjecttemplate',
            name='readonly',
            field=models.BooleanField(default=False, verbose_name='只读标识'),
        ),
        migrations.AddField(
            model_name='subjecttemplate',
            name='source_group_id',
            field=models.IntegerField(default=0, verbose_name='来源用户组ID'),
        ),
    ]
