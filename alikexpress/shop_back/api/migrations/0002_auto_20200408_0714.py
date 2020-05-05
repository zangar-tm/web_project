# Generated by Django 3.0.4 on 2020-04-08 07:14

from django.db import migrations, models
import django.db.models.deletion
import utils.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='has_discount',
            field=models.BooleanField(default=False, verbose_name='Есть скидка?'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False, verbose_name='Есть в наличие?'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_top',
            field=models.BooleanField(default=False, verbose_name='В топе?'),
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Понравилось'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.TextField(blank=True, null=True, verbose_name='Полное описание продукта'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_with_discount',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание продукта'),
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, verbose_name='Ключ')),
                ('value', models.CharField(max_length=50, verbose_name='Значение')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='api.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Характеристика продукта',
                'verbose_name_plural': 'Характеристики продукта',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField()),
                ('content', models.TextField(blank=True, null=True)),
                ('user_full_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Отзыв о продукте',
                'verbose_name_plural': 'Отзывы о продукте',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to=utils.file_upload.image_path, verbose_name='Картинки')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Картинка продукта',
                'verbose_name_plural': 'Картинки продукта',
            },
        ),
        migrations.CreateModel(
            name='Fabricator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название производителя')),
                ('categories', models.ManyToManyField(blank=True, null=True, related_name='fabricators', to='api.Category', verbose_name='Производители')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='fabricator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.Fabricator', verbose_name='Производитель'),
        ),
    ]