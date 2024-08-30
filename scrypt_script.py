import os
import time
from dataclasses import dataclass, field
from enum import Enum, auto as enum_auto

from project_logger import (
    ProjectLogger,
    color_text,
    Color,
    Attribute,
    LOW_DEBUG,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    standard_file_format_string,
    standard_stream_format_string
)

logger = ProjectLogger(
    file_logger_name= __file__ + "_file", file_log_level= LOW_DEBUG, file_log_format_string= standard_file_format_string,
    file_filename= __file__ + ".log", file_max_size= 10 * 1024 * 1024, file_backup_count= 0,
    stream_logger_name= __file__ + "_stream", stream_log_level= DEBUG, stream_log_format_string= standard_stream_format_string
)

ENABLE_MOD_CONFIGS_CARD_LOGGING = True

class Tribe(Enum):
    REPTILE = enum_auto()
    INSECT = enum_auto()
    AVIAN = enum_auto()
    CANINE = enum_auto()
    HOOVED = enum_auto()
    SQUIRREL = enum_auto()

class Ability(Enum):
    ARMORED = 54
    MORSEL = 103
    DOUBLE_STRIKE = 100
    AIRBORN = 19
    ANNOYING = 76
    BELLIST = 75
    AMORPHOUS = 31
    TRINKET_BEARER = 29
    FROZEN_AWAY = 26
    RABBIT_HOLE = 1
    BEES_WITHIN = 2
    SPRINTER = 3
    TOUCH_OF_DEATH = 4
    FLEDGLING = 5
    DAM_BUILDER = 6
    HOARDER = 7
    BURROWER = 8
    FECUNDITY = 9
    LOOSE_TAIL = 10
    CORPSE_EATER = 11
    BONE_KING = 12
    WATERBORNE = 13
    UNKILLABLE = 14
    SHARP_QUILLS = 15
    HEAFTY = 16
    ANT_SPAWNER = 17
    GUARDIAN = 18
    MANY_LIVES = 20
    REPULSIVE = 21
    WORTHY_SACRIFICE = 22
    MIGHTY_LEAP = 23
    BIFURCATED = 24
    TRIFURCATED = 25
    STINKY = 83
    OMNI_STRIKE = 33
    LEADER = 34
    RAMPAGER = 102
    BONE_DIGGER = 28
    WATERBORNE_TENTACLE = 89
    SCAVENGER = 101
    BLOODLUST = 104
    BROODPARASITE = 99

class Decal(Enum):
    BLOOD_2 = "decal_blood_2"
    FUNGUS = "decal_fungus"
    STITCHES = "decal_stitches"
    DECAL_PAINT_2 = "decal_paint_2"
    DECAL_PAINT_3 = "decal_paint_3"
    DECAL_BLOOD_3 = "decal_blood_3"
    DECAL_BLOOD_4 = "decal_blood_4"

@dataclass
class CardModConfig:

    replacement_name : str = 'null'
    attack_adjustment : int = 0
    health_adjustment : int = 0
    abilities : list[Ability] = field(default_factory= list)
    negate_abilities : list[int] = field(default_factory= list)
    blood_cost_adjustment : int = 0
    bones_cost_adjustment : int = 0
    energy_cost_adjustment : int = 0
    nullify_gems_cost : bool = False
    add_gem_cost : list[str] = field(default_factory= list)
    gemify : bool = False
    special_abilities : list[str] = field(default_factory= list)
    stat_icon : int = 0
    from_card_merge : bool = False
    from_duplicate_merge : bool = False
    from_totem : bool = False
    from_latch : bool = False
    from_overclock : bool = False
    side_deck_mod : bool = False
    non_copyable : bool = False
    from_evolve : bool = False
    transformer_beast_card_id : str = 'null'
    death_card_info : str = 'null'
    bounty_hunter_info : str = 'null'
    build_a_card_portrait_info : str = 'null'
    decal_ids : list[Decal] = field(default_factory= list)

    def __str__(self) -> str:
        return f"Attk: {'+' if self.attack_adjustment > 0 else ''}{self.attack_adjustment}, Health: {'+' if self.health_adjustment > 0 else ''}{self.health_adjustment}"

@dataclass
class BaseStats:
    display_name : str
    attack : int
    health : int
    tribes : list[Tribe]
    rare : bool = False
    blood_cost : int = 0
    bone_cost : int = 0
    abilities : list[Ability] = field(default_factory= list)

    def __str__(self) -> str:
        return f"[{self.display_name}] A: {self.attack} H: {self.health} Rare: {self.rare} Tribes: {self.tribes} Abilities: {self.abilities}"

class Creatures(Enum):

    AMOEBA = "Amoeba"
    STATIC_GLITCH = "!STATIC!GLITCH"
    PELTLICE = "Lice"
    CAT = "Cat"
    URAYULI = "Urayuli"
    OUROBOROS = "Ouroboros"
    MANTISGOD = "MantisGod"
    SQUIRREL = "Squirrel"
    WOLFCUB = "WolfCub"
    PORCUPINE = "Porcupine"
    COYOTE = "Coyote"
    STOAT = "Stoat"
    WOLF = "Wolf"
    SKUNK = "Skunk"
    PRONGHORN = "Pronghorn"
    RINGWORM = "RingWorm"
    TREE = "Tree"
    SPARROW = "Sparrow"
    BULLFROG = "Bullfrog"
    BOULDER = "Boulder"
    SMOKE = "Smoke"
    MULE = "Mule"
    BEEHIVE = "Beehive"
    BEE = "Bee"
    MANTIS = "Mantis"
    GOLDNUGGET = "GoldNugget"
    BLOODHOUND = "Bloodhound"
    VULTURE = "Vulture"
    RAVENEGG = "RavenEgg"
    GECK = "Geck"
    RAVEN = "Raven"
    MOLE = "Mole"
    COCKROACH = "Cockroach"
    ALPHA = "Alpha"
    PACKRAT = "PackRat"
    ANT = "Ant"
    ANTQUEEN = "AntQueen"
    SKINK = "Skink"
    ADDER = "Adder"
    KINGFISHER = "Kingfisher"
    BAITBUCKET = "BaitBucket"
    TREE_SNOWCOVERED = "Tree_SnowCovered"
    ELKCUB = "ElkCub"
    MAGGOTS = "Maggots"
    TRAPFROG = "TrapFrog"
    TRAP = "Trap"
    SHARK = "Shark"
    MOLEMAN = "MoleMan"
    MOTHMAN = "Mothman_Stage1"
    AMALGAM = "Amalgam"
    STUMP = "Stump"
    GIANTCARD_MOON = "!GIANTCARD_MOON"
    TAIL_INSECT = "Tail_Insect"
    PELTHARE = "PeltHare"
    MOOSE = "Moose"
    RABBIT = "Rabbit"
    RATTLER = "Rattler"
    SNAPPER = "Snapper"
    SQUIDBELL = "SquidBell"
    DEFAULTTAIL = "DefaultTail"
    LONG_ELK = "Snelk"
    GOAT = "Goat"
    ELK = "Elk"
    BULL = "Bull"
    BAT = "Bat"
    GRIZZLY = "Grizzly"
    ANTFLYING = "AntFlying"
    PELTGOLDEN = "PeltGolden"
    FROZENOPOSSUM = "FrozenOpossum"
    OPOSSUM = "Opossum"
    PELTWOLF = "PeltWolf"
    SQUIDCARDS = "SquidCards"
    DAM = "Dam"
    MUDTURTLE = "MudTurtle"
    RATKING = "RatKing"
    OTTER = "Otter"
    FIELDMOUSE = "FieldMouse"
    TAIL_BIRD = "Tail_Bird"
    JERSEYDEVIL = "JerseyDevil"
    DAUS = "Daus"
    DAUSBELL = "DausBell"
    TAIL_FURRY = "Tail_Furry"
    SQUIDMIRROR = "SquidMirror"
    DIREWOLF = "DireWolf"
    MEALWORM = "MealWorm"
    KRAKEN = "Kraken"
    RACCOON = "Raccoon"
    DIREWOLFPUP = "DireWolfCub"
    WOLVERINE = "Wolverine"
    LAMMERGEIER = "Lammergeier"
    MAGPIE = "Magpie"
    REDHART = "RedHart"
    TADPOLE = "Tadpole"
    SKINKTAIL = "SkinkTail"
    AQUASQUIRREL = "AquaSquirrel"
    HYDRAEGG = "HydraEgg"
    STARVATION = "Starvation"
    CUCKOO = "Cuckoo"
    SNELK_NECK = "Snelk_Neck"
    MOLESEAMAN = "MoleSeaman"
    GIANTCARD_SHIP = "!GIANTCARD_SHIP"
    SKELETONPIRATE = "SkeletonPirate"
    WARREN = "Warren"
    HODAG = "Hodag"
    BEAVER = "Beaver"
    IJIRAQ = "Ijiraq"
    HYDRA = "Hydra"


