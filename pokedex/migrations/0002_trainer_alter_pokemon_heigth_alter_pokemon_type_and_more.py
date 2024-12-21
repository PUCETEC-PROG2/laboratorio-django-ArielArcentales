# Generated by Django 4.2 on 2024-12-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_mane', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='heigth',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('C', 'Tierra'), ('B', 'Fuego'), ('A', 'Agua'), ('F', 'Lagartija'), ('E', 'Electrico'), ('D', 'Planta')], max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weigth',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
