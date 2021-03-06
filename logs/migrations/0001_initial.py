# Generated by Django 2.2.4 on 2020-07-17 20:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('level', models.CharField(blank=True, choices=[('critical', 'critical'), ('debug', 'debug'), ('error', 'error'), ('warning', 'warning'), ('information', 'info')], max_length=20)),
                ('event', models.IntegerField(blank=True)),
                ('origin', models.GenericIPAddressField(null=True, validators=[django.core.validators.validate_ipv4_address])),
                ('archived', models.BooleanField(default=False)),
                ('ambient', models.CharField(blank=True, choices=[('production', 'Produção'), ('homologation', 'Homologação'), ('dev', 'dev')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
