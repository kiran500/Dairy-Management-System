# Generated by Django 2.1.7 on 2019-03-03 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0005_auto_20190303_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalname', models.CharField(db_index=True, max_length=200)),
                ('milkprice', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='animalcategory',
            name='related_vendor',
        ),
        migrations.RenameModel(
            old_name='AddVendor',
            new_name='Vendor',
        ),
        migrations.DeleteModel(
            name='AnimalCategory',
        ),
        migrations.AddField(
            model_name='milkcategory',
            name='related_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MilkCategory', to='dairyapp.Vendor'),
        ),
    ]
