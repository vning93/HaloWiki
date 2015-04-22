from django.contrib import admin
from api.models import Character, Weapon, Map, Vehicle, Game, Game_Mode, Achievement, Weapon_Usable_On_Map, Vehicle_Usable_On_Map, Game_Mode_Playable_On_Map, Game_Playable_Game_Mode, Character_Appear_In_Game, Achievement_Unlockable_In_Game, Question, Choice
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

# Register your models here.

	### Start Real Admin ###

class CharacterResource(resources.ModelResource):

	class Meta:
		model = Character

class CharacterAdmin(ImportExportModelAdmin):
    list_display = ('name', 'current_status', 'home_world', 'gender', 'birth_date')
    search_fields = ['name', 'current_status', 'home_world', 'gender']
    resource_class = CharacterResource
    pass

class MapResource(resources.ModelResource):

	class Meta:
		model = Map

class MapAdmin(ImportExportModelAdmin):
	list_display = ('name', 'location', 'weapons')
	search_fields = ['name', 'location']
	resource_class = MapResource
	pass

class WeaponResource(resources.ModelResource):

	class Meta:
		model = Weapon

class WeaponAdmin(ImportExportModelAdmin):
	list_display = ('name', 'firing_mode', 'damage_level', 'dual_wield')
	resource_class = WeaponResource
	search_fields = ['name', 'firing_mode', 'damage_level', 'dual_wield']
	pass

class VehicleResource(resources.ModelResource):

	class Meta:
		model = Vehicle

class VehicleAdmin(ImportExportModelAdmin):
	list_display = ('name', 'model', 'vclass', 'num_users')
	search_fields = ['name', 'model', 'vclass', 'num_users']
	resource_class = VehicleResource
	pass

class GameResource(resources.ModelResource):

	class Meta:
		model = Game

class GameAdmin(ImportExportModelAdmin):
	list_display = ('name','year','developer','publisher','rating','platform')
	search_fields = ['name','year','developer','publisher','rating','platform']
	resource_class = GameResource
	pass

class Game_ModeResource(resources.ModelResource):

	class Meta:
		model = Game_Mode

class Game_ModeAdmin(ImportExportModelAdmin):
	list_display = ('name','multi_player','emblem')
	search_fields = ['name','multi_player','emblem']
	resource_class = Game_ModeResource
	pass

class AchievementResource(resources.ModelResource):

	class Meta:
		model = Achievement

class AchievementAdmin(ImportExportModelAdmin):
	list_display = ('name','criteria','emblem')
	search_fields = ['name','criteria','emblem']
	resource_class = AchievementResource
	pass

# Relational Tables #

class Weapon_Usable_On_MapAdmin(ImportExportModelAdmin):
	list_display = ('weapon','map')

class Vehicle_Usable_On_MapAdmin(ImportExportModelAdmin):
	list_display = ('vehicle','map')

class Game_Mode_Playable_On_MapAdmin(ImportExportModelAdmin):
	list_display = ('game_mode','map')

class Game_Playable_Game_ModeAdmin(ImportExportModelAdmin):
	list_display = ('game','game_mode')

class Character_Appear_In_GameAdmin(ImportExportModelAdmin):
	list_display = ('character','game')

class Achievement_Unlockable_In_GameAdmin(ImportExportModelAdmin):
	list_display = ('achievement','game')

# End Relational Tables #

admin.site.register(Character, CharacterAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Game_Mode, Game_ModeAdmin)
admin.site.register(Achievement, AchievementAdmin)
# Relational
admin.site.register(Weapon_Usable_On_Map, Weapon_Usable_On_MapAdmin)
admin.site.register(Vehicle_Usable_On_Map, Vehicle_Usable_On_MapAdmin)
admin.site.register(Game_Mode_Playable_On_Map, Game_Mode_Playable_On_MapAdmin)
admin.site.register(Game_Playable_Game_Mode, Game_Playable_Game_ModeAdmin)
admin.site.register(Character_Appear_In_Game, Character_Appear_In_GameAdmin)
admin.site.register(Achievement_Unlockable_In_Game, Achievement_Unlockable_In_GameAdmin)

    ### End Real Admin ###

    #######################

    ### Start Test Admin ###

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('question_text', 'pub_date', 'was_published_recently')

# admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)

	### End Test Admin ###