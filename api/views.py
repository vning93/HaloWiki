from django.shortcuts import render, render_to_response, RequestContext, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from api.models import Character, Weapon, Map, Vehicle, Game, Game_Mode, Achievement, Weapon_Usable_On_Map, Vehicle_Usable_On_Map, Game_Mode_Playable_On_Map, Game_Playable_Game_Mode, Character_Appear_In_Game, Achievement_Unlockable_In_Game, Question, Choice
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
from datetime import datetime
from django.db import connection
from django.db import models

# Create your views here.

### Start Real Views ###

class IndexView(TemplateView):
	template_name = "api/index.html"

class LevelsView(generic.ListView):
    # model = Map
    model = Map(Map.objects.raw('SELECT * FROM api_map'))
    template_name = "api/levels.html"

    def get_context_data(self, **kwargs):
        ctx = super(LevelsView, self).get_context_data(**kwargs)
        ctx['weapons_list'] = Weapon.objects.raw('SELECT * FROM api_weapon')
        ctx['vehicles_list'] = Vehicle.objects.raw('SELECT * FROM api_vehicle')
        ctx['game_modes_list'] = Game_Mode.objects.raw('SELECT * FROM api_game_mode')
        ctx['maps_list'] = Map.objects.raw('SELECT * FROM api_map')
        return ctx

class LevelsEditView(generic.DetailView):
    model = Map(Map.objects.raw('SELECT * FROM api_map'))
    template_name = 'api/levels_edit.html'

    def get_context_data(self, **kwargs):
        ctx = super(LevelsEditView, self).get_context_data(**kwargs)
        ctx['weapons_list'] = Weapon.objects.raw('SELECT * FROM api_weapon')
        ctx['vehicles_list'] = Vehicle.objects.raw('SELECT * FROM api_vehicle')
        ctx['game_modes_list'] = Game_Mode.objects.raw('SELECT * FROM api_game_mode')
        ctx['maps_list'] = Map.objects.raw('SELECT * FROM api_map')
        return ctx

class CharactersView(generic.ListView):
    model = Character(Character.objects.raw('SELECT * FROM api_character'))
    template_name = "api/characters.html"

class CharactersEditView(generic.DetailView):
    model = Character(Character.objects.raw('SELECT * FROM api_character'))
    template_name = 'api/characters_edit.html'

class WeaponsView(generic.ListView):
    model = Weapon(Weapon.objects.raw('SELECT * FROM api_weapon'))
    template_name = "api/weapons.html"

class WeaponsEditView(generic.DetailView):
    model = Weapon(Weapon.objects.raw('SELECT * FROM api_weapon'))
    template_name = 'api/weapons_edit.html'

class VehiclesView(generic.ListView):
    model = Vehicle(Vehicle.objects.raw('SELECT * FROM api_vehicle'))
    template_name = "api/vehicles.html"

class VehiclesEditView(generic.DetailView):
    model = Vehicle(Vehicle.objects.raw('SELECT * FROM api_vehicle'))
    template_name = 'api/vehicles_edit.html'

class GamesView(generic.ListView):
    model = Game(Game.objects.raw('SELECT * FROM api_game'))
    template_name = "api/games.html"

    def get_context_data(self, **kwargs):
        ctx = super(GamesView, self).get_context_data(**kwargs)
        ctx['games_list'] = Game.objects.raw('SELECT * FROM api_game')
        ctx['game_modes_list'] = Game_Mode.objects.raw('SELECT * FROM api_game_mode')
        ctx['characters_list'] = Character.objects.raw('SELECT * FROM api_character')
        ctx['achievements_list'] = Achievement.objects.raw('SELECT * FROM api_achievement')
        return ctx

class GamesEditView(generic.DetailView):
    model = Game(Game.objects.raw('SELECT * FROM api_game'))
    template_name = 'api/games_edit.html'

    def get_context_data(self, **kwargs):
        ctx = super(GamesEditView, self).get_context_data(**kwargs)
        ctx['games_list'] = Game.objects.raw('SELECT * FROM api_game')
        ctx['game_modes_list'] = Game_Mode.objects.raw('SELECT * FROM api_game_mode')
        ctx['characters_list'] = Character.objects.raw('SELECT * FROM api_character')
        ctx['achievements_list'] = Achievement.objects.raw('SELECT * FROM api_achievement')
        return ctx

class GameModesView(generic.ListView):
    model = Game_Mode(Game_Mode.objects.raw('SELECT * FROM api_game_mode'))
    template_name = "api/gamemodes.html"

