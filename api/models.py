from django.db import models
import datetime
from django.utils import timezone

# https://docs.djangoproject.com/en/1.7/ref/models/fields/

# Create your models here.

MALE = "MALE"
FEMALE = "FEMALE"
GENDER_CHOICES = (
	(MALE, "Male"),
	(FEMALE, "Female")
)

SEMI = "SEMI"
AUTOMATIC = "AUTOMATIC"
MELEE = "MELEE"
FIRING_MODE_CHOICES = (
	(SEMI, "Semi"),
	(AUTOMATIC, "Automatic"),
	(MELEE, "Melee")
)

### Start Real Models ###

class Character(models.Model):
    name = models.CharField(
    	max_length = 50,
    	unique = True
    )
    current_status = models.CharField(
    	max_length = 200,
    	default = '',
        blank = True,
        null = True
    )
    home_world = models.CharField(
    	max_length = 50,
    	default = '',
        blank = True,
        null = True
    )
    gender = models.CharField(
    	max_length = 10,
    	choices = GENDER_CHOICES
    )
    birth_date = models.DateTimeField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Weapon(models.Model):
	name = models.CharField(
		max_length = 50,
		unique = True
	)
	firing_mode = models.CharField(
		max_length = 10,
		choices = FIRING_MODE_CHOICES
	)
	damage_level = models.DecimalField(
		max_digits = 8,
		decimal_places = 2
	)
	dual_wield = models.BooleanField(
		default = False
	)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Map(models.Model):
    name = models.CharField(
    	max_length = 50,
    	unique = True
    )
    location = models.CharField(
    	max_length = 200,
    	default = '',
        blank = True,
        null = True
    )

    @property
    def weapons(self):
        weapons_set = Weapon_Usable_On_Map.objects.filter(map=self)
        return weapons_set

    @property
    def vehicles(self):
    	vehicles_set = Vehicle_Usable_On_Map.objects.filter(map=self)
    	return vehicles_set

    @property
    def game_modes(self):
    	game_modes_set = Game_Mode_Playable_On_Map.objects.filter(map=self)
    	return game_modes_set

 #    weapons = models.ManyToManyField(
	# 	Weapon,
	# 	through = 'Weapon_Usable_On_Map'
	# )

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Vehicle(models.Model):
	name = models.CharField(
		max_length = 50,
		unique = True
	)
	model = models.CharField(
		max_length = 50,
		default = '',
        blank = True,
        null = True
	)
	vclass = models.CharField(
		max_length = 25,
		default = '',
        blank = True,
        null = True
	)
	num_users = models.IntegerField()

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Game(models.Model):
	name = models.CharField(
		max_length = 50,
		unique = True
	)
	year = models.DateField(
		auto_now = False,
		auto_now_add = False
	)
	developer = models.CharField(
		max_length = 50,
		default = '',
        blank = True,
        null = True
	)
	publisher = models.CharField(
		max_length = 50,
		default = '',
        blank = True,
        null = True
	)
	rating = models.DecimalField(
		max_digits = 6,
		decimal_places = 2
	)
	platform = models.CharField(
		max_length = 50,
		default = '',
		blank = True,
		null = True
	)

	@property
	def game_modes(self):
		game_modes_set = Game_Playable_Game_Mode.objects.filter(game=self)
		return game_modes_set

	@property
	def characters(self):
		characters_set = Character_Appear_In_Game.objects.filter(game=self)
		return characters_set

	@property
	def achievements(self):
		achievements_set = Achievement_Unlockable_In_Game.objects.filter(game=self)
		return achievements_set

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Game_Mode(models.Model):
	name = models.CharField(
		max_length = 50,
		unique = True
	)
	multi_player = models.BooleanField(
		default = False
	)
	emblem = models.CharField(
		max_length = 30,
		default = '',
		blank = True,
		null = True
	)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Achievement(models.Model):
	name = models.CharField(
		max_length = 50,
		unique = True
	)
	criteria = models.CharField(
		max_length = 200,
		default = '',
		blank = True,
		null = True
	)
	emblem = models.CharField(
		max_length = 30,
		default = '',
		blank = True,
		null = True
	)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

# Many-To-Many Tables #

class Weapon_Usable_On_Map(models.Model):
    weapon = models.ForeignKey(
    	Weapon
    )
    map = models.ForeignKey(
    	Map
    )

    def __str__(self):              # __unicode__ on Python 2
		return '%s' % (self.weapon)

class Vehicle_Usable_On_Map(models.Model):
	vehicle = models.ForeignKey(
		Vehicle
	)
	map = models.ForeignKey(
		Map
	)

	def __str__(self):              # __unicode__ on Python 2
		return '%s' % (self.vehicle)

class Game_Mode_Playable_On_Map(models.Model):
	game_mode = models.ForeignKey(
		Game_Mode
	)
	map = models.ForeignKey(
		Map
	)

	def __str__(self):              # __unicode__ on Python 2
		return '%s' % (self.game_mode)

class Game_Playable_Game_Mode(models.Model):
	game = models.ForeignKey(
		Game
	)
	game_mode = models.ForeignKey(
		Game_Mode
	)

	def __str__(self):              # __unicode__ on Python 2
		return '%s' % (self.game_mode)

class Character_Appear_In_Game(models.Model):
	character = models.ForeignKey(
		Character
	)
	game = models.ForeignKey(
		Game
	)

	def __str__(self):
		return '%s' % (self.character)

class Achievement_Unlockable_In_Game(models.Model):
	achievement = models.ForeignKey(
		Achievement
	)
	game = models.ForeignKey(
		Game
	)

	def __str__(self):
		return '%s' % (self.achievement)

### End Real Models ###

#########################

### Start Test Models ###

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

### End Test Models ###