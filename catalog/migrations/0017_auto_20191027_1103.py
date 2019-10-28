# Generated by Django 2.2.6 on 2019-10-27 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_relationorganisationorganisation_relationorganisationorganisationtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for the work', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EntityWorkAliasType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A work alias type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EntityWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for a work type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelationShowWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the show - work relation type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelationShowWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(blank=True, help_text='If show was credited differently', max_length=200, null=True)),
                ('work_name', models.CharField(blank=True, help_text='If work was credited differently', max_length=200, null=True)),
                ('begin_date', models.DateField(blank=True, help_text='When did the relation start?', null=True)),
                ('end_date', models.DateField(blank=True, help_text='When did the relation end?', null=True)),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.RelationShowWorkType')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityShow')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityWork')),
            ],
        ),
        migrations.CreateModel(
            name='EntityWorkAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an alias for the work', max_length=200)),
                ('alias_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityWorkAliasType')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.EntityWork')),
            ],
        ),
        migrations.AddField(
            model_name='entitywork',
            name='work_types',
            field=models.ManyToManyField(blank=True, to='catalog.EntityWorkType'),
        ),
    ]
