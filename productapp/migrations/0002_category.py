# Generated by Django 4.1.7 on 2023-03-11 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.brand')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
