from django.db import models


class Directions(models.Model):
    reference_direction = models.CharField(verbose_name='Reference direction', max_length=20, null=False,
                                           primary_key=True, unique=True)
    date_creation_direction = models.DateField(verbose_name='Date de creation', null=False)
    # date_enregistrement = models.DateField(verbose_name='Date enregistrement', auto_now_add=True, null=False)
    information_direction = models.TextField(verbose_name='Information sur Direction', max_length=255, null=False)

    def __str__(self):
        return f'{self.reference_direction}-{self.information_direction}'


class Agent(models.Model):
    matricule_agent = models.CharField(primary_key=True, verbose_name="Matricule Agent", max_length=25, unique=True,
                                       null=False)
    nom_complet_agent = models.CharField(verbose_name='Nom Complet Agent', max_length=255, null=False)
    contact_agent = models.CharField(verbose_name='Contact Agent', max_length=12, null=False)
    # date_enregistrement = models.DateField(verbose_name='Date enregistrement', auto_now_add=True, null=False)
    date_prise_service = models.DateField(verbose_name='Date prise de service', null=False)

    direction = models.ForeignKey(Directions, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom_complet_agent}'


class Client(models.Model):
    num_client = models.CharField(verbose_name="Numero Client", primary_key=True, unique=True, null=False,
                                  max_length=25)
    nom_complet = models.CharField(verbose_name='Nom complet', max_length=255, null=False)
    contact_client = models.CharField(verbose_name='Contact', max_length=11, null=False)
    Lieu_habitation = models.CharField(verbose_name='Lieu habitation', max_length=255, null=False)
    # date_enregistrement = models.DateField(verbose_name='Date enregistrement', auto_now_add=True, null=False)
    date_abonmt_client = models.DateField(verbose_name="Date d'abonnement client", null=False)

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom_complet}-{self.contact_client}'


class Emplacement_equip(models.Model):
    latitude_emplacement_equip = models.FloatField(verbose_name='La latitude', null=False)
    longitude_emplacement_equip = models.FloatField(verbose_name='La Longitude', null=False)
    # date_enregistrement = models.DateField(verbose_name='Date enregistrement', auto_now_add=True, null=False)
    Desc_emplacement_equip = models.TextField(verbose_name='Description emplacement', max_length=25, null=False)

    def __str__(self):
        return f'{self.longitude_emplacement_equip}-{self.latitude_emplacement_equip}-{self.Desc_emplacement_equip}'


class Equipements(models.Model):
    activite_compteur = [
        ('Actif', 'Actif'),
        ('Non_Actif', 'Non_Actif'),
    ]
    choix_type = [
        ('prepayé', 'Prepayé'),
        ('postpayé', 'Postpayé'),
    ]
    choix_phase = [

        ('Monophasique', 'Monophasique'),
        ('Diphasique', 'Diphasique'),
        ('Triphasique', 'Triphasique'),
    ]
    choix_amperage = [
        ('5A', '5A'),
        ('5A', '10A'),
        ('15A', '15A'),
        ('20A', '20A'),
        ('25A', '25A'),
        ('25A', '30A'),
    ]

    num_compt = models.CharField(verbose_name="Numero du Compteur", null=False, max_length=20, unique=True,
                                 primary_key=True)
    amperage_compt = models.CharField(verbose_name="Amperage", null=False, choices=choix_amperage, max_length=10)
    phase_compt = models.CharField(verbose_name="Phase du compteur", null=False, choices=choix_phase, max_length=25)
    type_compt = models.CharField(verbose_name="Type de compteur", null=False, choices=choix_type, max_length=10)
    localite_compt = models.CharField(verbose_name="localité", null=False, max_length=15)
    # date_enregistrement = models.DateField(verbose_name='Date enregistrement', auto_now_add=True, null=False)
    date_dinstallation = models.DateTimeField(verbose_name="Date d'installation", null=False)
    date_abonmt_compt = models.DateTimeField(verbose_name="Date d'abonnement", null=False)
    compt_actif = models.CharField(verbose_name="Activité du compteur", choices=activite_compteur, max_length=15)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE)
    emplacement_equip = models.OneToOneField(Emplacement_equip, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.num_compt}'


class Emplacement_raccord(models.Model):
    latitude_emplacement_raccord = models.FloatField(verbose_name='La latitude', null=False)
    longitude_emplacement_raccord = models.FloatField(verbose_name='La Longitude', null=False)
    Desc_emplacement_raccord = models.TextField(verbose_name='Description emplacement', max_length=25, null=False)


class Raccordement_ligne_electrique(models.Model):
    reference_raccordement = models.CharField(verbose_name='Réference raccordement', max_length=225, null=False,
                                              primary_key=True)
    date_raccordement = models.DateField(verbose_name='Date raccordement', null=False)
    # date_enregistrement = models.DateField(verbose_name='Date enregistrement', auto_now_add=True, null=False)

    equipements = models.ForeignKey(Equipements, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    emplacement_raccord = models.OneToOneField(Emplacement_raccord, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reference_raccordement}'
