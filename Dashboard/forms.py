from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Equipement


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=8, max_length=15, widget=forms.TextInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Entrer Username"
               }))
    email = forms.EmailField(min_length=8, max_length=50, widget=forms.TextInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Entrer Email"
               }))

    first_name = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Entrer Nom"
               }))

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Entrer prénom"
               }))
    password1 = forms.CharField(min_length=8, max_length=15, widget=forms.PasswordInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Entrer le mot de passe"
               }))
    password2 = forms.CharField(min_length=8, max_length=15, widget=forms.PasswordInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Confirmer le mot de passe"
               }))

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']


class LoginForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Enter Username"
               }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Enter password"
               }))

    class Meta:
        model = User
        fields = ['username', 'password']


class resetpwForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 "
                        "focus:outline-none focus:shadow-outline-purple dark:text-gray-300 "
                        "dark:focus:shadow-outline-gray form-input",
               "placeholder": "Entrer Email"
               }))

    class Meta:
        model = User
        fields = ['email']


class EquipementForm(forms.ModelForm):
    date_abonmt_compt = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Numero du "
                                                                                              "compteur"}))
    date_dinstallation = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Numero du "
                                                                                              "compteur"}))

    class Meta:
        model = Equipement
        fields = '__all__'
