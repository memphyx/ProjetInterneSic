from django.urls import path
from . import views

urlpatterns = [

    path('dbhomepage', views.dbhomepage, name='dbhomepage'),
    path('accordion', views.accordion, name='accordion'),
    path('auth_normal_sign_in', views.auth_normal_sign_in, name='auth_normal_sign_inn'),
    path('auth_sign_up', views.auth_sign_up, name='auth_sign_up'),
    path('bs_basic_table', views.bs_basic_table, name='bs_basic_table'),
    path('account', views.account, name='account'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('button', views.button, name='button'),
    path('chart', views.chart, name='chart'),
   # path('forms', views.forms, name='forms'),
    #path('cards', views.cards, name='cards'),
    #path('charts', views.charts, name='charts'),
    #path('dblogin', views.dblogin, name='dblogin'),
    #path('deconnexion', views.deconnexion, name='deconnexion'),
]

