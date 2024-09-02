from creatures import Creature, base_stat_dict

standard_cards = [
    Creature.AMOEBA,
    Creature.PELTLICE,
    Creature.CAT,
    Creature.URAYULI,
    Creature.OUROBOROS,
    Creature.MANTISGOD,
    Creature.SQUIRREL,
    Creature.WOLFCUB,
    Creature.PORCUPINE,
    Creature.COYOTE,
    Creature.STOAT,
    Creature.WOLF,
    Creature.SKUNK,
    Creature.PRONGHORN,
    Creature.RINGWORM,
    Creature.SPARROW,
    Creature.BULLFROG,
    Creature.BEEHIVE,
    Creature.BEE,
    Creature.MANTIS,
    Creature.BLOODHOUND,
    Creature.VULTURE,
    Creature.RAVENEGG,
    Creature.GECK,
    Creature.RAVEN,
    Creature.MOLE,
    Creature.COCKROACH,
    Creature.ALPHA,
    Creature.PACKRAT,
    Creature.ANT,
    Creature.ANTQUEEN,
    Creature.SKINK,
    Creature.ADDER,
    Creature.KINGFISHER,
    Creature.ELKCUB,
    Creature.MAGGOTS,
    Creature.SHARK,
    Creature.MOLEMAN,
    Creature.MOTHMAN,
    Creature.AMALGAM,
    Creature.PELTHARE,
    Creature.MOOSE,
    Creature.RABBIT,
    Creature.RATTLER,
    Creature.SNAPPER,
    Creature.SQUIDBELL,
    Creature.LONG_ELK,
    Creature.GOAT,
    Creature.ELK,
    Creature.BULL,
    Creature.BAT,
    Creature.GRIZZLY,
    Creature.ANTFLYING,
    Creature.PELTGOLDEN,
    Creature.FROZENOPOSSUM,
    Creature.OPOSSUM,
    Creature.PELTWOLF,
    Creature.SQUIDCARDS,
    Creature.MUDTURTLE,
    Creature.RATKING,
    Creature.OTTER,
    Creature.FIELDMOUSE,
    Creature.JERSEYDEVIL,
    Creature.DAUS,
    Creature.SQUIDMIRROR,
    Creature.DIREWOLF,
    Creature.MEALWORM,
    Creature.KRAKEN,
    Creature.RACCOON,
    Creature.DIREWOLFPUP,
    Creature.WOLVERINE,
    Creature.LAMMERGEIER,
    Creature.MAGPIE,
    Creature.REDHART,
    Creature.TADPOLE,
    Creature.HYDRAEGG,
    Creature.CUCKOO,
    Creature.MOLESEAMAN,
    Creature.WARREN,
    Creature.HODAG,
    Creature.BEAVER,
    Creature.IJIRAQ,
    Creature.HYDRA
]

pelt_cards = [
    Creature.PELTGOLDEN,
    Creature.PELTHARE,
    Creature.PELTWOLF
]

rare_standard_cards = [c for c in standard_cards if base_stat_dict[c].rare]
not_rare_standard_cards = [c for c in standard_cards if c not in rare_standard_cards]

no_cost_standard_cards = [c for c in standard_cards if base_stat_dict[c].bone_cost == 0 and base_stat_dict[c].blood_cost == 0]
no_cost_rare_standard_cards = [c for c in standard_cards if base_stat_dict[c].bone_cost == 0 and base_stat_dict[c].blood_cost == 0 and base_stat_dict[c].rare]
no_cost_not_rare_standard_cards = [c for c in no_cost_standard_cards if c not in no_cost_rare_standard_cards]

blood_cost_standard_cards : list[list[Creature]] = []
for blood_cost in range(1,5):
    blood_cost_standard_cards.append(
        [c for c in standard_cards if base_stat_dict[c].blood_cost == blood_cost]
    )

blood_cost_rare_standard_cards : list[list[Creature]] = []
for blood_cost in range(1,5):
    blood_cost_rare_standard_cards.append(
        [c for c in rare_standard_cards if base_stat_dict[c].blood_cost == blood_cost]
    )

blood_cost_not_rare_standard_cards : list[list[Creature]] = []
for blood_cost in range(1,5):
    blood_cost_not_rare_standard_cards.append(
        [c for c in not_rare_standard_cards if base_stat_dict[c].blood_cost == blood_cost]
    )

bone_cost_standard_cards : list[list[Creature]] = []
for bone_cost in range(1,10):
    bone_cost_standard_cards.append(
        [c for c in standard_cards if base_stat_dict[c].bone_cost == bone_cost]
    )

bone_cost_rare_standard_cards : list[list[Creature]] = []
for bone_cost in range(1,10):
    bone_cost_rare_standard_cards.append(
        [c for c in rare_standard_cards if base_stat_dict[c].bone_cost == bone_cost]
    )

bone_cost_not_rare_standard_cards : list[list[Creature]] = []
for bone_cost in range(1,10):
    bone_cost_not_rare_standard_cards.append(
        [c for c in not_rare_standard_cards if base_stat_dict[c].bone_cost == bone_cost]
    )