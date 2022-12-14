# Generated by Django 4.1.1 on 2022-12-06 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('matricule_agent', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True, verbose_name='Matricule Agent')),
                ('nom_complet_agent', models.CharField(max_length=255, verbose_name='Nom Complet Agent')),
                ('contact_agent', models.CharField(max_length=12, verbose_name='Contact Agent')),
                ('date_prise_service', models.DateField(verbose_name='Date prise de service')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_complet', models.CharField(max_length=255, verbose_name='Nom complet')),
                ('contact_client', models.CharField(max_length=11, verbose_name='Contact')),
                ('Lieu_habitation', models.CharField(max_length=255, verbose_name='Lieu habitation')),
                ('date_abonmt_client', models.DateField(verbose_name="Date d'abonnement client")),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('reference_direction', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Reference direction')),
                ('date_creation_direction', models.DateField(verbose_name='Date de creation')),
                ('information_direction', models.TextField(max_length=255, verbose_name='Information sur Direction')),
            ],
        ),
        migrations.CreateModel(
            name='Emplacement_equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude_emplacement_equip', models.FloatField(verbose_name='La latitude')),
                ('longitude_emplacement_equip', models.FloatField(verbose_name='La Longitude')),
                ('Desc_emplacement_equip', models.TextField(max_length=25, verbose_name='Description emplacement')),
            ],
        ),
        migrations.CreateModel(
            name='Emplacement_raccord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude_emplacement_raccord', models.FloatField(verbose_name='La latitude')),
                ('longitude_emplacement_raccord', models.FloatField(verbose_name='La Longitude')),
                ('Desc_emplacement_raccord', models.TextField(max_length=25, verbose_name='Description emplacement')),
            ],
        ),
        migrations.CreateModel(
            name='Equipements',
            fields=[
                ('num_compt', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Numero du Compteur')),
                ('amperage_compt', models.CharField(choices=[('5A', '5A'), ('5A', '10A'), ('15A', '15A'), ('20A', '20A'), ('25A', '25A'), ('25A', '30A')], max_length=10, verbose_name='Amperage')),
                ('phase_compt', models.CharField(choices=[('Monophasique', 'Monophasique'), ('Diphasique', 'Diphasique'), ('Triphasique', 'Triphasique')], max_length=25, verbose_name='Phase du compteur')),
                ('type_compt', models.CharField(choices=[('prepay??', 'Prepay??'), ('postpay??', 'Postpay??')], max_length=10, verbose_name='Type de compteur')),
                ('localite_compt', models.CharField(max_length=15, verbose_name='localit??')),
                ('date_dinstallation', models.DateTimeField(verbose_name="Date d'installation")),
                ('date_abonmt_compt', models.DateTimeField(verbose_name="Date d'abonnement")),
                ('compt_actif', models.CharField(choices=[('Actif', 'Actif'), ('Non_Actif', 'Non_Actif')], max_length=15, verbose_name='Activit?? du compteur')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.agent')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.client')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.directions')),
                ('emplacement_equip', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.emplacement_equip')),
            ],
        ),
        migrations.CreateModel(
            name='Raccordement_ligne_electrique',
            fields=[
                ('reference_raccordement', models.CharField(max_length=225, primary_key=True, serialize=False, verbose_name='R??ference raccordement')),
                ('date_raccordement', models.DateField(verbose_name='Date raccordement')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.agent')),
                ('emplacement_raccord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.emplacement_raccord')),
                ('equipements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.equipements')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backoffice.directions'),
        ),
    ]