class GameModesEditView(generic.DetailView):
    model = Game_Mode(Game_Mode.objects.raw('SELECT * FROM api_game_mode'))
    template_name = 'api/gamemodes_edit.html'

class AchievementsView(generic.ListView):
    model = Achievement(Achievement.objects.raw('SELECT * FROM api_achievement'))
    template_name = "api/achievements.html"

class AchievementsEditView(generic.DetailView):
    model = Achievement(Achievement.objects.raw('SELECT * FROM api_achievement'))
    template_name = 'api/achievements_edit.html'

def createMap(request, *args, **kwargs):
    try:
        new_name = request.POST['name']
        new_location = request.POST['location']

        new_map = Map(
            name = new_name,
            location = new_location
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_map (name, location) VALUES (%s, %s)', (new_name, new_location))

        # new_map.save()
        return HttpResponseRedirect("/levels/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createMapWeapon(request, *args, **kwargs):
    try:
        new_weapon = Weapon.objects.get(name=request.POST['weapon'])
        new_map = Map.objects.get(name=request.POST['map'])

        new_map_weapon = Weapon_Usable_On_Map(
            weapon = new_weapon,
            map = new_map
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_weapon_usable_on_map (map_id, weapon_id) VALUES (%s, %s)', (new_map.id, new_weapon.id))

        # new_map_weapon.save()
        return HttpResponseRedirect("/levels/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createMapVehicle(request, *args, **kwargs):
    try:
        new_vehicle = Vehicle.objects.get(name=request.POST['vehicle'])
        new_map = Map.objects.get(name=request.POST['map'])

        new_map_vehicle = Vehicle_Usable_On_Map(
            vehicle = new_vehicle,
            map = new_map
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_vehicle_usable_on_map (map_id, vehicle_id) VALUES (%s, %s)', (new_map.id, new_vehicle.id))

        # new_map_vehicle.save()
        return HttpResponseRedirect("/levels/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createMapGameMode(request, *args, **kwargs):
    try:
        new_game_mode = Game_Mode.objects.get(name=request.POST['game_mode'])
        new_map = Map.objects.get(name=request.POST['map'])

        new_map_game_mode = Game_Mode_Playable_On_Map(
            game_mode = new_game_mode,
            map = new_map
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_game_mode_playable_on_map (map_id, game_mode_id) VALUES (%s, %s)', (new_map.id, new_game_mode.id))

        # new_map_game_mode.save()
        return HttpResponseRedirect("/levels/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def editLevel(request, *args, **kwargs):
    try:
        this_level = Map.objects.get(name=request.POST['name'])

        this_level.name = request.POST['name']
        this_level.location = request.POST['location']

        cursor = connection.cursor()
        cursor.execute('UPDATE api_map SET location=%s WHERE name=%s', (this_level.location, this_level.name))

        # this_level.save()
        return HttpResponseRedirect("/levels/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createCharacter(request, *args, **kwargs):
    try:
        new_name = request.POST['name']
        new_current_status = request.POST['current_status']
        new_home_world = request.POST['home_world']
        new_gender = request.POST['gender']
        new_birth_date = datetime.strptime(request.POST['birth_date'], '%m-%d-%Y')

        new_character = Character(
            name = new_name,
            current_status = new_current_status,
            home_world = new_home_world,
            gender = new_gender,
            birth_date = new_birth_date
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_character (name, current_status, home_world, gender, birth_date) VALUES (%s, %s, %s, %s, %s)', (new_name, new_current_status, new_home_world, new_gender, new_birth_date))

        # new_character.save()
        return HttpResponseRedirect("/characters/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def editCharacter(request, *args, **kwargs):
    try:
        this_character = Character.objects.get(name=request.POST['name'])

        this_character.name = request.POST['name']
        this_character.current_status = request.POST['current_status']
        this_character.home_world = request.POST['home_world']
        this_character.gender = request.POST['gender']
        this_character.birth_date = datetime.strptime(request.POST['birth_date'], '%m-%d-%Y')

        cursor = connection.cursor()
        cursor.execute('UPDATE api_character SET current_status=%s, home_world=%s, gender=%s, birth_date=%s WHERE name=%s', (this_character.current_status, this_character.home_world, this_character.gender, this_character.birth_date, this_character.name))

        # this_character.save()
        return HttpResponseRedirect("/characters/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createWeapon(request, *args, **kwargs):
    try:
        new_name = request.POST['name']
        new_firing_mode = request.POST['firing_mode']
        new_damage_level = ("%.2f" % float(request.POST['damage_level']))
        new_dual_wield = int(request.POST['dual_wield'])
        # new_maps = request.POST['maps']
        new_weapon = Weapon(
            name = new_name,
            firing_mode = new_firing_mode,
            damage_level = new_damage_level,
            dual_wield = new_dual_wield
            # maps = request.POST['maps']
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_weapon (name, firing_mode, damage_level, dual_wield) VALUES (%s, %s, %s, %s)', (new_name, new_firing_mode, new_damage_level, new_dual_wield))

        # new_weapon.save()
        return HttpResponseRedirect("/weapons/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def editWeapon(request, *args, **kwargs):
    try:
        this_weapon = Weapon.objects.get(name=request.POST['name'])

        this_weapon.name = request.POST['name']
        this_weapon.firing_mode = request.POST['firing_mode']
        this_weapon.damage_level = ("%.2f" % float(request.POST['damage_level']))
        this_weapon.dual_wield = int(request.POST['dual_wield'])

        cursor = connection.cursor()
        cursor.execute('UPDATE api_weapon SET firing_mode=%s, damage_level=%s, dual_wield=%s WHERE name=%s', (this_weapon.firing_mode, this_weapon.damage_level, this_weapon.dual_wield, this_weapon.name))

        # this_weapon.save()
        return HttpResponseRedirect("/weapons/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createVehicle(request, *args, **kwargs):
    try:
        new_name = request.POST['name']
        new_model = request.POST['model']
        new_vclass = request.POST['vclass']
        new_num_users = request.POST['num_users']
        new_vehicle = Vehicle(
            name = new_name,
            model = new_model,
            vclass = new_vclass,
            num_users = new_num_users
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_vehicle (name, model, vclass, num_users) VALUES (%s, %s, %s, %s)', (new_name, new_model, new_vclass, new_num_users))

        # new_vehicle.save()
        return HttpResponseRedirect("/vehicles/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def editVehicle(request, *args, **kwargs):
    try:
        this_vehicle = Vehicle.objects.get(name=request.POST['name'])

        this_vehicle.name = request.POST['name']
        this_vehicle.model = request.POST['model']
        this_vehicle.vclass = request.POST['vclass']
        this_vehicle.num_users = request.POST['num_users']

        cursor = connection.cursor()
        cursor.execute('UPDATE api_vehicle SET model=%s, vclass=%s, num_users=%s WHERE name=%s', (this_vehicle.model, this_vehicle.vclass, this_vehicle.num_users, this_vehicle.name))

        # this_vehicle.save()
        return HttpResponseRedirect("/vehicles/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createGame(request, *args, **kwargs):
    try:
        new_name = request.POST['name']
        new_year = datetime.strptime(request.POST['year'], '%m-%d-%Y')
        new_developer = request.POST['developer']
        new_publisher = request.POST['publisher']
        new_rating = ("%.2f" % float(request.POST['rating']))
        new_platform = request.POST['platform']
        # new_game_modes = request.POST['game_modes']
        # new_characters = request.POST['characters']
        # new_achievements = request.POST['achievements']
        new_game = Game(
            name = new_name,
            year = new_year,
            developer = new_developer,
            publisher = new_publisher,
            rating = new_rating,
            platform = new_platform
            # game_modes = new_game_modes,
            # characters = new_characters,
            # achievements = new_achievements
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_game (name, year, developer, publisher, rating, platform) VALUES (%s, %s, %s, %s, %s, %s)', (new_name, new_year, new_developer, new_publisher, new_rating, new_platform))

        # new_game.save()
        return HttpResponseRedirect("/games/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createGamesGameMode(request, *args, **kwargs):
    try:
        new_game_mode = Game_Mode.objects.get(name=request.POST['game_mode'])
        new_game = Game.objects.get(name=request.POST['game'])

        new_game_game_mode = Game_Playable_Game_Mode(
            game_mode = new_game_mode,
            game = new_game
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_game_playable_game_mode (game_mode_id, game_id) VALUES (%s, %s)', (new_game_mode.id, new_game.id))

        # new_game_game_mode.save()
        return HttpResponseRedirect("/games/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createGamesCharacters(request, *args, **kwargs):
    try:
        new_character = Character.objects.get(name=request.POST['character'])
        new_game = Game.objects.get(name=request.POST['game'])

        new_game_character = Character_Appear_In_Game(
            character = new_character,
            game = new_game
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_character_appear_in_game (character_id, game_id) VALUES (%s, %s)', (new_character.id, new_game.id))

        # new_game_character.save()
        return HttpResponseRedirect("/games/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createGamesAchievements(request, *args, **kwargs):
    try:
        new_achievement = Achievement.objects.get(name=request.POST['achievement'])
        new_game = Game.objects.get(name=request.POST['game'])

        new_game_achievement = Achievement_Unlockable_In_Game(
            achievement = new_achievement,
            game = new_game
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_achievement_unlockable_in_game (achievement_id, game_id) VALUES (%s, %s)', (new_achievement.id, new_game.id))

        # new_game_achievement.save()
        return HttpResponseRedirect("/games/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def editGame(request, *args, **kwargs):
    try:
        this_game = Game.objects.get(name=request.POST['name'])

        this_game.name = request.POST['name']
        this_game.year = datetime.strptime(request.POST['year'], '%m-%d-%Y')
        this_game.developer = request.POST['developer']
        this_game.publisher = request.POST['publisher']
        this_game.rating = request.POST['rating']
        this_game.platform = request.POST['platform']

        cursor = connection.cursor()
        cursor.execute('UPDATE api_game SET year=%s, developer=%s, publisher=%s, rating=%s, platform=%s WHERE name=%s', (this_game.year, this_game.developer, this_game.publisher, this_game.rating, this_game.platform, this_game.name))

        # this_game.save()
        return HttpResponseRedirect("/games/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createGameMode(request, *args, **kwargs):
    try:
        new_name = request.POST['name']
        new_multi_player = int(request.POST['multi_player'])
        new_emblem = request.POST['emblem']
        new_game_mode = Game_Mode(
            name = new_name,
            multi_player = new_multi_player,
            emblem = new_emblem
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_game_mode (name, multi_player, emblem) VALUES (%s, %s, %s)', (new_name, new_multi_player, new_emblem))

        # new_game_mode.save()
        return HttpResponseRedirect("/gamemodes/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def editGameMode(request, *args, **kwargs):
    try:
        this_game_mode = Game_Mode.objects.get(name=request.POST['name'])

        this_game_mode.name = request.POST['name']
        this_game_mode.multi_player = request.POST['multi_player']
        this_game_mode.emblem = request.POST['emblem']

        cursor = connection.cursor()
        cursor.execute('UPDATE api_game_mode SET multi_player=%s, emblem=%s WHERE name=%s', (this_game_mode.multi_player, this_game_mode.emblem, this_game_mode.name))

        # this_game_mode.save()
        return HttpResponseRedirect("/gamemodes/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def createAchievement(request, *args, **kwargs):
    try:
        new_name = request.POST['name']
        new_criteria = request.POST['criteria']
        new_emblem = request.POST['emblem']
        new_achievement = Achievement(
            name = new_name,
            criteria = new_criteria,
            emblem = new_emblem
        )

        cursor = connection.cursor()
        cursor.execute('INSERT INTO api_achievement (name, criteria, emblem) VALUES (%s, %s, %s)', (new_name, new_criteria, new_emblem))

        # new_achievement.save()
        return HttpResponseRedirect("/achievements/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

def editAchievement(request, *args, **kwargs):
    try:
        this_achievement = Achievement.objects.get(name=request.POST['name'])

        this_achievement.name = request.POST['name']
        this_achievement.criteria = request.POST['criteria']
        this_achievement.emblem = request.POST['emblem']

        cursor = connection.cursor()
        cursor.execute('UPDATE api_achievement SET criteria=%s, emblem=%s WHERE name=%s', (this_achievement.criteria, this_achievement.emblem, this_achievement.name))

        # this_achievement.save()
        return HttpResponseRedirect("/achievements/")
    except KeyError as e:
        return Response({
            "detail": "Missing some fields with error: {}".format(e)
        }, status=status.HTTP_400_BAD_REQUEST)

### End Real Views ###

########################

### Start Test Views ###

# def index(request):
#     # return HttpResponse("Hello, world. You're at the api index.")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('api/index.html')
#     # output = ', '.join([p.question_text for p in latest_question_list])
#     # return HttpResponse(output)
#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     context = {'latest_question_list': latest_question_list}
#     # return HttpResponse(template.render(context))
#     return render(request, 'api/index.html', context)

class TestView(generic.ListView):
    template_name = 'api/test.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'api/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'api/detail.html'

# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'api/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'api/results.html'

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'api/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('api:results', args=(p.id,)))

### End Test Views ###