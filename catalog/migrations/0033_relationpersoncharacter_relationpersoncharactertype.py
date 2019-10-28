# Generated by Django 2.2.6 on 2019-10-27 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_relationpersonwork_relationpersonworktype'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationPersonCharacterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the person - character relation type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelationPersonCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(blank=True, help_text='If person was credited differently', max_length=200, null=True)),
                ('character_name', models.CharField(blank=True, help_text='If character was credited differently', max_length=200, null=True)),
                ('production_name', models.CharField(blank=True, help_text='When production is credited differently', max_length=200, null=True)),
                ('begin_date', models.DateField(blank=True, help_text='When did the relation start?', null=True)),
                ('end_date', models.DateField(blank=True, help_text='When did the relation end?', null=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityCharacter')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityPerson')),
                ('production', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityProduction')),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.RelationPersonCharacterType')),
            ],
        ),
    ]
