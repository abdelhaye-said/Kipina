# Generated by Django 3.0.4 on 2021-07-10 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('nationalite', models.CharField(max_length=100, null=True)),
                ('langueMaternelle', models.CharField(max_length=100, null=True)),
                ('langueParlee', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('exterieur', 'exterieur'), ('interne', 'interne')], max_length=100, null=True)),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('classe', models.CharField(choices=[('Foxes', 'Foxes'), ('Little Foxes', 'Little Foxes'), ('Bears', 'Bears'), ('Seals', 'Seals'), ('Owls', 'Owls')], max_length=100, null=True)),
                ('frais_scolarite', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_transport', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM'), ('AM-PM', 'AM-PM'), ('NON', 'NON')], max_length=100, null=True)),
                ('enfant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.Enfant')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Garde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_transport', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM'), ('AM-PM', 'AM-PM'), ('Mercredi PM', 'Mercredi PM')], max_length=100, null=True)),
                ('enfant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.Enfant')),
            ],
        ),
        migrations.CreateModel(
            name='Renseignement_pere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('enfant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.Enfant')),
            ],
        ),
        migrations.CreateModel(
            name='Cantine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_transport', models.CharField(choices=[('4j', '4j'), ('5j', '5j'), ('NON', 'NON')], max_length=100, null=True)),
                ('enfant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.Enfant')),
            ],
        ),
        migrations.CreateModel(
            name='Assurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assure', models.BooleanField()),
                ('enfant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.Enfant')),
            ],
        ),
    ]
