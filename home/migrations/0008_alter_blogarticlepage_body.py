# Generated by Django 4.0.4 on 2022-05-04 15:46

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blogarticlepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticlepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
