# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-22 20:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0004_auto_20170411_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsideLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('atitle', models.CharField(blank=True, max_length=200)),
                ('acontent', models.TextField(blank=True)),
                ('alink', models.CharField(blank=True, help_text='Optional, if provided clicking the link will go here.', max_length=2000)),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='AsidePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('picture', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('picture_discription', models.CharField(blank=True, max_length=200, null=True)),
                ('picture_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Aside page',
                'verbose_name_plural': 'Aside pages',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('heading', models.CharField(help_text='The heading under the icon blurbs', max_length=400)),
                ('subheading', models.CharField(help_text='The subheading just below the heading', max_length=400)),
                ('featured_works_heading', models.CharField(default='Featured Works', max_length=200)),
                ('featured_works_sub_heading', models.CharField(default='recent research projects', max_length=200)),
                ('content_heading', models.CharField(default='What We Offer', max_length=200)),
                ('content_sub_heading', models.CharField(default='BMEII applies and validates imaging modalities', max_length=200)),
                ('program_heading', models.CharField(default='OUR PROGRAMS', max_length=200)),
                ('program_sub_heading', models.CharField(default='BMEII combines state-of-the-art facilities', max_length=200)),
                ('latest_posts_heading', models.CharField(default='Latest Posts', max_length=200)),
            ],
            options={
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='IconBlurb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('link', models.CharField(blank=True, help_text='Optional, if provided clicking the blurb will go here.', max_length=2000)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blurbs', to='flat.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('title', models.CharField(default='BMEII Imaging', max_length=200)),
                ('description', models.CharField(default='BMEII programs at Mount Sinai', max_length=200)),
                ('link', models.URLField(blank=True, null=True)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='flat.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(default='BMEII occupies approximately 20,000 square feet.', max_length=200)),
                ('description', models.CharField(default='BMEII is responsible for coordinating                                     and executing all research projects', max_length=400)),
                ('link', models.URLField(blank=True, null=True)),
                ('icon', models.CharField(default='icon-globe icon-medium', max_length=100)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='flat.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='flat.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.AddField(
            model_name='asidelink',
            name='asidepage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asides', to='flat.AsidePage'),
        ),
    ]
