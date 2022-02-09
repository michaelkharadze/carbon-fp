# Generated by Django 3.1.5 on 2022-02-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footprint', '0011_auto_20210912_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bottledGasUsed',
            field=models.IntegerField(blank=True, null=True, verbose_name=' გამოყენებული ჩამოსხმული გაზი გასული წლის განმავლობაში (კილოგრამებში)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='coalUsed',
            field=models.IntegerField(blank=True, null=True, verbose_name=' გამოიყენებული ქვანახშირი გასული წლის განმავლობაში (კილოგრამებში)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='electricityGreen',
            field=models.IntegerField(choices=[(100, 'არა'), (75, 'დიახ')], default=100, verbose_name=' იყენებთ მწვანე ენერგიას?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='heatingGasUsed',
            field=models.BooleanField(choices=[(0, 'არა'), (1, 'დიახ')], default=0, verbose_name=' გამოიყენება თქვენ სახლში ზეთი, ქვანახშირი, შეშა ან ჩამოსხმული გაზი გასათბობად?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='heatingOilUsed',
            field=models.IntegerField(blank=True, null=True, verbose_name=' გამოყენებული ზეთი გასული წლის განმავლობაში (ლიტრებში)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='miscSpending',
            field=models.DecimalField(choices=[(50, 'დიდი რაოდენობა'), (34, 'საშუალო რაოდენობა'), (24, 'მცირე რაოდენობა'), (14, 'ძალიან მცირე')], decimal_places=2, default=34, max_digits=6, null=True, verbose_name=' რა რაოდენობას ხარჯავთ სხვადასხვა ხარჯებში?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='recyclePGM',
            field=models.DecimalField(blank=True, choices=[(0, 'არა'), (7, 'დიახ')], decimal_places=2, default=0, max_digits=6, null=True, verbose_name=' ქაღალდს, მინას და ლითონს ამუშავებთ?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='recyclePlastic',
            field=models.DecimalField(blank=True, choices=[(0, 'არა'), (14, 'დიახ')], decimal_places=2, default=0, max_digits=6, null=True, verbose_name=' პლასტმასს ამუშავებთ გარდა პოლიეთილენის პარკებისა?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='woodUsed',
            field=models.IntegerField(blank=True, null=True, verbose_name=' გამოყენებული შეშა გასული წლის განმავლობაში (კილოგრამებში)'),
        ),
    ]