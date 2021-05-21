# Generated by Django 3.2.3 on 2021-05-20 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_name_item_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='club',
        ),
        migrations.AddField(
            model_name='item',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.club'),
        ),
    ]