from random import choice, randint, random
from card_classes import Card, CardModConfig
from card_collection import (
    standard_cards,
    rare_standard_cards,
    not_rare_standard_cards,
    blood_cost_standard_cards,
    blood_cost_rare_standard_cards,
    blood_cost_not_rare_standard_cards,
    bone_cost_standard_cards,
    bone_cost_rare_standard_cards,
    bone_cost_not_rare_standard_cards,
    no_cost_standard_cards,
    no_cost_rare_standard_cards,
    no_cost_not_rare_standard_cards
)
from creatures import Creatures, base_stat_dict
from card_attribute_enums import Ability, Tribe, Decal
from project_logger import (
    ProjectLogger,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    color_text,
    Color
)

def clamp(input, low, high):
    ret = input
    if ret < low:
        return low
    if ret > high:
        return high
    return ret

def challenge_card_randomizer(cards : list[Card], logger : ProjectLogger) -> bool:

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
                logger.log(level= INFO, message= f"Card {new_card.base_stats.display_name} blood cost {color_text('increased', color= Color.RED)} by 1 to {new_blood_cost}")
            
            if random() > 0.97:
                new_blood_cost -= 1
                logger.log(level= INFO, message= f"Card {new_card.base_stats.display_name} blood cost {color_text('decreased', color= Color.GREEN)} by 1 to {new_blood_cost}")
        
        # Bone card
        else:

            if random() > 0.97:
                new_bone_cost += 1
                logger.log(level= INFO, message= f"Card {new_card.base_stats.display_name} bone cost {color_text('increased', color= Color.RED)} by 1 to {new_bone_cost}")
            
            if random() > 0.97:
                new_bone_cost -= 1
                logger.log(level= INFO, message= f"Card {new_card.base_stats.display_name} bone cost {color_text('decreased', color= Color.GREEN)} by 1 to {new_bone_cost}")

        new_blood_cost = clamp(new_blood_cost, 0, 4)
        new_bone_cost = clamp(new_bone_cost, 0, 8)

        new_mod = CardModConfig()
        new_mod.attack_adjustment = new_attack_stat - new_card.attack
        new_mod.health_adjustment = new_health_stat - new_card.health
        new_mod.blood_cost_adjustment = new_blood_cost - new_card.base_stats.blood_cost
        new_mod.bones_cost_adjustment = new_bone_cost - new_card.base_stats.bone_cost
        new_card.add_mod_config(new_mod)

        cards[i] = new_card
    
    logger.log(level= INFO, message= f"New cards:")
    for card in cards:
        logger.log(level= INFO, message= f"{card}")

    write_necessary = True
    return write_necessary


def challenge_stat_clamp(cards : list[Card], max_attack : int, max_health : int) -> bool:

    write_necessary = True

    for card in cards:

        if card.attack > max_attack or card.health > 2 or card.blood_cost > 0:

            write_necessary = True

            new_mod = CardModConfig()

            if card.attack > max_attack:
                # Clamp attack to max_attack
                new_mod.attack_adjustment = max_attack - card.attack
            
            if card.health > max_health:
                # Clamp health to max_health
                new_mod.health_adjustment = max_health - card.health
            
            if card.blood_cost > 0:
                # Clamp to 0
                new_mod.blood_cost_adjustment = 0 - card.blood_cost

            card.add_mod_config(new_mod)
    
    return write_necessary