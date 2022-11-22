from django.db import models
'''
choix_amperage = [
    ('1', '5A'),
    ('2', '10A'),
    ('3', '15A'),
    ('4', '20A'),
    ('5', '25A'),
    ('6', '30A'),
]


choix_phase = [

    ('1', 'Monophasique'),
    ('2', 'Diphasique'),
    ('3', 'Triphasique'),
]

choix_type = [
    ('1', 'prepayé'),
    ('2', 'postpayé'),
]

activite_compteur = [
    ('1', 'Actif'),
    ('2', 'Non Actif'),
]


class Equipement(models.Model):
    num_compt = models.CharField(verbose_name="Numero du Compteur", null=False, max_length=20)
    amperage_compt = models.CharField(verbose_name="Amperage", null=False, choices=choix_amperage, max_length=10)
    phase_compt = models.CharField(verbose_name="Phase du compteur", null=False, choices=choix_phase, max_length=10)
    type_compt = models.CharField(verbose_name="Type de compteur", null=False, choices=choix_type, max_length=10)
    longitude_compt = models.FloatField(verbose_name="Longitude", null=False)
    latitude_compt = models.FloatField(verbose_name="Latitude", null=False)
    nom_sur_compt = models.CharField(verbose_name="Propietaire sur compteur", null=False, max_length=50)
    tel_sur_compt = models.CharField(verbose_name="Telephone du Proprio", null=True, max_length=12)
    localite_compt = models.CharField(verbose_name="localité", null=False, max_length=15)
    date_abonmt_compt = models.DateField(verbose_name="Date d'abonnement compteur", null=False)
    date_dinstallation = models.DateField(verbose_name="Date d'installation", null=False)
    compt_actif = models.CharField(verbose_name="Activité du compteur", choices=activite_compteur, max_length=15)

    def __str__(self):
        return self.nom_sur_compt + ' ' + self.tel_sur_compt

'''
