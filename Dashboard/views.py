from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, resetpwForm, EquipementForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Equipement


# Create your views here.
def dbhomepage(request):
    import json
    import requests

    header = {
        "Authorization": "Token f137b9110ad8f79faa24e0194bdfb6329e0e8877"
    }
    kobodata = requests.get('https://kf.kobotoolbox.org/api/v2/assets/aJDTcJNqBnRkzpdr5U6uJQ.json', headers=header)

    api = json.loads(kobodata.content)

    context = {
        'api': api
    }

    return render(request, 'dbhomepage.html', context)


def accordion(request):
    return render(request, 'accordion.html')


def auth_normal_sign_in(request):
    if request.method == 'POST':
        form1 = RegisterForm(request.POST)
        if form1.is_valid():
            # verification d'existence d'un utilisateur
            if User.objects.filter(username=form1.cleaned_data['username']).exists():
                return render(request, 'auth_normal_sign_in.html', {'form1': form1})

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
            return render(request, 'auth_normal_sign_in.html', {'form1': form1})

    form1 = RegisterForm()
    return render(request, 'cauth_normal_sign_in', {'form1': form1})


def auth_sign_up(request):
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
    return render(request, 'auth_sign_up.html', context)


def deconnexion(request):
    logout(request)
    return redirect('homeindex')


def forgot_password(request):
    form = resetpwForm()

    context = {'form': form}
    return render(request, 'forgot-password.html', context)


def breadcrumb(request):
    return render(request, 'breadcrumb.html')


def bs_basic_table(request):
    return render(request, 'bs_basic_table.html')


def button(request):
    return render(request, 'button.html')


def chart(request):
    return render(request, 'chart.html')


def form_elements_component(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('forms')
    form2 = EquipementForm()
    dbdata = Equipement.objects.all()
    context = {
        'form2': form2,
        'dbdata': dbdata
    }
    return render(request, 'form_elements_component.html',context)


def color(request):
    return render(request, 'color.html')


def tables(request):
    return render(request, 'tables.html')


def account(request):
    return render(request, 'account.html')


def forgot_password_done(request):
    return render(request, 'forgot-password_done.html')
