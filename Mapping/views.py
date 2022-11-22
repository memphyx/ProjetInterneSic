from django.shortcuts import render, redirect
from .forms import EquipementForm
#from .models import Equipement


# Create your views here.
def mapsindex(request):
    return render(request, 'mapsindex.html')


def mapview(request):
    return render(request, 'mapview.html')


def AddMapp(request):
    return render(request, 'AddMapp.html')


def MapData(request):
    import json
    import requests

    header = {
        "Authorization": "Token f137b9110ad8f79faa24e0194bdfb6329e0e8877"
    }
    kobodata = requests.get('https://kc.kobotoolbox.org/api/v1/data/1132854.json', headers=header)

    api = json.loads(kobodata.content)

    context = {'api': api}

    return render(request, 'MapData.html', context)


def Map_Stat(request):
    return render(request, 'Map_Stat.html')


'''def Data_Collect(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Data_Collect')
    form2 = EquipementForm()
    dbdata = Equipement.objects.all()
    context = {
        'form2': form2,
        'dbdata': dbdata
    }
    return render(request, 'Data_Collect.html', context)'''


def Delete_Data_Collect(request):
    return render(request, 'Data_Collect.html')


def Update_Data_Collect(request):
    return render(request, 'Data_Collect.html')


def Detail_Data_Collect(request):
    return render(request, 'Data_Collect.html')
