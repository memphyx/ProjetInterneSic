from django.urls import path
from . import views

urlpatterns = [
    path('mapsindex', views.mapsindex, name='mapsindex'),
    path('mapview', views.mapview, name='mapview'),
    path('AddMapp', views.AddMapp, name='AddMapp'),
    path('Map_Stat', views.Map_Stat, name='Map_Stat'),
    path('MapData', views.MapData, name='MapData'),
    #path('Data_Collect', views.Data_Collect, name='Data_Collect'),
    path('Delete_Data_Collect', views.Delete_Data_Collect, name='Delete_Data_Collect'),
    path('Update_Data_Collect', views.Update_Data_Collect, name='Update_Data_Collect'),
    path('Detail_Data_Collect', views.Detail_Data_Collect, name='Detail_Data_Collect'),
]


