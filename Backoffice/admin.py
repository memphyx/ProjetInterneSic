from django.contrib import admin
from .models import Equipements, Raccordement_ligne_electrique, Client, Agent, Directions, Emplacement_raccord, Emplacement_equip

admin.site.register(Equipements)
admin.site.register(Raccordement_ligne_electrique)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Directions)
admin.site.register(Emplacement_raccord)
admin.site.register(Emplacement_equip)