base_stat_dict = {
    Creatures.HYDRA : BaseStats(
        display_name= "Hydra",
        attack= 1,
        health= 5,
        bone_cost= 1,
        rare= True,
        tribes= [t for t in Tribe if t is not Tribe.SQUIRREL],
        abilities= [Ability.BIFURCATED, Ability.TRIFURCATED]
    ),
    Creatures.IJIRAQ : BaseStats(
        display_name= "Ijiraq",
        attack= 4,
        health= 1,
        blood_cost= 0,
        rare= True,
        tribes= [],
        abilities= [Ability.REPULSIVE]
    ),
    Creatures.MANTISGOD : BaseStats(
        display_name= "Mantis God",
        attack= 1,
        health= 1,
        blood_cost= 1,
        rare= True,
        tribes= [Tribe.INSECT],
        abilities= [Ability.TRIFURCATED]
    ),
    Creatures.AMOEBA : BaseStats(
        display_name= "Amoeba",
        attack= 1,
        health= 2,
        rare= True,
        tribes= [],
        bone_cost= 2,
        abilities= [Ability.AMORPHOUS]
    ),
    Creatures.STATIC_GLITCH : BaseStats(
        display_name= "Static Glitch",
        attack= 1,
        health= 1,
        tribes= [],
        blood_cost= 1,
        abilities= []
    ),
    Creatures.PELTLICE : BaseStats(
        display_name= "Pelt Lice",
        attack= 1,
        health= 1,
        rare= False,
        tribes= [],
        blood_cost= 4,
        abilities= [Ability.DOUBLE_STRIKE]
    ),
    Creatures.CAT : BaseStats(
        display_name= "Cat",
        attack= 0,
        health= 1,
        tribes= [],
        blood_cost= 1,
        abilities= [Ability.MANY_LIVES]
    ),
    Creatures.URAYULI : BaseStats(
        display_name= "Urayuli",
        attack= 7,
        health= 7,
        rare= True,
        tribes= [],
        blood_cost= 4,
        abilities= []
    ),
    Creatures.OUROBOROS : BaseStats(
        display_name= "Ouroboros",
        attack= 1,
        health= 1,
        rare= True,
        tribes= [Tribe.REPTILE],
        blood_cost= 2,
        abilities= [Ability.UNKILLABLE]
    ),
    Creatures.SQUIRREL : BaseStats(
        display_name= "Squirrel",
        attack= 0,
        health= 1,
        tribes= [Tribe.SQUIRREL],
        abilities= []
    ),
    Creatures.WOLFCUB : BaseStats(
        display_name= "Wolf Cub",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.CANINE],
        abilities= [Ability.FLEDGLING]
    ),
    Creatures.PORCUPINE : BaseStats(
        display_name= "Porcupine",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.SHARP_QUILLS]
    ),
    Creatures.COYOTE : BaseStats(
        display_name= "Coyote",
        attack= 2,
        health= 1,
        bone_cost= 4,
        tribes= [Tribe.CANINE],
        abilities= []
    ),
    Creatures.STOAT : BaseStats(
        display_name= "Stoat",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.WOLF : BaseStats(
        display_name= "Wolf",
        attack= 3,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.CANINE],
        abilities= []
    ),
    Creatures.SKUNK : BaseStats(
        display_name= "Skunk",
        attack= 0,
        health= 3,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.STINKY]
    ),
    Creatures.PRONGHORN : BaseStats(
        display_name= "Pronghorn",
        attack= 1,
        health= 3,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER, Ability.BIFURCATED]
    ),
    Creatures.RINGWORM : BaseStats(
        display_name= "Ringworm",
        attack= 0,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= []
    ),
    Creatures.TREE : BaseStats(
        display_name= "Tree?",
        attack= 0,
        health= 4,
        tribes= [],
        abilities= []
    ),
    Creatures.SPARROW : BaseStats(
        display_name= "Sparrow",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creatures.BULLFROG : BaseStats(
        display_name= "Bullfrog",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creatures.BOULDER : BaseStats(
        display_name= "Boulder",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.SMOKE : BaseStats(
        display_name= "The Smoke",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= [Ability.BONE_KING]
    ),
    Creatures.MULE : BaseStats(
        display_name= "Pack Mule",
        attack= 0,
        health= 5,
        tribes= [],
        abilities= [Ability.SPRINTER]
    ),
    Creatures.BEEHIVE : BaseStats(
        display_name= "Beehive",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= [Ability.BEES_WITHIN]
    ),
    Creatures.BEE : BaseStats(
        display_name= "Bee",
        attack= 1,
        health= 1,
        blood_cost= 0,
        tribes= [Tribe.INSECT],
        abilities= [Ability.AIRBORN]
    ),
    Creatures.MANTIS : BaseStats(
        display_name= "Mantis",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= [Ability.BIFURCATED]
    ),
    Creatures.GOLDNUGGET : BaseStats(
        display_name= "Nugget",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.BLOODHOUND : BaseStats(
        display_name= "Bloodhound",
        attack= 2,
        health= 3,
        blood_cost= 2,
        tribes= [Tribe.CANINE],
        abilities= [Ability.GUARDIAN]
    ),
    Creatures.VULTURE : BaseStats(
        display_name= "Turkey Vulture",
        attack= 3,
        health= 3,
        bone_cost= 8,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creatures.RAVENEGG : BaseStats(
        display_name= "Raven Egg",
        attack= 0,
        health= 2,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.FLEDGLING]
    ),
    Creatures.GECK : BaseStats(
        display_name= "Geck",
        attack= 1,
        health= 1,
        rare= True,
        blood_cost= 0,
        tribes= [Tribe.REPTILE],
        abilities= []
    ),
    Creatures.RAVEN : BaseStats(
        display_name= "Raven",
        attack= 2,
        health= 3,
        blood_cost= 2,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creatures.MOLE : BaseStats(
        display_name= "Mole",
        attack= 0,
        health= 4,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.BURROWER]
    ),
    Creatures.COCKROACH : BaseStats(
        display_name= "Cockroach",
        attack= 1,
        health= 1,
        bone_cost= 4,
        tribes= [Tribe.INSECT],
        abilities= [Ability.UNKILLABLE]
    ),
    Creatures.ALPHA : BaseStats(
        display_name= "Alpha",
        attack= 1,
        health= 2,
        tribes= [Tribe.CANINE],
        bone_cost= 4,
        abilities= [Ability.LEADER]
    ),
    Creatures.PACKRAT : BaseStats(
        display_name= "Pack Rat",
        attack= 2,
        health= 2,
        rare= True,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.TRINKET_BEARER]
    ),
    Creatures.ANT : BaseStats(
        display_name= "Worker Ant",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= []
    ),
    Creatures.ANTQUEEN : BaseStats(
        display_name= "Ant Queen",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.INSECT],
        abilities= [Ability.ANT_SPAWNER]
    ),
    Creatures.SKINK : BaseStats(
        display_name= "Skink",
        attack= 1,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.LOOSE_TAIL]
    ),
    Creatures.ADDER : BaseStats(
        display_name= "Adder",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.TOUCH_OF_DEATH]
    ),
    Creatures.KINGFISHER : BaseStats(
        display_name= "Kingfisher",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.WATERBORNE, Ability.AIRBORN]
    ),
    Creatures.BAITBUCKET : BaseStats(
        display_name= "Bait Bucket",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.TREE_SNOWCOVERED : BaseStats(
        display_name= "Snowy Tree?",
        attack= 0,
        health= 3,
        tribes= [],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creatures.ELKCUB : BaseStats(
        display_name= "Elk Fawn",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER, Ability.FLEDGLING]
    ),
    Creatures.MAGGOTS : BaseStats(
        display_name= "Corpse Maggots",
        attack= 1,
        health= 1,
        bone_cost= 5,
        tribes= [Tribe.INSECT],
        abilities= [Ability.CORPSE_EATER]
    ),
    Creatures.TRAPFROG : BaseStats(
        display_name= "Strange Frog",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creatures.TRAP : BaseStats(
        display_name= "Trap",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creatures.SHARK : BaseStats(
        display_name= "Great White",
        attack= 4,
        health= 2,
        blood_cost= 3,
        tribes= [],
        abilities= [Ability.WATERBORNE]
    ),
    Creatures.MOLEMAN : BaseStats(
        display_name= "Moleman",
        attack= 0,
        health= 6,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.BURROWER, Ability.MIGHTY_LEAP]
    ),
    Creatures.MOTHMAN : BaseStats(
        display_name= "Strange Larva",
        attack= 0,
        health= 3,
        blood_cost= 1,
        rare= True,
        tribes= [Tribe.INSECT],
        abilities= [Ability.FLEDGLING]
    ),
    Creatures.AMALGAM : BaseStats(
        display_name= "Amalgam",
        attack= 3,
        health= 3,
        rare= True,
        tribes= [t for t in Tribe],
        blood_cost= 2,
        abilities= []
    ),
    Creatures.STUMP : BaseStats(
        display_name= "Stump",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.GIANTCARD_MOON : BaseStats(
        display_name= "The Moon",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.TAIL_INSECT : BaseStats(
        display_name= "Insect Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.PELTHARE : BaseStats(
        display_name= "Rabbit Pelt",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.MOOSE : BaseStats(
        display_name= "Moose Buck",
        attack= 3,
        health= 7,
        blood_cost= 3,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.HEAFTY]
    ),
    Creatures.RABBIT : BaseStats(
        display_name= "Rabbit",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.RATTLER : BaseStats(
        display_name= "Rattler",
        attack= 3,
        health= 1,
        bone_cost= 6,
        tribes= [Tribe.REPTILE],
        abilities= []
    ),
    Creatures.SNAPPER : BaseStats(
        display_name= "River Snapper",
        attack= 1,
        health= 6,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= []
    ),
    Creatures.SQUIDBELL : BaseStats(
        display_name= "Squid (Bell)",
        attack= 1,
        health= 3,
        blood_cost= 2,
        tribes= [],
        abilities= []
    ),
    Creatures.DEFAULTTAIL : BaseStats(
        display_name= "Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.LONG_ELK : BaseStats(
        display_name= "Long Elk",
        attack= 1,
        health= 2,
        bone_cost= 4,
        rare= True,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER, Ability.TOUCH_OF_DEATH]
    ),
    Creatures.GOAT : BaseStats(
        display_name= "Black Goat",
        attack= 0,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.WORTHY_SACRIFICE]
    ),
    Creatures.ELK : BaseStats(
        display_name= "Elk",
        attack= 2,
        health= 4,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER]
    ),
    Creatures.BULL : BaseStats(
        display_name= "Wild Bull",
        attack= 3,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.RAMPAGER]
    ),
    Creatures.BAT : BaseStats(
        display_name= "Bat",
        attack= 2,
        health= 1,
        bone_cost= 4,
        tribes= [],
        abilities= [Ability.AIRBORN]
    ),
    Creatures.GRIZZLY : BaseStats(
        display_name= "Grizzly",
        attack= 4,
        health= 6,
        blood_cost= 3,
        tribes= [],
        abilities= []
    ),
    Creatures.ANTFLYING : BaseStats(
        display_name= "Flying Ant",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= [Ability.AIRBORN]
    ),
    Creatures.PELTGOLDEN : BaseStats(
        display_name= "Golden Pelt",
        attack= 0,
        health= 3,
        blood_cost= 0,
        tribes= [],
        abilities= []
    ),
    Creatures.FROZENOPOSSUM : BaseStats(
        display_name= "Frozen Opossum",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= [Ability.FROZEN_AWAY]
    ),
    Creatures.OPOSSUM : BaseStats(
        display_name= "Opossum",
        attack= 1,
        health= 1,
        bone_cost= 2,
        tribes= [],
        abilities= []
    ),
    Creatures.PELTWOLF : BaseStats(
        display_name= "Wolf Pelt",
        attack= 0,
        health= 2,
        tribes= [],
        abilities= []
    ),
    Creatures.SQUIDCARDS : BaseStats(
        display_name= "Squid (Cards)",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.DAM : BaseStats(
        display_name= "Dam",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.MUDTURTLE : BaseStats(
        display_name= "Mud Turtle",
        attack= 2,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.ARMORED]
    ),
    Creatures.RATKING : BaseStats(
        display_name= "Rat King",
        attack= 2,
        health= 1,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.BONE_KING]
    ),
    Creatures.OTTER : BaseStats(
        display_name= "River Otter",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.WATERBORNE]
    ),
    Creatures.FIELDMOUSE : BaseStats(
        display_name= "Field Mice",
        attack= 2,
        health= 2,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.FECUNDITY]
    ),
    Creatures.TAIL_BIRD : BaseStats(
        display_name= "Bird Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.JERSEYDEVIL : BaseStats(
        display_name= "Child 13",
        attack= 1,
        health= 1,
        rare= True,
        blood_cost= 1,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.MANY_LIVES]
    ),
    Creatures.DAUS : BaseStats(
        display_name= "The Daus",
        attack= 2,
        health= 2,
        blood_cost= 2,
        rare= True,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.BELLIST]
    ),
    Creatures.DAUSBELL : BaseStats(
        display_name= "Chime",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.TAIL_FURRY : BaseStats(
        display_name= "Furry Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.SQUIDMIRROR : BaseStats(
        display_name= "Squid (Mirro)",
        attack= 1,
        health= 3,
        blood_cost= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.DIREWOLF : BaseStats(
        display_name= "Dire Wolf",
        attack= 2,
        health= 5,
        blood_cost= 3,
        tribes= [Tribe.CANINE],
        abilities= [Ability.DOUBLE_STRIKE]
    ),
    Creatures.MEALWORM : BaseStats(
        display_name= "Mealworm",
        attack= 0,
        health= 2,
        bone_cost= 2,
        tribes= [Tribe.INSECT],
        abilities= [Ability.MORSEL]
    ),
    Creatures.KRAKEN : BaseStats(
        display_name= "Great Kraken",
        attack= 1,
        health= 1,
        blood_cost= 1,
        rare= True,
        tribes= [],
        abilities= [Ability.WATERBORNE_TENTACLE]
    ),
    Creatures.RACCOON : BaseStats(
        display_name= "Raccoon",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.SCAVENGER]
    ),
    Creatures.DIREWOLFPUP : BaseStats(
        display_name= "Dire Wolf Pup",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.CANINE],
        abilities= [Ability.BONE_DIGGER, Ability.FLEDGLING]
    ),
    Creatures.WOLVERINE : BaseStats(
        display_name= "Wolverine",
        attack= 1,
        health= 3,
        bone_cost= 5,
        tribes= [],
        abilities= []
    ),
    Creatures.LAMMERGEIER : BaseStats(
        display_name= "Lammergeier",
        attack= 1,
        health= 4,
        blood_cost= 3,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creatures.MAGPIE : BaseStats(
        display_name= "Magpie",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.HOARDER, Ability.AIRBORN]
    ),
    Creatures.REDHART : BaseStats(
        display_name= "Redhart",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER]
    ),
    Creatures.TADPOLE : BaseStats(
        display_name= "Tadpole",
        attack= 0,
        health= 1,
        blood_cost= 0,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.WATERBORNE, Ability.FLEDGLING]
    ),
    Creatures.SKINKTAIL : BaseStats(
        display_name= "Skink Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.AQUASQUIRREL : BaseStats(
        display_name= "Aqua Squirrel",
        attack= 1,
        health= 1,
        tribes= [Tribe.SQUIRREL],
        abilities= []
    ),
    Creatures.HYDRAEGG : BaseStats(
        display_name= "Hydra Egg",
        attack= 1,
        health= 1,
        bone_cost= 1,
        rare= True,
        tribes= [],
        abilities= []
    ),
    Creatures.STARVATION : BaseStats(
        display_name= "Starvation",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.CUCKOO : BaseStats(
        display_name= "Cuckoo",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.BROODPARASITE]
    ),
    Creatures.SNELK_NECK : BaseStats(
        display_name= "Vertebrae",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.MOLESEAMAN : BaseStats(
        display_name= "Mole Seaman",
        attack= 1,
        health= 8,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.BURROWER, Ability.MIGHTY_LEAP]
    ),
    Creatures.GIANTCARD_SHIP : BaseStats(
        display_name= "The Limonchello",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.SKELETONPIRATE : BaseStats(
        display_name= "Skeleton Pirate",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creatures.WARREN : BaseStats(
        display_name= "Warren",
        attack= 0,
        health= 2,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.RABBIT_HOLE]
    ),
    Creatures.HODAG : BaseStats(
        display_name= "Hodag",
        attack= 1,
        health= 5,
        blood_cost= 2,
        rare= True,
        tribes= [],
        abilities= []
    ),
    Creatures.BEAVER : BaseStats(
        display_name= "Beaver",
        attack= 1,
        health= 3,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.DAM_BUILDER]
    )
}

