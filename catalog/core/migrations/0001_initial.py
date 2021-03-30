# Generated by Django 3.1.5 on 2021-03-30 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Category of footwear.', max_length=100, verbose_name='Category.')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Collection.', max_length=100, verbose_name='Collection.')),
            ],
        ),
        migrations.CreateModel(
            name='Footwear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Code of footwear.', max_length=100, verbose_name='Code.')),
                ('upper', models.CharField(help_text='Upper/Leather material of footwear.', max_length=100, verbose_name='Upper.')),
                ('name', models.CharField(help_text='Title of footwear', max_length=100, verbose_name='Title.')),
                ('outsole', models.CharField(help_text='Outsole material of footwear.', max_length=100, verbose_name='Outsole.')),
                ('lining', models.CharField(help_text='Lining material of footwear.', max_length=100, verbose_name='Lining.')),
                ('shoelaces', models.CharField(help_text='Shoelaces material of footwear.', max_length=100, verbose_name='Shoelaces.')),
                ('insole', models.CharField(help_text='Insole material of footwear.', max_length=100, verbose_name='Insole.')),
                ('abc_curve', models.CharField(help_text='ABC curve of footwear.', max_length=1, verbose_name='Category.')),
                ('cost_price', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Size grid.', max_length=100, verbose_name='Size')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Status of sale.', max_length=100, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of photo.', max_length=100, verbose_name='Title.')),
                ('url', models.URLField(help_text='URL of photo.', verbose_name='URL.')),
                ('thumb', models.URLField(help_text='URL thumb of photo.', verbose_name='Thumb.')),
                ('mime', models.CharField(help_text='Mime type of photo.', max_length=100, verbose_name='MIME.')),
                ('extension', models.CharField(help_text='Extension type of photo.', max_length=10, verbose_name='Extension.')),
                ('code_footwear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.footwear')),
            ],
        ),
        migrations.AddField(
            model_name='footwear',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.size'),
        ),
        migrations.AddField(
            model_name='footwear',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
    ]
