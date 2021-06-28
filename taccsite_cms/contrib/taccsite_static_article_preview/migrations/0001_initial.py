# Generated by Django 2.2.16 on 2021-06-28 23:14

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
            name='TaccsiteStaticAllocsArticlePreview',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='taccsite_static_article_preview_taccsitestaticallocsarticlepreview', serialize=False, to='cms.CMSPlugin')),
                ('media_support', models.CharField(choices=[('nested', 'Nest a single Picture / Image plugin inside this plugin.')], default='nested', max_length=255, verbose_name='How to Add an Image')),
                ('title_text', models.CharField(default='', help_text='The title for the article.', max_length=50, verbose_name='Title')),
                ('abstract_text', models.TextField(default='', help_text='A summary of the article', verbose_name='Abstract')),
                ('expiry_date', models.DateField(blank=True, help_text='The date after which submissions are not accepted (manual entry). Format: YYYY-MM-DD', null=True, verbose_name='Submission End Date')),
                ('publish_date', models.DateField(blank=True, help_text='The date after which submissions are accepted (manual entry). Format: YYYY-MM-DD', null=True, verbose_name='Submission Start Date')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TaccsiteStaticNewsArticlePreview',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='taccsite_static_article_preview_taccsitestaticnewsarticlepreview', serialize=False, to='cms.CMSPlugin')),
                ('media_support', models.CharField(choices=[('nested', 'Nest a single Picture / Image plugin inside this plugin.')], default='nested', max_length=255, verbose_name='How to Add an Image')),
                ('title_text', models.CharField(default='', help_text='The title for the article.', max_length=50, verbose_name='Title')),
                ('abstract_text', models.TextField(default='', help_text='A summary of the article', verbose_name='Abstract')),
                ('type_text', models.CharField(blank=True, help_text='The type of the article, ex: "Science News", "Press Release" (manual entry).', max_length=50, verbose_name='Type')),
                ('author_text', models.CharField(blank=True, help_text='The author of the article (manual entry).', max_length=50, verbose_name='Author')),
                ('publish_date', models.DateField(blank=True, help_text='The date the article was published (manual entry).', null=True, verbose_name='Date Published')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
