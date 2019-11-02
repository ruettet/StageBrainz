# Generated by Django 2.2.6 on 2019-11-02 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entitycharacter',
            options={'ordering': ['sort_name']},
        ),
        migrations.AlterModelOptions(
            name='entitygenre',
            options={'ordering': ['sort_name']},
        ),
        migrations.AlterModelOptions(
            name='entityorganity',
            options={'ordering': ['sort_name']},
        ),
        migrations.AlterModelOptions(
            name='entityproduction',
            options={'ordering': ['sort_name']},
        ),
        migrations.AlterModelOptions(
            name='entityurl',
            options={'ordering': ['sort_name']},
        ),
        migrations.AlterModelOptions(
            name='entitywork',
            options={'ordering': ['sort_name']},
        ),
        migrations.AlterModelOptions(
            name='relationproductionorganity',
            options={'ordering': ['-highlighted_relation', 'entity_b']},
        ),
        migrations.AlterModelOptions(
            name='relationshowproduction',
            options={'ordering': ['entity_a']},
        ),
    ]
