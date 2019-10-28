# Generated by Django 2.2.6 on 2019-10-27 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0039_relationorganisationurl_relationorganisationurltype'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationWorkWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the work - work relation type', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RelationWorkWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_a_name', models.CharField(blank=True, help_text='If first work was credited differently', max_length=200, null=True)),
                ('work_b_name', models.CharField(blank=True, help_text='If second work was credited differently', max_length=200, null=True)),
                ('begin_date', models.DateField(blank=True, help_text='When did the relation start?', null=True)),
                ('end_date', models.DateField(blank=True, help_text='When did the relation end?', null=True)),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.RelationWorkWorkType')),
                ('work_a', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relationworkwork_work_a', to='catalog.EntityWork')),
                ('work_b', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relationworkwork_work_b', to='catalog.EntityWork')),
            ],
        ),
    ]
