# Generated by Django 2.2.16 on 2021-06-28 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taccsite_static_article_list', '0004_auto_20210628_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taccsitearticlelist',
            old_name='header_title_text',
            new_name='title_text',
        ),
    ]