def clamp(input, low, high):
    ret = input
    if ret < low:
        return low
    if ret > high:
        return high
    return ret

standard_cards = [
    Creatures.AMOEBA,
    Creatures.PELTLICE,
    Creatures.CAT,
    Creatures.URAYULI,
    Creatures.OUROBOROS,
    Creatures.MANTISGOD,
    Creatures.SQUIRREL,
    Creatures.WOLFCUB,
    Creatures.PORCUPINE,
    Creatures.COYOTE,
    Creatures.STOAT,
    Creatures.WOLF,
    Creatures.SKUNK,
    Creatures.PRONGHORN,
    Creatures.RINGWORM,
    Creatures.SPARROW,
    Creatures.BULLFROG,
    Creatures.BEEHIVE,
    Creatures.BEE,
    Creatures.MANTIS,
    Creatures.BLOODHOUND,
    Creatures.VULTURE,
    Creatures.RAVENEGG,
    Creatures.GECK,
    Creatures.RAVEN,
    Creatures.MOLE,
    Creatures.COCKROACH,
    Creatures.ALPHA,
    Creatures.PACKRAT,
    Creatures.ANT,
    Creatures.ANTQUEEN,
    Creatures.SKINK,
    Creatures.ADDER,
    Creatures.KINGFISHER,
    Creatures.ELKCUB,
    Creatures.MAGGOTS,
    Creatures.SHARK,
    Creatures.MOLEMAN,
    Creatures.MOTHMAN,
    Creatures.AMALGAM,
    Creatures.PELTHARE,
    Creatures.MOOSE,
    Creatures.RABBIT,
    Creatures.RATTLER,
    Creatures.SNAPPER,
    Creatures.SQUIDBELL,
    Creatures.LONG_ELK,
    Creatures.GOAT,
    Creatures.ELK,
    Creatures.BULL,
    Creatures.BAT,
    Creatures.GRIZZLY,
    Creatures.ANTFLYING,
    Creatures.PELTGOLDEN,
    Creatures.FROZENOPOSSUM,
    Creatures.OPOSSUM,
    Creatures.PELTWOLF,
    Creatures.SQUIDCARDS,
    Creatures.MUDTURTLE,
    Creatures.RATKING,
    Creatures.OTTER,
    Creatures.FIELDMOUSE,
    Creatures.JERSEYDEVIL,
    Creatures.DAUS,
    Creatures.SQUIDMIRROR,
    Creatures.DIREWOLF,
    Creatures.MEALWORM,
    Creatures.KRAKEN,
    Creatures.RACCOON,
    Creatures.DIREWOLFPUP,
    Creatures.WOLVERINE,
    Creatures.LAMMERGEIER,
    Creatures.MAGPIE,
    Creatures.REDHART,
    Creatures.TADPOLE,
    Creatures.HYDRAEGG,
    Creatures.CUCKOO,
    Creatures.MOLESEAMAN,
    Creatures.WARREN,
    Creatures.HODAG,
    Creatures.BEAVER,
    Creatures.IJIRAQ,
    Creatures.HYDRA
]

