# Generated by Django 2.2.6 on 2019-10-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20191027_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationShowCharacterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the show - character relation type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelationShowCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(blank=True, help_text='If show was credited differently', max_length=200, null=True)),
                ('character_name', models.CharField(blank=True, help_text='If character was credited differently', max_length=200, null=True)),
                ('begin_date', models.DateField(blank=True, help_text='When did the relation start?', null=True)),
                ('end_date', models.DateField(blank=True, help_text='When did the relation end?', null=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityCharacter')),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.RelationShowCharacterType')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityShow')),
            ],
        ),
    ]
