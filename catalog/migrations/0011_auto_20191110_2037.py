# Generated by Django 2.2.6 on 2019-11-10 19:37

from django.db import migrations
import partial_date.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20191110_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='entityproduction',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='entityproduction',
            name='start_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
    ]