rare_standard_cards = [c for c in standard_cards if base_stat_dict[c].rare]
not_rare_standard_cards = [c for c in standard_cards if c not in rare_standard_cards]

no_cost_standard_cards = [c for c in standard_cards if base_stat_dict[c].bone_cost == 0 and base_stat_dict[c].blood_cost == 0]
no_cost_rare_standard_cards = [c for c in standard_cards if base_stat_dict[c].bone_cost == 0 and base_stat_dict[c].blood_cost == 0 and base_stat_dict[c].rare]
no_cost_not_rare_standard_cards = [c for c in no_cost_standard_cards if c not in no_cost_rare_standard_cards]

blood_cost_standard_cards : list[list[Creatures]] = []
for blood_cost in range(1,5):
    blood_cost_standard_cards.append(
        [c for c in standard_cards if base_stat_dict[c].blood_cost == blood_cost]
    )

blood_cost_rare_standard_cards : list[list[Creatures]] = []
for blood_cost in range(1,5):
    blood_cost_rare_standard_cards.append(
        [c for c in rare_standard_cards if base_stat_dict[c].blood_cost == blood_cost]
    )

blood_cost_not_rare_standard_cards : list[list[Creatures]] = []
for blood_cost in range(1,5):
    blood_cost_not_rare_standard_cards.append(
        [c for c in not_rare_standard_cards if base_stat_dict[c].blood_cost == blood_cost]
    )

