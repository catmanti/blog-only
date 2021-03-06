# Generated by Django 4.0.4 on 2022-05-05 17:54

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0008_alter_blogarticlepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='blog_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='add additional text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
