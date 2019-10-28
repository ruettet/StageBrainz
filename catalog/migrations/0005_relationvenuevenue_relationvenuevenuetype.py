# Generated by Django 2.2.6 on 2019-10-26 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_relationshoworganisation_relationshoworganisationtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationVenueVenueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the show - show relation type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelationVenueVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_a_name', models.CharField(blank=True, help_text='If first venue was credited differently', max_length=200, null=True)),
                ('venue_b_name', models.CharField(blank=True, help_text='If second venue was credited differently', max_length=200, null=True)),
                ('begin_date', models.DateField(blank=True, help_text='When did the relation start?', null=True)),
                ('end_date', models.DateField(blank=True, help_text='When did the relation end?', null=True)),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.RelationVenueVenueType')),
                ('venue_a', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relationvenuevenue_venue_a', to='catalog.EntityShow')),
                ('venue_b', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relationvenuevenue_venue_b', to='catalog.EntityShow')),
            ],
        ),
    ]