bone_cost_standard_cards : list[list[Creatures]] = []
for bone_cost in range(1,10):
    bone_cost_standard_cards.append(
        [c for c in standard_cards if base_stat_dict[c].bone_cost == bone_cost]
    )

bone_cost_rare_standard_cards : list[list[Creatures]] = []
for bone_cost in range(1,10):
    bone_cost_rare_standard_cards.append(
        [c for c in rare_standard_cards if base_stat_dict[c].bone_cost == bone_cost]
    )

bone_cost_not_rare_standard_cards : list[list[Creatures]] = []
for bone_cost in range(1,10):
    bone_cost_not_rare_standard_cards.append(
        [c for c in not_rare_standard_cards if base_stat_dict[c].bone_cost == bone_cost]
    )

class Card:

    def __init__(self, name : str) -> None:
        self.name = name
        self.creature = Creatures(name)
        self.base_stats = base_stat_dict[self.creature]
        self.attack = self.base_stats.attack
        self.health = self.base_stats.health
        self.blood_cost = 0
        self.bone_cost = 0
        self.mod_configs : list[CardModConfig] = []
        self.abilities : list[Ability] = self.base_stats.abilities
    
    def add_mod_config(self, mod_config : CardModConfig) -> None:
        self.mod_configs.append(mod_config)

        self.attack = sum([m.attack_adjustment for m in self.mod_configs]) + self.base_stats.attack
        self.health = sum([m.health_adjustment for m in self.mod_configs]) + self.base_stats.health
        self.blood_cost = sum([m.blood_cost_adjustment for m in self.mod_configs]) + self.base_stats.blood_cost
        self.bone_cost = sum([m.bones_cost_adjustment for m in self.mod_configs]) + self.base_stats.bone_cost

        self.abilities : list[Ability] = []
        for mc in self.mod_configs:
            for a in mc.abilities:
                self.abilities.append(a)
        self.abilities.extend(self.base_stats.abilities)
        
        self.abilities = list(set(self.abilities))
    
    def __str__(self) -> str:
        name_str = f"[{self.base_stats.display_name}]"
        
        if self.attack < 3:
            attack_color = Color.LIGHT_MAGENTA
        elif self.attack < 6:
            attack_color = Color.YELLOW
        else:
            attack_color = Color.LIGHT_GREEN
        attack_text = color_text(f"{self.attack:<3}", color= attack_color)

        if self.health < 3:
            health_color = Color.LIGHT_MAGENTA
        elif self.health < 6:
            health_color = Color.YELLOW
        else:
            health_color = Color.LIGHT_GREEN
        health_text = color_text(f"{self.health:<3}", color= health_color)

        msg = f'.{name_str:>20} Attack: {attack_text}, Health: {health_text}'        
        if self.base_stats.bone_cost:
            msg += f" {color_text('Bones', color= Color.BLACK, on_color= Color.WHITE)}: {self.bone_cost}, "
        else:
            msg += f" Blood: {self.blood_cost}, "

        msg += "Abilities:"
        if self.abilities:
            for a in self.abilities:
                msg += f' {a.name},'
            msg = msg[:-1]
        else:
            msg += " None"
        
        if ENABLE_MOD_CONFIGS_CARD_LOGGING:
            if self.mod_configs:
                msg+= "\n"
                for mc in self.mod_configs:
                    msg += f"\t{str(mc)}\n"
                msg = msg[:-1]

        return msg

def formatted_true_false(i : bool) -> str:
    if i:
        return 'true'
    else:
        return 'false'

def parse_text_between_things(s : str, first : str, second : str) -> str:

    logger.log(LOW_DEBUG, f"parsing string {s}")
    try:
        i1 = s.index(first)
        s2 = s[i1+len(first):]
        i2 = s2.index(second)
        s3 = s2[0 : i2]
    except:
        logger.log(level= ERROR, message= f"Could not parse text between '{first}' and '{second}' for string {s}")
        return 'error'
    
    return s3

