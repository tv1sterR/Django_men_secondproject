# Generated by Django 4.2.1 on 2025-03-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0003_alter_men_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='men',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=1),
        ),
    ]
