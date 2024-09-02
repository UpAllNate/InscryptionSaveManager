from dataclasses import dataclass, field
from enum import Enum, auto as enum_auto
from card_attribute_enums import (
    Ability,
    Tribe,
    Decal
)
from project_logger import color_text, Color
from creatures import Creatures, BaseStats, base_stat_dict
from card_attribute_enums import Ability, Tribe

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
        ret_str = f"Attk: {'+' if self.attack_adjustment > 0 else ''}{self.attack_adjustment}, Health: {'+' if self.health_adjustment > 0 else ''}{self.health_adjustment}, Abilities: "
        
        if self.abilities:
            for a in self.abilities:
                ret_str += f"{a.name}, "
            ret_str = ret_str[:-2]
        else:
            ret_str += "None"
        return ret_str

class Card:

    def __init__(self, name : str) -> None:
        self.name = name
        self.creature = Creatures(name)
        self.base_stats : BaseStats = base_stat_dict[self.creature]
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

        if self.mod_configs:
            msg+= "\n"
            for mc in self.mod_configs:
                msg += f"\t{str(mc)}\n"
            msg = msg[:-1]

        return msg