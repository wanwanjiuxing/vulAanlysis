# Generated by Django 4.0 on 2021-12-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulList', '0006_total_vulsfixmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total_vulsFixItem1Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsFixItem2Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsFixItem3Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsFixItem4Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsFixItem5Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsFixItem6Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsFixItem7Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsFixItem8Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('fixed_amount', models.IntegerField(default=0, verbose_name='已整改漏洞')),
                ('fixing_amount', models.IntegerField(default=0, verbose_name='未整改漏洞')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType1Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType2Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType3Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType4Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType5Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType6Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType7Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType8Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
        migrations.CreateModel(
            name='Total_vulsRiseType9Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(default='1/1', max_length=128, verbose_name='日期')),
                ('vuls_amount', models.IntegerField(default=0, verbose_name='漏洞数量')),
            ],
        ),
    ]
