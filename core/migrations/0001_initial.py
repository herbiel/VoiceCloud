# Generated by Django 4.2.2 on 2023-06-17 17:07

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='名称')),
                ('gateway', models.CharField(default='', max_length=50, verbose_name='网关')),
                ('expression', models.TextField(default='', max_length=20, verbose_name='匹配条件')),
                ('domain', models.CharField(default='', max_length=20, verbose_name='域名')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
            ],
            options={
                'verbose_name': '路由',
                'verbose_name_plural': '路由',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=20, verbose_name='域名')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
            ],
            options={
                'verbose_name': '域名',
                'verbose_name_plural': '域名',
            },
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=20, verbose_name='分机号码')),
                ('password', models.CharField(default='', max_length=20, verbose_name='密码')),
                ('displayname', models.CharField(default='', max_length=20, verbose_name='显示名字')),
                ('domain', models.CharField(default='', max_length=20, verbose_name='域名')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
            ],
            options={
                'verbose_name': '分机',
                'verbose_name_plural': '分机',
            },
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='名称')),
                ('username', models.CharField(default='', max_length=20, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=20, verbose_name='密码')),
                ('realm', models.CharField(default='', max_length=20, verbose_name='认证地址')),
                ('proxy', models.CharField(default='', max_length=20, verbose_name='认证代理')),
                ('domain', models.CharField(default='', max_length=20, verbose_name='域名')),
                ('register', models.BooleanField(default=False, verbose_name='是否注册')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
            ],
            options={
                'verbose_name': '网关',
                'verbose_name_plural': '网关',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('domain', models.CharField(default='', max_length=200, verbose_name='域名')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]