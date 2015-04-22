from django.conf.urls import patterns, include, url

from api import views

urlpatterns = [
	
	### Start Real Urls ###

    # ex: /api/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^levels/$', views.LevelsView.as_view(), name='levels'),
    url(r'^levels/create/$', views.createMap, name='createMap'),
    url(r'^levels_weapons/create/$', views.createMapWeapon, name='createMapWeapon'),
    url(r'^levels_vehicles/create/$', views.createMapVehicle, name='createMapVehicle'),
    url(r'^levels_game_modes/create/$', views.createMapGameMode, name='createMapGameMode'),
    url(r'^levels/(?P<pk>[0-9]+)/edit/$', views.LevelsEditView.as_view(), name='levelsEdit'),
    url(r'^levels/(?P<pk>[0-9]+)/edit_change/$', views.editLevel, name='editLevel'),

    url(r'^characters/$', views.CharactersView.as_view(), name='characters'),
    url(r'^characters/create/$', views.createCharacter, name='createCharacter'),
    url(r'^characters/(?P<pk>[0-9]+)/edit/$', views.CharactersEditView.as_view(), name='charactersEdit'),
    url(r'^characters/(?P<pk>[0-9]+)/edit_change/$', views.editCharacter, name='editCharacter'),

    url(r'^weapons/$', views.WeaponsView.as_view(), name='weapons'),
    url(r'^weapons/create/$', views.createWeapon, name='createWeapon'),
    url(r'^weapons/(?P<pk>[0-9]+)/edit/$', views.WeaponsEditView.as_view(), name='weaponsEdit'),
    url(r'^weapons/(?P<pk>[0-9]+)/edit_change/$', views.editWeapon, name='editWeapon'),

    url(r'^vehicles/$', views.VehiclesView.as_view(), name='vehicles'),
    url(r'^vehicles/create/$', views.createVehicle, name='createVehicle'),
    url(r'^vehicles/(?P<pk>[0-9]+)/edit/$', views.VehiclesEditView.as_view(), name='vehiclesEdit'),
    url(r'^vehicles/(?P<pk>[0-9]+)/edit_change/$', views.editVehicle, name='editVehicle'),

    url(r'^games/$', views.GamesView.as_view(), name='games'),
    url(r'^games/create/$', views.createGame, name='createGame'),
    url(r'^games_game_modes/create/$', views.createGamesGameMode, name='createGamesGameMode'),
    url(r'^games_characters/create/$', views.createGamesCharacters, name='createGamesCharacters'),
    url(r'^games_achievements/create/$', views.createGamesAchievements, name='createGamesAchievements'),
    url(r'^games/(?P<pk>[0-9]+)/edit/$', views.GamesEditView.as_view(), name='gamesEdit'),
    url(r'^games/(?P<pk>[0-9]+)/edit_change/$', views.editGame, name='editGame'),

    url(r'^gamemodes/$', views.GameModesView.as_view(), name='gamemodes'),
    url(r'^gamemodes/create/$', views.createGameMode, name='createGameMode'),
    url(r'^gamemodes/(?P<pk>[0-9]+)/edit/$', views.GameModesEditView.as_view(), name='gamemodesEdit'),
    url(r'^gamemodes/(?P<pk>[0-9]+)/edit_change/$', views.editGameMode, name='editGameMode'),

    url(r'^achievements/$', views.AchievementsView.as_view(), name='achievements'),
    url(r'^achievements/create/$', views.createAchievement, name='createAchievement'),
    url(r'^achievements/(?P<pk>[0-9]+)/edit/$', views.AchievementsEditView.as_view(), name='achievementsEdit'),
    url(r'^achievements/(?P<pk>[0-9]+)/edit_change/$', views.editAchievement, name='editAchievement'),

    ### End Real Urls ###

    #######################

    ### Start Test Urls ###

    # ex: /api/
    # url(r'^$', views.index, name='index'),
    # ex: /api/test/
    # THIS ONE
    # url(r'^test/$', views.TestView.as_view(), name='test'),

    # ex: /api/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # THIS ONE
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex: /api/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # THIS ONE
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /api/5/vote/
    # THIS ONE
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


    ### End Test Urls ###
]