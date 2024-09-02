from enum import Enum, auto as enum_auto

class TotemTop(Enum):
    REPTILE = 5

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