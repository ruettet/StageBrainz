# Generated by Django 2.2.6 on 2019-10-31 20:17

from django.db import migrations
import partial_date.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20191031_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entityorganity',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='entityorganity',
            name='start_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='entityshow',
            name='when_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationcharactercharacter',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationcharactercharacter',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationcharactergenre',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationcharactergenre',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationcharacterurl',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationcharacterurl',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationgenregenre',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationgenregenre',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationgenreurl',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationgenreurl',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganitycharacter',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganitycharacter',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganitygenre',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganitygenre',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganityorganity',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganityorganity',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganityurl',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganityurl',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganitywork',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationorganitywork',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductioncharacter',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductioncharacter',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductiongenre',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductiongenre',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionorganity',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionorganity',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionproduction',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionproduction',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionurl',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionurl',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionwork',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationproductionwork',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowcharacter',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowcharacter',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowgenre',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowgenre',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshoworganity',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshoworganity',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowproduction',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowproduction',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowshow',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowshow',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowurl',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowurl',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowwork',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowwork',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationurlurl',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationurlurl',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkcharacter',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkcharacter',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkgenre',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkgenre',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkurl',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkurl',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkwork',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='relationworkwork',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='begin_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, default=None, null=True),
        ),
    ]
