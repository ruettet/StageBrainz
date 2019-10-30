# Generated by Django 2.2.6 on 2019-10-30 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20191030_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationproductioncharacter',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationproductioncharacter',
            name='character_name',
        ),
        migrations.RemoveField(
            model_name='relationproductioncharacter',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationproductioncharacter',
            name='production_name',
        ),
        migrations.RemoveField(
            model_name='relationproductioncharacter',
            name='relation_str',
        ),
        migrations.RemoveField(
            model_name='relationproductionorganity',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationproductionorganity',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationproductionorganity',
            name='organity_name',
        ),
        migrations.RemoveField(
            model_name='relationproductionorganity',
            name='production_name',
        ),
        migrations.RemoveField(
            model_name='relationproductionorganity',
            name='relation_str',
        ),
        migrations.RemoveField(
            model_name='relationproductionproduction',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationproductionproduction',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationproductionproduction',
            name='production_a_name',
        ),
        migrations.RemoveField(
            model_name='relationproductionproduction',
            name='production_b_name',
        ),
        migrations.RemoveField(
            model_name='relationproductionwork',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationproductionwork',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationproductionwork',
            name='production_name',
        ),
        migrations.RemoveField(
            model_name='relationproductionwork',
            name='relation_str',
        ),
        migrations.RemoveField(
            model_name='relationproductionwork',
            name='work_name',
        ),
        migrations.RemoveField(
            model_name='relationshowcharacter',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationshowcharacter',
            name='character_name',
        ),
        migrations.RemoveField(
            model_name='relationshowcharacter',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationshowcharacter',
            name='show_name',
        ),
        migrations.RemoveField(
            model_name='relationshowgenre',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationshowgenre',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationshowgenre',
            name='genre_name',
        ),
        migrations.RemoveField(
            model_name='relationshowgenre',
            name='show_name',
        ),
        migrations.RemoveField(
            model_name='relationshoworganity',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationshoworganity',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationshoworganity',
            name='organity_name',
        ),
        migrations.RemoveField(
            model_name='relationshoworganity',
            name='show_name',
        ),
        migrations.RemoveField(
            model_name='relationshowurl',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationshowurl',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationshowurl',
            name='show_name',
        ),
        migrations.RemoveField(
            model_name='relationshowurl',
            name='url_name',
        ),
        migrations.RemoveField(
            model_name='relationshowwork',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='relationshowwork',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='relationshowwork',
            name='show_name',
        ),
        migrations.RemoveField(
            model_name='relationshowwork',
            name='work_name',
        ),
        migrations.AddField(
            model_name='relationshowshow',
            name='relation_name',
            field=models.CharField(blank=True, help_text='A name for the relation', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='relationshowshow',
            name='relation_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.RelationShowShowType'),
        ),
    ]
