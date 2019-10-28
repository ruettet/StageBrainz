# Generated by Django 2.2.6 on 2019-10-27 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0036_relationorganisationwork_relationorganisationworktype'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationOrganisationCharacterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the organisation - character relation type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelationOrganisationCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(blank=True, help_text='If organisation was credited differently', max_length=200, null=True)),
                ('character_name', models.CharField(blank=True, help_text='If character was credited differently', max_length=200, null=True)),
                ('begin_date', models.DateField(blank=True, help_text='When did the relation start?', null=True)),
                ('end_date', models.DateField(blank=True, help_text='When did the relation end?', null=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityCharacter')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityOrganisation')),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.RelationOrganisationCharacterType')),
            ],
        ),
    ]
