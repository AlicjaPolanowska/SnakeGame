from django.urls import path

from . import views

app_name = 'snakegame'
urlpatterns = [
    path('', views.index, name='index'),
    path('newgame/', views.new_game, name='newgame'),
    path('game/', views.game, name='game'),
    path('the_end/', views.game, name='the_end')
]
