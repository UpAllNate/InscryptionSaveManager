from enum import Enum, auto as enum_auto
from card_attribute_enums import (
    Tribe,
    Ability
)
from dataclasses import dataclass, field

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

class Creature(Enum):

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
    Creature.HYDRA : BaseStats(
        display_name= "Hydra",
        attack= 1,
        health= 5,
        bone_cost= 1,
        rare= True,
        tribes= [t for t in Tribe if t is not Tribe.SQUIRREL],
        abilities= [Ability.BIFURCATED, Ability.TRIFURCATED]
    ),
    Creature.IJIRAQ : BaseStats(
        display_name= "Ijiraq",
        attack= 4,
        health= 1,
        blood_cost= 0,
        rare= True,
        tribes= [],
        abilities= [Ability.REPULSIVE]
    ),
    Creature.MANTISGOD : BaseStats(
        display_name= "Mantis God",
        attack= 1,
        health= 1,
        blood_cost= 1,
        rare= True,
        tribes= [Tribe.INSECT],
        abilities= [Ability.TRIFURCATED]
    ),
    Creature.AMOEBA : BaseStats(
        display_name= "Amoeba",
        attack= 1,
        health= 2,
        rare= True,
        tribes= [],
        bone_cost= 2,
        abilities= [Ability.AMORPHOUS]
    ),
    Creature.STATIC_GLITCH : BaseStats(
        display_name= "Static Glitch",
        attack= 1,
        health= 1,
        tribes= [],
        blood_cost= 1,
        abilities= []
    ),
    Creature.PELTLICE : BaseStats(
        display_name= "Pelt Lice",
        attack= 1,
        health= 1,
        rare= False,
        tribes= [],
        blood_cost= 4,
        abilities= [Ability.DOUBLE_STRIKE]
    ),
    Creature.CAT : BaseStats(
        display_name= "Cat",
        attack= 0,
        health= 1,
        tribes= [],
        blood_cost= 1,
        abilities= [Ability.MANY_LIVES]
    ),
    Creature.URAYULI : BaseStats(
        display_name= "Urayuli",
        attack= 7,
        health= 7,
        rare= True,
        tribes= [],
        blood_cost= 4,
        abilities= []
    ),
    Creature.OUROBOROS : BaseStats(
        display_name= "Ouroboros",
        attack= 1,
        health= 1,
        rare= True,
        tribes= [Tribe.REPTILE],
        blood_cost= 2,
        abilities= [Ability.UNKILLABLE]
    ),
    Creature.SQUIRREL : BaseStats(
        display_name= "Squirrel",
        attack= 0,
        health= 1,
        tribes= [Tribe.SQUIRREL],
        abilities= []
    ),
    Creature.WOLFCUB : BaseStats(
        display_name= "Wolf Cub",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.CANINE],
        abilities= [Ability.FLEDGLING]
    ),
    Creature.PORCUPINE : BaseStats(
        display_name= "Porcupine",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.SHARP_QUILLS]
    ),
    Creature.COYOTE : BaseStats(
        display_name= "Coyote",
        attack= 2,
        health= 1,
        bone_cost= 4,
        tribes= [Tribe.CANINE],
        abilities= []
    ),
    Creature.STOAT : BaseStats(
        display_name= "Stoat",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [],
        abilities= []
    ),
    Creature.WOLF : BaseStats(
        display_name= "Wolf",
        attack= 3,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.CANINE],
        abilities= []
    ),
    Creature.SKUNK : BaseStats(
        display_name= "Skunk",
        attack= 0,
        health= 3,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.STINKY]
    ),
    Creature.PRONGHORN : BaseStats(
        display_name= "Pronghorn",
        attack= 1,
        health= 3,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER, Ability.BIFURCATED]
    ),
    Creature.RINGWORM : BaseStats(
        display_name= "Ringworm",
        attack= 0,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= []
    ),
    Creature.TREE : BaseStats(
        display_name= "Tree?",
        attack= 0,
        health= 4,
        tribes= [],
        abilities= []
    ),
    Creature.SPARROW : BaseStats(
        display_name= "Sparrow",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creature.BULLFROG : BaseStats(
        display_name= "Bullfrog",
        attack= 1,
        health= 2,
        blood_cost= 1,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creature.BOULDER : BaseStats(
        display_name= "Boulder",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.SMOKE : BaseStats(
        display_name= "The Smoke",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= [Ability.BONE_KING]
    ),
    Creature.MULE : BaseStats(
        display_name= "Pack Mule",
        attack= 0,
        health= 5,
        tribes= [],
        abilities= [Ability.SPRINTER]
    ),
    Creature.BEEHIVE : BaseStats(
        display_name= "Beehive",
        attack= 0,
        health= 2,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= [Ability.BEES_WITHIN]
    ),
    Creature.BEE : BaseStats(
        display_name= "Bee",
        attack= 1,
        health= 1,
        blood_cost= 0,
        tribes= [Tribe.INSECT],
        abilities= [Ability.AIRBORN]
    ),
    Creature.MANTIS : BaseStats(
        display_name= "Mantis",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= [Ability.BIFURCATED]
    ),
    Creature.GOLDNUGGET : BaseStats(
        display_name= "Nugget",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.BLOODHOUND : BaseStats(
        display_name= "Bloodhound",
        attack= 2,
        health= 3,
        blood_cost= 2,
        tribes= [Tribe.CANINE],
        abilities= [Ability.GUARDIAN]
    ),
    Creature.VULTURE : BaseStats(
        display_name= "Turkey Vulture",
        attack= 3,
        health= 3,
        bone_cost= 8,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creature.RAVENEGG : BaseStats(
        display_name= "Raven Egg",
        attack= 0,
        health= 2,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.FLEDGLING]
    ),
    Creature.GECK : BaseStats(
        display_name= "Geck",
        attack= 1,
        health= 1,
        rare= True,
        blood_cost= 0,
        tribes= [Tribe.REPTILE],
        abilities= []
    ),
    Creature.RAVEN : BaseStats(
        display_name= "Raven",
        attack= 2,
        health= 3,
        blood_cost= 2,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creature.MOLE : BaseStats(
        display_name= "Mole",
        attack= 0,
        health= 4,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.BURROWER]
    ),
    Creature.COCKROACH : BaseStats(
        display_name= "Cockroach",
        attack= 1,
        health= 1,
        bone_cost= 4,
        tribes= [Tribe.INSECT],
        abilities= [Ability.UNKILLABLE]
    ),
    Creature.ALPHA : BaseStats(
        display_name= "Alpha",
        attack= 1,
        health= 2,
        tribes= [Tribe.CANINE],
        bone_cost= 4,
        abilities= [Ability.LEADER]
    ),
    Creature.PACKRAT : BaseStats(
        display_name= "Pack Rat",
        attack= 2,
        health= 2,
        rare= True,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.TRINKET_BEARER]
    ),
    Creature.ANT : BaseStats(
        display_name= "Worker Ant",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= []
    ),
    Creature.ANTQUEEN : BaseStats(
        display_name= "Ant Queen",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.INSECT],
        abilities= [Ability.ANT_SPAWNER]
    ),
    Creature.SKINK : BaseStats(
        display_name= "Skink",
        attack= 1,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.LOOSE_TAIL]
    ),
    Creature.ADDER : BaseStats(
        display_name= "Adder",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.TOUCH_OF_DEATH]
    ),
    Creature.KINGFISHER : BaseStats(
        display_name= "Kingfisher",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.WATERBORNE, Ability.AIRBORN]
    ),
    Creature.BAITBUCKET : BaseStats(
        display_name= "Bait Bucket",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.TREE_SNOWCOVERED : BaseStats(
        display_name= "Snowy Tree?",
        attack= 0,
        health= 3,
        tribes= [],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creature.ELKCUB : BaseStats(
        display_name= "Elk Fawn",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER, Ability.FLEDGLING]
    ),
    Creature.MAGGOTS : BaseStats(
        display_name= "Corpse Maggots",
        attack= 1,
        health= 1,
        bone_cost= 5,
        tribes= [Tribe.INSECT],
        abilities= [Ability.CORPSE_EATER]
    ),
    Creature.TRAPFROG : BaseStats(
        display_name= "Strange Frog",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creature.TRAP : BaseStats(
        display_name= "Trap",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= [Ability.MIGHTY_LEAP]
    ),
    Creature.SHARK : BaseStats(
        display_name= "Great White",
        attack= 4,
        health= 2,
        blood_cost= 3,
        tribes= [],
        abilities= [Ability.WATERBORNE]
    ),
    Creature.MOLEMAN : BaseStats(
        display_name= "Moleman",
        attack= 0,
        health= 6,
        blood_cost= 1,
        rare= True,
        tribes= [],
        abilities= [Ability.BURROWER, Ability.MIGHTY_LEAP]
    ),
    Creature.MOTHMAN : BaseStats(
        display_name= "Strange Larva",
        attack= 0,
        health= 3,
        blood_cost= 1,
        rare= True,
        tribes= [Tribe.INSECT],
        abilities= [Ability.FLEDGLING]
    ),
    Creature.AMALGAM : BaseStats(
        display_name= "Amalgam",
        attack= 3,
        health= 3,
        rare= True,
        tribes= [t for t in Tribe],
        blood_cost= 2,
        abilities= []
    ),
    Creature.STUMP : BaseStats(
        display_name= "Stump",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.GIANTCARD_MOON : BaseStats(
        display_name= "The Moon",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.TAIL_INSECT : BaseStats(
        display_name= "Insect Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.PELTHARE : BaseStats(
        display_name= "Rabbit Pelt",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.MOOSE : BaseStats(
        display_name= "Moose Buck",
        attack= 3,
        health= 7,
        blood_cost= 3,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.HEAFTY]
    ),
    Creature.RABBIT : BaseStats(
        display_name= "Rabbit",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.RATTLER : BaseStats(
        display_name= "Rattler",
        attack= 3,
        health= 1,
        bone_cost= 6,
        tribes= [Tribe.REPTILE],
        abilities= []
    ),
    Creature.SNAPPER : BaseStats(
        display_name= "River Snapper",
        attack= 1,
        health= 6,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= []
    ),
    Creature.SQUIDBELL : BaseStats(
        display_name= "Squid (Bell)",
        attack= 1,
        health= 3,
        blood_cost= 2,
        tribes= [],
        abilities= []
    ),
    Creature.DEFAULTTAIL : BaseStats(
        display_name= "Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.LONG_ELK : BaseStats(
        display_name= "Long Elk",
        attack= 1,
        health= 2,
        bone_cost= 4,
        rare= True,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER, Ability.TOUCH_OF_DEATH]
    ),
    Creature.GOAT : BaseStats(
        display_name= "Black Goat",
        attack= 0,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.WORTHY_SACRIFICE]
    ),
    Creature.ELK : BaseStats(
        display_name= "Elk",
        attack= 2,
        health= 4,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER]
    ),
    Creature.BULL : BaseStats(
        display_name= "Wild Bull",
        attack= 3,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.RAMPAGER]
    ),
    Creature.BAT : BaseStats(
        display_name= "Bat",
        attack= 2,
        health= 1,
        bone_cost= 4,
        tribes= [],
        abilities= [Ability.AIRBORN]
    ),
    Creature.GRIZZLY : BaseStats(
        display_name= "Grizzly",
        attack= 4,
        health= 6,
        blood_cost= 3,
        tribes= [],
        abilities= []
    ),
    Creature.ANTFLYING : BaseStats(
        display_name= "Flying Ant",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.INSECT],
        abilities= [Ability.AIRBORN]
    ),
    Creature.PELTGOLDEN : BaseStats(
        display_name= "Golden Pelt",
        attack= 0,
        health= 3,
        blood_cost= 0,
        tribes= [],
        abilities= []
    ),
    Creature.FROZENOPOSSUM : BaseStats(
        display_name= "Frozen Opossum",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= [Ability.FROZEN_AWAY]
    ),
    Creature.OPOSSUM : BaseStats(
        display_name= "Opossum",
        attack= 1,
        health= 1,
        bone_cost= 2,
        tribes= [],
        abilities= []
    ),
    Creature.PELTWOLF : BaseStats(
        display_name= "Wolf Pelt",
        attack= 0,
        health= 2,
        tribes= [],
        abilities= []
    ),
    Creature.SQUIDCARDS : BaseStats(
        display_name= "Squid (Cards)",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= []
    ),
    Creature.DAM : BaseStats(
        display_name= "Dam",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.MUDTURTLE : BaseStats(
        display_name= "Mud Turtle",
        attack= 2,
        health= 2,
        blood_cost= 2,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.ARMORED]
    ),
    Creature.RATKING : BaseStats(
        display_name= "Rat King",
        attack= 2,
        health= 1,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.BONE_KING]
    ),
    Creature.OTTER : BaseStats(
        display_name= "River Otter",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.WATERBORNE]
    ),
    Creature.FIELDMOUSE : BaseStats(
        display_name= "Field Mice",
        attack= 2,
        health= 2,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.FECUNDITY]
    ),
    Creature.TAIL_BIRD : BaseStats(
        display_name= "Bird Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.JERSEYDEVIL : BaseStats(
        display_name= "Child 13",
        attack= 1,
        health= 1,
        rare= True,
        blood_cost= 1,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.MANY_LIVES]
    ),
    Creature.DAUS : BaseStats(
        display_name= "The Daus",
        attack= 2,
        health= 2,
        blood_cost= 2,
        rare= True,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.BELLIST]
    ),
    Creature.DAUSBELL : BaseStats(
        display_name= "Chime",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.TAIL_FURRY : BaseStats(
        display_name= "Furry Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.SQUIDMIRROR : BaseStats(
        display_name= "Squid (Mirro)",
        attack= 1,
        health= 3,
        blood_cost= 1,
        tribes= [],
        abilities= []
    ),
    Creature.DIREWOLF : BaseStats(
        display_name= "Dire Wolf",
        attack= 2,
        health= 5,
        blood_cost= 3,
        tribes= [Tribe.CANINE],
        abilities= [Ability.DOUBLE_STRIKE]
    ),
    Creature.MEALWORM : BaseStats(
        display_name= "Mealworm",
        attack= 0,
        health= 2,
        bone_cost= 2,
        tribes= [Tribe.INSECT],
        abilities= [Ability.MORSEL]
    ),
    Creature.KRAKEN : BaseStats(
        display_name= "Great Kraken",
        attack= 1,
        health= 1,
        blood_cost= 1,
        rare= True,
        tribes= [],
        abilities= [Ability.WATERBORNE_TENTACLE]
    ),
    Creature.RACCOON : BaseStats(
        display_name= "Raccoon",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.SCAVENGER]
    ),
    Creature.DIREWOLFPUP : BaseStats(
        display_name= "Dire Wolf Pup",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.CANINE],
        abilities= [Ability.BONE_DIGGER, Ability.FLEDGLING]
    ),
    Creature.WOLVERINE : BaseStats(
        display_name= "Wolverine",
        attack= 1,
        health= 3,
        bone_cost= 5,
        tribes= [],
        abilities= []
    ),
    Creature.LAMMERGEIER : BaseStats(
        display_name= "Lammergeier",
        attack= 1,
        health= 4,
        blood_cost= 3,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.AIRBORN]
    ),
    Creature.MAGPIE : BaseStats(
        display_name= "Magpie",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.HOARDER, Ability.AIRBORN]
    ),
    Creature.REDHART : BaseStats(
        display_name= "Redhart",
        attack= 1,
        health= 1,
        blood_cost= 2,
        tribes= [Tribe.HOOVED],
        abilities= [Ability.SPRINTER]
    ),
    Creature.TADPOLE : BaseStats(
        display_name= "Tadpole",
        attack= 0,
        health= 1,
        blood_cost= 0,
        tribes= [Tribe.REPTILE],
        abilities= [Ability.WATERBORNE, Ability.FLEDGLING]
    ),
    Creature.SKINKTAIL : BaseStats(
        display_name= "Skink Tail",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.AQUASQUIRREL : BaseStats(
        display_name= "Aqua Squirrel",
        attack= 1,
        health= 1,
        tribes= [Tribe.SQUIRREL],
        abilities= []
    ),
    Creature.HYDRAEGG : BaseStats(
        display_name= "Hydra Egg",
        attack= 1,
        health= 1,
        bone_cost= 1,
        rare= True,
        tribes= [],
        abilities= []
    ),
    Creature.STARVATION : BaseStats(
        display_name= "Starvation",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.CUCKOO : BaseStats(
        display_name= "Cuckoo",
        attack= 1,
        health= 1,
        blood_cost= 1,
        tribes= [Tribe.AVIAN],
        abilities= [Ability.BROODPARASITE]
    ),
    Creature.SNELK_NECK : BaseStats(
        display_name= "Vertebrae",
        attack= 0,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.MOLESEAMAN : BaseStats(
        display_name= "Mole Seaman",
        attack= 1,
        health= 8,
        blood_cost= 1,
        rare= True,
        tribes= [],
        abilities= [Ability.BURROWER, Ability.MIGHTY_LEAP]
    ),
    Creature.GIANTCARD_SHIP : BaseStats(
        display_name= "The Limonchello",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.SKELETONPIRATE : BaseStats(
        display_name= "Skeleton Pirate",
        attack= 1,
        health= 1,
        tribes= [],
        abilities= []
    ),
    Creature.WARREN : BaseStats(
        display_name= "Warren",
        attack= 0,
        health= 2,
        blood_cost= 1,
        tribes= [],
        abilities= [Ability.RABBIT_HOLE]
    ),
    Creature.HODAG : BaseStats(
        display_name= "Hodag",
        attack= 1,
        health= 5,
        blood_cost= 2,
        rare= True,
        tribes= [],
        abilities= []
    ),
    Creature.BEAVER : BaseStats(
        display_name= "Beaver",
        attack= 1,
        health= 3,
        blood_cost= 2,
        tribes= [],
        abilities= [Ability.DAM_BUILDER]
    )
}