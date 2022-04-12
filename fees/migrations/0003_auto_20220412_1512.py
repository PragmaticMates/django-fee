# Generated by Django 3.1.14 on 2022-04-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0002_auto_20220404_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricing',
            options={'ordering': ['price'], 'verbose_name': 'pricing', 'verbose_name_plural': 'pricings'},
        ),
        migrations.AlterModelOptions(
            name='quota',
            options={'ordering': ('order',), 'verbose_name': 'Quota', 'verbose_name_plural': 'Quotas'},
        ),
        migrations.AddField(
            model_name='quota',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, help_text='to set order in pricing', verbose_name='ordering'),
        ),
        migrations.AlterUniqueTogether(
            name='pricing',
            unique_together={('package', 'period')},
        ),
    ]