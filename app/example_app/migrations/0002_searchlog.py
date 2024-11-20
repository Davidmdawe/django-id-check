# Generated by Django 3.2.20 on 2024-11-19 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('id_check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.DateField(auto_now_add=True)),
                ('id_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_logs', to='id_check.idinfo')),
            ],
        ),
    ]
