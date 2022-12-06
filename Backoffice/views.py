from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import *


# Create your views here.
def dbindex(request):
    import json
    import requests

    # header = {
    #   "Authorization": "Token f137b9110ad8f79faa24e0194bdfb6329e0e8877"
    # }
    # kobodata = requests.get('https://kf.kobotoolbox.org/api/v2/assets/aJDTcJNqBnRkzpdr5U6uJQ.json', headers=header)

    # api = json.loads(kobodata.content)

    # context = {
    #     'api': api
    #  }

    return render(request, 'dbindex.html')


def buttons(request):
    return render(request, 'buttons.html')


def create_account(request):
    # retour a la page daccueil si lutilisateur est conn
    if request.user.is_authenticated:
        return redirect('dbindex')
    if request.method == 'POST':
        form1 = RegisterForm(request.POST)
        if form1.is_valid():
            # verification d'existence d'un utilisateur
            if User.objects.filter(username=form1.cleaned_data['username']).exists():
                return render(request, 'create_account.html', {'form1': form1})

            else:
                # creation d'utilisatleur
                username = form1.cleaned_data['username']
                first_name = form1.cleaned_data['first_name']
                last_name = form1.cleaned_data['last_name']
                email = form1.cleaned_data['email']
                password = form1.cleaned_data['password2']

                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save()
                # connexion de l'utilisateur cree
                login(request, user)

            if user is not None:
                return redirect('dblogin')
        else:
            return render(request, 'create-account.html', {'form1': form1})

    form1 = RegisterForm()
    return render(request, 'create-account.html', {'form1': form1})


def dblogin(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeindex')
        else:
            messages.info(request, 'username ou password est incorrecte')

    context = {'form': form}
    return render(request, 'login.html', context)


def deconnexion(request):
    logout(request)
    return redirect('homeindex')


def forgot_password(request):
    form = resetpwForm()

    context = {'form': form}
    return render(request, 'forgot-password.html', context)


def error(request):
    return render(request, '404.html')


def blank(request):
    return render(request, 'blank.html')


def cards(request):
    return render(request, 'cards.html')


def charts(request):
    return render(request, 'charts.html')


def forms(request):
    if request.method == 'POST':
        form = EquipementsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('forms')
    form2 = EquipementsForm()
    # dbdata = Equipement.objects.all()
    context = {
        'form2': form2,
        # 'dbdata': dbdata
    }
    return render(request, 'forms.html', context)


def forms_details(request):
    form2 = EquipementsForm()
    tous_les_equipements = Equipements.objects.all()
    # compteur_actif = tous_les_equipements.filter(activite_compteur="Actif").count()
    # compteur_non_actif = tous_les_equipements.filter(activite_compteur="Non_Actif").count()
    total_des_equipement = tous_les_equipements.count()
    context = {
        'form2': form2,
        'tous_les_equipements': tous_les_equipements,
        'total_des_equipement': total_des_equipement,
        # 'compteur_actif': compteur_actif,
        # 'compteur_non_actif': compteur_non_actif,
    }
    return render(request, 'forms_details.html', context)


def forms_update(request):
    return render(request, 'forms_update.html')


def forms_view(request):
    return render(request, 'forms_view.html')


def forms_delete(request):
    return render(request, 'forms_delete.html')


def Direction(request):
    if request.method == 'POST':
        form = DirectionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Direction')

    form2 = DirectionForm()

    total_directions = Directions.objects.all()
    tous_les_directions = total_directions.count()

    context = {
        'form2': form2,
        'totaldirection': total_directions,
        'tous_les_directions': tous_les_directions
    }
    return render(request, 'Direction.html', context)


def direction_view(request):
    return render(request, 'direction_view.html')


def direction_delete(request):
    return render(request, 'direction_delete.html')


def direction_update(request):
    return render(request, 'direction_update.html')


def detail_direction(request):
    form2 = DirectionForm()
    total_directions = Directions.objects.all()
    tous_les_directions = total_directions.count()

    context = {
        'form2': form2,
        'total_directions': total_directions,
        'tous_les_directions': tous_les_directions
    }

    return render(request, 'direction_detail.html', context)


def agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('agent')
    form2 = AgentForm()
    tous_les_agents = Agent.objects.all()
    total_agent = tous_les_agents.count()
    context = {
        'form2': form2,
        'tous_les_agents': tous_les_agents,
        'total_agent': total_agent
    }
    return render(request, 'agent.html', context)


def agent_detail(request):
    form2 = AgentForm()
    tous_les_agents = Agent.objects.all()
    total_agent = tous_les_agents.count()
    context = {
        'form2': form2,
        'tous_les_agents': tous_les_agents,
        'total_agent': total_agent
    }
    return render(request, 'agent_detail.html', context)


def agent_view(request):
    return render(request, 'agent_view.html')


def agent_delete(request):
    return render(request, 'agent_delete.html')


def agent_update(request):
    return render(request, 'agent_update.html')


def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('client')

    form2 = ClientForm()
  #  tous_les_client = Client.objets.all()
   # total_client = tous_les_client.count()
    context = {
        'form2': form2,
   #     'tous_les_client': tous_les_client,
    #    'total_client': total_client
    }
    return render(request, 'client.html', context)


def client_detail(request):
    form2 = ClientForm()
    tous_les_client = Client.objets.all()
    total_client = tous_les_client.count()

    context = {
        'form2': form2,
        'tous_les_client': tous_les_client,
        'total_client': total_client
    }
    return render(request, 'client_detail.html', context)


def client_view(request):
    return render(request, 'client_view.html')


def client_delete(request):
    return render(request, 'client_delete.html')


def client_update(request):
    return render(request, 'client_update.html')


def Emplacement_equip(request):
    if request.method == 'POST':
        form = Emplacement_EquipForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Emplacement_equip')
    form2 = Emplacement_EquipForm()
    # dbdata = Equipement.objects.all()
    context = {
        'form2': form2,
        # 'dbdata': dbdata
    }
    return render(request, 'Emplacement_equip.html', context)


def Emplacement_raccord(request):
    if request.method == 'POST':
        form = Emplacement_raccordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Emplacement_equip')
    form2 = Emplacement_raccordForm()
    # dbdata = Equipement.objects.all()
    context = {

        'form2': form2,
        # 'dbdata': dbdata
    }
    return render(request, 'Emplacement_raccord.html', context)


def Raccordement_ligne_electrique(request):
    if request.method == 'POST':
        form = Raccordement_ligne_electriqueForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Emplacement_equip')
    form2 = Raccordement_ligne_electriqueForm()
    # tous_les_raccordement_electrique = Equipement.objects.all()
    context = {

        'form2': form2,
        # 'dbdata': dbdata
    }
    return render(request, 'Raccordement_ligne_electrique.html', context)


def modals(request):
    return render(request, 'modals.html')


def tables(request):
    return render(request, 'tables.html')


def account(request):
    return render(request, 'account.html')


def forgot_password_done(request):
    return render(request, 'forgot-password_done.html')