def parse_mod_text(mod_text_lines : list[str], cards : list[Card]) -> None:

    logger.log(level= LOW_DEBUG, message= f'Parsing mod text')
    vol_card_index = -1
    card_index = 0
    parse_mod_text = False
    parsing_abilities = False
    parse_negate_abilities = False
    parse_add_gem_cost = False
    parse_special_abilities = False
    parse_decal_ids = False
    mod_config = CardModConfig()

    for line in mod_text_lines:
        logger.log(LOW_DEBUG, message= f"Parsing mod text line: {line[:-1]}")
        if line.startswith('                            "$k": '):
            card_name = parse_text_between_things(line, first= '"$k": "', second= '"')
            logger.log(LOW_DEBUG, message= f"Mod Config data for card name {card_name} detected")
            if "#" in card_name:
                s = card_name.split("#")
                card_name, card_dupe_num = s[0], int(s[1])
            else:
                card_dupe_num = 0
            logger.log(level= LOW_DEBUG, message= f'Parsed card name {card_name} and card duplicate number {card_dupe_num}')

            for i in range(0, card_dupe_num + 1):
                temp_cards_list = [c.name for c in cards[vol_card_index+ 1:]]
                vol_card_index = temp_cards_list.index(card_name)
                card_index += vol_card_index
                if i > 0:
                    card_index += 1
                logger.log(level= LOW_DEBUG, message= f'Card name {card_name} found at index {vol_card_index} in cards list {temp_cards_list}... primary list index {card_index}')
    
        if line.startswith('                                    {'):
            parse_mod_text = True
        
        if parse_mod_text:

            if line.startswith('                                        "nameReplacement":'):
                replacement_name = parse_text_between_things(line, first= " ", second= ",")
                if ': "' in replacement_name:
                    mod_config.replacement_name = parse_text_between_things(line, first= ': "', second= '"')

            if line.startswith('                                        "attackAdjustment":'):
                mod_config.attack_adjustment = int(parse_text_between_things(line, first= ": ", second= ","))

            if line.startswith('                                        "healthAdjustment":'):
                mod_config.health_adjustment = int(parse_text_between_things(line, first= ": ", second= ","))

            if line.startswith('                                        "abilities": {'):
                parsing_abilities = True

            if parsing_abilities:
                if line.startswith('                                                '):
                    if "," not in line:
                        ability_number = int(line.strip())
                    else:
                        ability_number = int(line.strip().split(",")[0])
                    mod_config.abilities.append(Ability(ability_number))

                if line.startswith('                                            ]'):
                    parsing_abilities = False


            if line.startswith('                                        "negateAbilities": {'):
                parse_negate_abilities = True

            if parse_negate_abilities:
                if line.startswith('                                                '):
                    if "," not in line:
                        ability_number = int(line.strip())
                    else:
                        ability_number = int(line.strip().split(",")[0])
                    mod_config.negate_abilities.append(ability_number)

                if line.startswith('                                            ]'):
                    parse_negate_abilities = False


            if "bloodCostAdjustment" in line:
                mod_config.blood_cost_adjustment = int(
                    parse_text_between_things(line.strip(), " ", ",")
                )
                logger.log(LOW_DEBUG, message= f"Blood Cost Adjustment for card name {card_name}: {mod_config.blood_cost_adjustment}")

            if line.startswith('                                        "bonesCostAdjustment":'):
                mod_config.bones_cost_adjustment = int(
                    parse_text_between_things(line.strip(), " ", ",")
                )
                logger.log(LOW_DEBUG, message= f"Bone Cost Adjustment for card name {card_name}: {mod_config.blood_cost_adjustment}")

            if line.startswith('                                        "energyCostAdjustment":'):
                mod_config.energy_cost_adjustment = int(
                    parse_text_between_things(line.strip(), " ", ",")
                )

            if line.startswith('                                        "nullifyGemsCost":'):
                mod_config.nullify_gems_cost = parse_text_between_things(line.strip(), " ", ",") == 'true'
            
            if line.startswith('                                        "addGemCost": {'):
                parse_add_gem_cost = True

            if parse_add_gem_cost:
                if line.startswith('                                                '):
                    if "," not in line:
                        gem_text = line.strip()
                    else:
                        gem_text = line.strip().split(",")[0]
                    mod_config.add_gem_cost.append(gem_text)

                if line.startswith('                                            ]'):
                    parse_add_gem_cost = False

            if line.startswith('                                        "gemify":'):
                mod_config.gemify = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "specialAbilities": {'):
                parse_special_abilities = True

            if parse_special_abilities:
                if line.startswith('                                                '):
                    if "," not in line:
                        special_abilities_text = line.strip()
                    else:
                        special_abilities_text = line.strip().split(",")[0]
                    mod_config.special_abilities.append(special_abilities_text)

                if line.startswith('                                            ]'):
                    parse_special_abilities = False


            if line.startswith('                                        "statIcon":'):
                mod_config.stat_icon = int(parse_text_between_things(line.strip(), " ", ","))

            if line.startswith('                                        "fromCardMerge":'):
                mod_config.from_card_merge = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "fromDuplicateMerge":'):
                mod_config.from_duplicate_merge = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "fromTotem":'):
                mod_config.from_totem = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "fromLatch":'):
                mod_config.from_latch = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "fromOverclock":'):
                mod_config.from_overclock = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "sideDeckMod":'):
                mod_config.side_deck_mod = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "nonCopyable":'):
                mod_config.non_copyable = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "fromEvolve":'):
                mod_config.from_evolve = parse_text_between_things(line.strip(), " ", ",") == 'true'

            if line.startswith('                                        "transformerBeastCardId":'):
                mod_config.transformer_beast_card_id = parse_text_between_things(line.strip(), " ", ",")

            if line.startswith('                                        "deathCardInfo":'):
                mod_config.death_card_info = parse_text_between_things(line.strip(), " ", ",")

            if line.startswith('                                        "bountyHunterInfo":'):
                mod_config.bounty_hunter_info = parse_text_between_things(line.strip(), " ", ",")

            if line.startswith('                                        "buildACardPortraitInfo":'):
                mod_config.build_a_card_portrait_info = parse_text_between_things(line.strip(), " ", ",")

            if line.startswith('                                        "decalIds": {'):
                parse_decal_ids = True

            if parse_decal_ids: 
                if line.startswith('                                                '):

                    decal_id_text = parse_text_between_things(line.strip(), '"', '"')
                    mod_config.decal_ids.append(Decal(decal_id_text))

                if line.startswith('                                            ]'):
                    parse_decal_ids = False


    cards[card_index].add_mod_config(mod_config)

def parse_save_file(save_file_path : str) -> list[Card]:
    ascension_init = False
    current_run_init = False
    card_ids_init = False
    card_mod_init = False
    capture_mod_card_text = False

    cards : list[Card] = []

    with open(save_file_path, 'r') as f:

        for line in f:
            line_stripped = line.strip()

            if line_stripped.startswith('"ascensionData"'):
                ascension_init = True
                logger.log(level= LOW_DEBUG, message= "Ascension detected")

            if ascension_init and line_stripped.startswith('"currentRun"'):
                current_run_init = True
                logger.log(level= LOW_DEBUG, message= "Current Run detected")

            if current_run_init and line.startswith("            },"):
                current_run_init = False
                card_ids_init = False
                card_mod_init = False
                logger.log(level= LOW_DEBUG, message= "Current Run parsing complete!")
            
            if current_run_init and line_stripped.startswith('"cardIds"'):
                card_ids_init = True
                logger.log(level= LOW_DEBUG, message= "Parsing cards...")

            if card_ids_init and line.startswith(' ' * 24):
                cards.append(Card(name = parse_text_between_things(line_stripped, '"', '"'))) # Text between quotes

            if card_ids_init and line_stripped.startswith("]"):
                card_ids_init = False
                logger.log(level= LOW_DEBUG, message= "All cards parsed")
            
            if current_run_init and line_stripped.startswith('"cardIdModInfos"'):
                card_mod_init = True
                logger.log(level= LOW_DEBUG, message= "Card Mods detected")
            
            if card_mod_init and line.startswith("                        {"):
                capture_mod_card_text = True
                capture_mod_lines : list[str] = []
                logger.log(level= LOW_DEBUG, message= "Parsing card mod...")
            
            if capture_mod_card_text:
                capture_mod_lines.append(line)
            
            if card_mod_init and line.startswith("                        }"):
                capture_mod_card_text = False
                parse_mod_text(mod_text_lines= capture_mod_lines, cards= cards)

            if current_run_init and line_stripped.startswith('"totems"'):
                totems_init = True
                logger.log(level= LOW_DEBUG, message= "Totems detected")
    
    return cards

def generate_mod_card_info(
    id : int,
    config : CardModConfig
) -> tuple[str, int]:
    
    # start
    
    ret_str = """                                    {
                                        "$id": """
    ret_str += str(id + 1)
    ret_str += ',\n'

    # Structure
    ret_str += """                                        "$type": 16,
                                        "singletonId": null,
                                        "nameReplacement": """
    
    # Name Replacement
    ret_str += config.replacement_name
    ret_str += ',\n'

    # Stat Adjustment
    ret_str += f'                                        "attackAdjustment": {config.attack_adjustment},\n'
    ret_str += f'                                        "healthAdjustment": {config.health_adjustment},\n'

    # Structure
    ret_str += """                                        "abilities": {
                                            "$id": """
    ret_str += str(id + 2)
    ret_str += ",\n"

    # Abilities
    ret_str += """                                            "$type": 7,
                                            "$rlength": """
    ret_str += str(len(config.abilities))
    ret_str += ",\n"

    ret_str += '                                            "$rcontent": [\n'

    for a in config.abilities:
        ret_str += f'                                                {a.value},\n'
    
    # Structure
    ret_str += """                                            ]
                                        },
                                        "negateAbilities": {
                                            "$id": """
    ret_str += str(id + 3)
    ret_str += ',\n'

    # Negate Abilities
    ret_str += """                                            "$type": 7,
                                            "$rlength": """
    ret_str += str(len(config.negate_abilities))
    ret_str += ",\n"

    ret_str += '                                            "$rcontent": [\n'

    for a in config.negate_abilities:
        ret_str += f'                                                {a},\n'

    # Structure
    ret_str += """                                            ]
                                        },\n"""

    # Cost Adjustment
    ret_str += f'                                        "bloodCostAdjustment": {config.blood_cost_adjustment},\n'
    ret_str += f'                                        "bonesCostAdjustment": {config.bones_cost_adjustment},\n'
    ret_str += f'                                        "energyCostAdjustment": {config.energy_cost_adjustment},\n'
    ret_str += f'                                        "nullifyGemsCost": {formatted_true_false(config.nullify_gems_cost)},\n'
    
    # Structure
    ret_str += """                                        "addGemCost": {
                                            "$id": """
    ret_str += str(id + 4)
    ret_str += ',\n'

    # Gem Cost
    ret_str += """                                            "$type": 17,
                                            "$rlength": """
    ret_str += str(len(config.add_gem_cost))
    ret_str += ',\n'

    ret_str += '                                            "$rcontent": [\n'

    for a in config.add_gem_cost:
        ret_str += f'                                                {a},\n'

    # Gemify
    ret_str += """                                            ]
                                        },
                                        "gemify": """
    ret_str += formatted_true_false(config.gemify)
    ret_str += ',\n'

    # Structure
    ret_str += """                                        "specialAbilities": {
                                            "$id": """
    ret_str += str(id + 5)
    ret_str += ',\n'

    # Special Abilities
    ret_str += """                                            "$type": 18,
                                            "$rlength": """
    ret_str += str(len(config.special_abilities))
    ret_str += ',\n'

    ret_str += '                                            "$rcontent": [\n'

    for a in config.special_abilities:
        ret_str += f'                                                {a},\n'

    # Structure
    ret_str += """                                            ]
                                        },\n"""

    # Stat Icon ??
    ret_str += f'                                        "statIcon": {config.stat_icon},\n'

    # Bool attributes
    ret_str += f'                                        "fromCardMerge": {formatted_true_false(config.from_card_merge)},\n'
    ret_str += f'                                        "fromDuplicateMerge": {formatted_true_false(config.from_duplicate_merge)},\n'
    ret_str += f'                                        "fromTotem": {formatted_true_false(config.from_totem)},\n'
    ret_str += f'                                        "fromLatch": {formatted_true_false(config.from_latch)},\n'
    ret_str += f'                                        "fromOverclock": {formatted_true_false(config.from_overclock)},\n'
    ret_str += f'                                        "sideDeckMod": {formatted_true_false(config.side_deck_mod)},\n'
    ret_str += f'                                        "nonCopyable": {formatted_true_false(config.non_copyable)},\n'
    ret_str += f'                                        "fromEvolve": {formatted_true_false(config.from_evolve)},\n'

    ret_str += f'                                        "transformerBeastCardId": {config.transformer_beast_card_id},\n'
    ret_str += f'                                        "deathCardInfo": {config.death_card_info},\n'
    ret_str += f'                                        "bountyHunterInfo": {config.bounty_hunter_info},\n'
    ret_str += f'                                        "buildACardPortraitInfo": {config.build_a_card_portrait_info},\n'

    # Structure
    ret_str += """                                        "decalIds": {
                                            "$id": """
    ret_str += str(id + 6)
    ret_str += ',\n'

    # Decal IDs
    ret_str += """                                            "$type": 9,
                                            "$rlength": """
    ret_str += str(len(config.decal_ids))
    ret_str += ',\n'

    ret_str += '                                            "$rcontent": [\n'

    for a in config.decal_ids:
        ret_str += f'                                                "{a.value}",\n'
    
    # Structure
    ret_str += """                                            ]
                                        }
                                    }"""

    return ret_str, id + 7

def generate_card_mod_block(
    card : Card,
    card_instance : int,
    id : int
) -> tuple[str, int]:

    ret_str = """                        {
                            "$k": """
    ret_str += f'"{card.name}"'

    if card_instance > 0:
        ret_str += f'#{card_instance}'
    
    ret_str += ',\n'

    ret_str += """                            "$v": {
                                "$id": """
    ret_str += f"{id},\n"

    id += 1

    ret_str += """                                "$type": 15,
                                "$rlength": """
    ret_str += f'{len(card.mod_configs)},\n'

    ret_str += """                                "$rcontent": ["""
    ret_str += "\n"

    for i, mod_config in enumerate(card.mod_configs):

        mod_card_info_str, id = generate_mod_card_info(id, mod_config)
        ret_str += mod_card_info_str

        if i < len(card.mod_configs) - 1:
            ret_str += ","
        ret_str += "\n"
    
    ret_str += """                                ]
                            }
                        }"""
    
    return ret_str, id

def write_save_file(save_file_path : str, cards : list[Card]) -> None:

    write_lines : list[str] = []
    id = 0
    overwriting = False
    ascension_init = False
    current_run_init = False
    card_mod_info_init = False
    write_card_names = False
    write_card_names_complete = False
    card_mod_complete = False

    with open(save_file_path, 'r') as f:
        for line in f:
            if line.startswith('    "ascensionData": {'):
                ascension_init = True
            
            if not ascension_init and '"$id": ' in line:
                id = int(parse_text_between_things(line, first= '"$id": ', second= ","))

            if ascension_init and line.startswith('        "currentRun": {'):
                current_run_init = True
                write_card_names = True

            if current_run_init and write_card_names and not write_card_names_complete and line.startswith('                    "$rlength":'):
                overwriting = True
                write_card_names_complete = True

                write_lines.append(f'                    "$rlength": {len(cards)},\n')
                write_lines.append('                    "$rcontent": [\n')
                
                for i, card in enumerate(cards):
                    if i < len(cards) - 1:
                        write_lines.append(f'                        "{card.name}",\n')
                    else:
                        write_lines.append(f'                        "{card.name}"\n')
            
            if current_run_init and line.startswith('                    ]'):
                overwriting = False
            
            if line.startswith('                "cardIdModInfos": {'):
                card_mod_info_init = True
            
            if card_mod_info_init and not card_mod_complete and line.startswith('                    "$rlength": '):
                overwriting = True
                card_mod_complete = True

                write_lines.append(f'                    "$rlength": {len(cards)},\n')
                write_lines.append('                    "$rcontent": [\n')

                instance_dict = {}
                for i, card in enumerate(cards):
                    if card.name not in instance_dict:
                        instance_dict[card.name] = 0
                    else:
                        instance_dict[card.name] += 1

                    ret_str, id = generate_card_mod_block(card, card_instance= instance_dict[card.name], id= id)

                    if i < len(cards) - 1:
                        write_lines.append(ret_str + ",\n")
                    else:
                        write_lines.append(ret_str + "\n")           
            

            if not overwriting:
                write_lines.append(line)

                if ascension_init and '"$id": ' in line:
                    id_index = line.index('"$id": ')
                    line = line[:id_index + 7] + str(id) + ",\n"
                    id += 1
    
    with open(save_file_path, 'w') as f:
        f.writelines(write_lines)

last_modified = None
def save_file_changed(save_file_path : str) -> bool:
    global last_modified

    current_modified = os.path.getmtime(save_file_path)
    if last_modified is None:
        last_modified = current_modified
    if current_modified != last_modified:
        time_diff_seconds = abs(current_modified - last_modified)
        last_modified = current_modified
        logger.log(INFO, f"########################### File save detected")
        return time_diff_seconds > 5
    return False

def handle_save_write(cards : list[Card], save_file_path : str, write_necessary : bool) -> None:
    global last_modified

    if write_necessary:
        write_save_file(save_file_path= save_file_path, cards= cards)
        last_modified = os.path.getmtime(save_file_path)
        
        # logger.log(level= INFO, message= "########################Cards written:")
        for card in cards:
            logger.log(INFO, message= str(card))
    
from random import choice, randint, random

def challenge_card_randomizer(cards : list[Card]) -> bool:

    for i, card in enumerate(cards):

        sigil_count = len(card.abilities)
        stat_sum = card.attack + card.health

        # Take an initial swing at generating a random card
        if card.base_stats.rare:
            if card.base_stats.rare:
                new_creature = choice(rare_standard_cards).value
            else:
                new_creature = choice(not_rare_standard_cards).value
        else:
            new_creature = choice(not_rare_standard_cards).value
        new_card = Card(new_creature)

        # If it has more sigils than the original card,
        # Generate new cards until you find one that has the same
        # or less amount of sigils
        while len(new_card.abilities) > sigil_count:

            if card.base_stats.rare:
                new_creature = choice(rare_standard_cards).value
            else:
                new_creature = choice(not_rare_standard_cards).value
            new_card = Card(new_creature)
        
        # If the new card now has less sigils,
        # Add a card mod config with random
        # additional sigils to make upthe difference
        if len(new_card.abilities) < sigil_count:
            new_mod = CardModConfig()

            while (len(new_card.abilities) + len(new_mod.abilities)) < sigil_count:
                new_ability = choice(list(Ability))
                if new_ability not in new_card.abilities:
                    new_mod.abilities.append(new_ability)
            
            new_card.add_mod_config(new_mod)
        
        # Adjust the attack and health randomly so they
        # add to the original card's stat sum
        if stat_sum == 1:
            new_attack_stat = 0
            new_health_stat = 1
        elif stat_sum == 2:
            new_attack_stat = 1
            new_health_stat = 1
        else:
            new_attack_stat = randint(1, stat_sum - 1)
            new_health_stat = stat_sum - new_attack_stat
        
        new_blood_cost = card.blood_cost
        new_bone_cost = card.bone_cost

        # Blood card or no cost
        if card.blood_cost > 0 or card.blood_cost == 0 and card.bone_cost == 0:

            if random() > 0.97:
                new_blood_cost += 1
                logger.log(level= WARNING, message= "Blood cost increased by 1")
            
            if random() > 0.97:
                new_blood_cost -= 1
                logger.log(level= WARNING, message= "Blood cost decreased by 1")
        
        # Bone card
        else:

            if random() > 0.97:
                new_bone_cost += 1
                logger.log(level= WARNING, message= "Bone cost increased by 1")
            
            if random() > 0.97:
                new_bone_cost -= 1
                logger.log(level= WARNING, message= "Bone cost decreased by 1")

        new_blood_cost = clamp(new_blood_cost, 0, 4)
        new_bone_cost = clamp(new_bone_cost, 0, 8)

        new_mod = CardModConfig()
        new_mod.attack_adjustment = new_attack_stat - new_card.attack
        new_mod.health_adjustment = new_health_stat - new_card.health
        new_mod.blood_cost_adjustment = new_blood_cost - new_card.base_stats.blood_cost
        new_mod.bones_cost_adjustment = new_bone_cost - new_card.base_stats.bone_cost
        new_card.add_mod_config(new_mod)

        cards[i] = new_card

    write_necessary = True
    return write_necessary


def challenge_all_twos(cards : list[Card]) -> bool:

    write_necessary = True

    for card in cards:

        if card.attack > 2 or card.health > 2 or card.blood_cost > 0:

            write_necessary = True

            new_mod = CardModConfig()

            if card.attack > 2:
                # Clamp attack to 2
                new_mod.attack_adjustment = 2 - card.attack
            
            if card.health > 2:
                # Clamp health to 2
                new_mod.health_adjustment = 2 - card.health
            
            if card.blood_cost > 0:
                # Clamp to 0
                new_mod.blood_cost_adjustment = 0 - card.blood_cost

            card.add_mod_config(new_mod)
    
    return write_necessary

def challenge(cards : list[Card]) -> bool:

    return challenge_card_randomizer(cards= cards)
        
    

if __name__ == "__main__":

    import os
    def clear_term():
        os.system('cls' if os.name == 'nt' else 'clear')

    save_file_path = 'SaveFile.gwsave'

    while True:

        if save_file_changed(save_file_path):

            clear_term()

            cards = parse_save_file(save_file_path)

            # logger.log(level= INFO, message= "#################### Cards parsed:")
            # for card in cards:
            #     logger.log(INFO, message= str(card))

            write_necessary = challenge(cards)
            handle_save_write(cards, save_file_path, write_necessary)

        time.sleep(1)

