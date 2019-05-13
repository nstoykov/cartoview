# Generated by Django 2.2 on 2019-05-13 08:55

import cartoview.fields
import cartoview.layers.validators
import cartoview.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_resource', '0001_initial'),
        ('layers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_resource.BaseModel')),
                ('bounding_box', cartoview.fields.ListField(blank=True, default=[0, 0, 0, 0], null=True, validators=[cartoview.validators.ListValidator(max_length=4, min_length=4)])),
                ('projection', models.CharField(default='EPSG:3857', max_length=30, validators=[cartoview.layers.validators.validate_projection])),
                ('center', cartoview.fields.ListField(default=[0, 0], validators=[cartoview.validators.ListValidator(max_length=2, min_length=2)])),
                ('constrain_rotation', models.BooleanField(default=True)),
                ('enable_rotation', models.BooleanField(default=True)),
                ('max_zoom', models.IntegerField(default=28, validators=[django.core.validators.MaxValueValidator(28), django.core.validators.MinValueValidator(0)])),
                ('min_zoom', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(28), django.core.validators.MinValueValidator(0)])),
                ('zoom_factor', models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(28), django.core.validators.MinValueValidator(1)])),
                ('zoom', models.FloatField(default=6, validators=[django.core.validators.MaxValueValidator(28), django.core.validators.MinValueValidator(1)])),
                ('rotation', models.IntegerField(default=0)),
                ('render_options', jsonfield.fields.JSONField(blank=True, default=dict)),
                ('layers', models.ManyToManyField(blank=True, to='layers.Layer')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maps', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site_maps', to='sites.Site')),
            ],
            bases=('base_resource.basemodel',),
        ),
    ]
