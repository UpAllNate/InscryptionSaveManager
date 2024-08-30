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
        rare= True,
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
        rare= True,
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