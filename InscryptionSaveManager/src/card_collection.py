from creatures import Creatures, base_stat_dict

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