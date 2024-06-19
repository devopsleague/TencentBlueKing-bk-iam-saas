# Generated by Django 3.2.16 on 2024-04-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminapiallowlistconfig',
            name='api',
            field=models.CharField(choices=[('system_list', '获取系统列表'), ('group_list', '获取用户组列表'), ('group_batch_create', '批量创建用户组'), ('group_update', '更新用户组'), ('group_delete', '删除用户组'), ('group_member_list', '获取用户组成员列表'), ('subject_joined_group_list', '获取Subject加入的用户组列表'), ('subject_role_list', '获取Subject角色列表'), ('role_super_manager_member_list', '获取超级管理员成员列表'), ('role_system_manager_member_list', '获取系统管理员及成员列表'), ('audit_event_list', '获取审计事件列表'), ('subject_freeze_unfreeze', '冻结/解冻Subject'), ('subject_permission_cleanup', '权限清理'), ('subject_permission_exists', '权限是否存在')], help_text='*代表任意', max_length=32, verbose_name='API'),
        ),
    ]