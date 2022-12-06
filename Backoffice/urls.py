from django.urls import path
from . import views

urlpatterns = [

    path('dbindex', views.dbindex, name='dbindex'),
    path('buttons', views.buttons, name='buttons'),
    path('create_account', views.create_account, name='create_account'),
    path('modals', views.modals, name='modals'),
    path('tables', views.tables, name='tables'),
    path('account', views.account, name='account'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('error', views.error, name='error'),
    path('blank', views.blank, name='blank'),

    path('forms', views.forms, name='forms'),
    path('forms_details', views.forms_details, name='forms_details'),
    path('forms_view', views.forms_view, name='forms_view'),
    path('forms_update', views.forms_update, name='forms_update'),
    path('forms_delete', views.forms_delete, name='forms_delete'),

    path('Direction', views.Direction, name='Direction'),
    path('detail_direction', views.detail_direction, name='detail_direction'),
    path('direction_delete', views.direction_delete, name='direction_delete'),
    path('direction_update', views.direction_update, name='direction_update'),
    path('direction_view', views.direction_view, name='direction_view'),


    path('agent', views.agent, name='agent'),
    path('agent_detail', views.agent_detail, name='agent_detail'),
    path('agent_view', views.agent_view, name='agent_view'),
    path('agent_delete', views.agent_delete, name='agent_delete'),
    path('agent_update', views.agent_update, name='agent_update'),


    path('client', views.client, name='client'),
    path('client_detail', views.client_detail, name='client_detail'),
    path('client_delete', views.client_delete, name='client_delete'),
    path('client_update', views.client_update, name='client_update'),
    path('client_view', views.client_view, name='client_view'),



    path('Emplacement_equip', views.Emplacement_equip, name='Emplacement_equip'),
    path('Emplacement_raccord', views.Emplacement_raccord, name='Emplacement_raccord'),
    path('Raccordement_ligne_electrique', views.Raccordement_ligne_electrique, name='Raccordement_ligne_electrique'),

    path('cards', views.cards, name='cards'),
    path('charts', views.charts, name='charts'),
    path('dblogin', views.dblogin, name='dblogin'),
    path('deconnexion', views.deconnexion, name='deconnexion'),

]
