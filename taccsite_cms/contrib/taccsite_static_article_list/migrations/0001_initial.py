# Generated by Django 2.2.16 on 2021-06-23 23:31

from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaccsiteArticleList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='taccsite_static_article_list_taccsitearticlelist', serialize=False, to='cms.CMSPlugin')),
                ('header_title_text', models.CharField(blank=True, help_text='The title at the top of the list.', max_length=100)),
                ('footer_link_text', models.CharField(blank=True, help_text='The "See All ..." link at the bottom of the list.', max_length=100)),
                ('content_type', models.CharField(blank=True, choices=[('news', 'News'), ('docs', 'Documents'), ('allocs', 'Allocations'), ('events', 'Events')], max_length=255)),
                ('layout_type', models.CharField(blank=True, choices=[('always-rows-N--even', '(always) N Even Rows'), ('widest-cols-2--even', '(at widest) 2 Equal Columns'), ('widest-cols-2--wide-narr', '(at widest) 2 Cols: 1 Wide, 1 Narrow'), ('widest-cols-2--narr-wide', '(at widest) 2 Cols: 1 Narrow, 1 Wide'), ('widest-cols-3--even', '(at widest) 3 Equal Columns')], default='always-rows-N--even', max_length=255)),
                ('style_type', models.CharField(blank=True, choices=[('divided', 'Dividers Between Articles')], max_length=255)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]