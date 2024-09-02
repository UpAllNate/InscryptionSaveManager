from random import choice, randint, random
from card_classes import Card, CardModConfig
from card_collection import (
    pelt_cards,
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
from creatures import Creature, base_stat_dict
from card_attribute_enums import Ability, Tribe, Decal
from project_logger import (
    ProjectLogger,
    standard_file_format_string,
    standard_stream_format_string,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    color_text,
    Color
)
from typing import Any

import os
def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')

def clamp(input, low, high):
    ret = input
    if ret < low:
        return low
    if ret > high:
        return high
    return ret

def prompt_for_data(prompt : str, logger : ProjectLogger, required_type = None, valid_responses : list = None) -> Any:

    while True:
        actual_prompt = prompt
        if valid_responses:
            actual_prompt += f"\n[Options] {valid_responses}\n"
        raw = input(actual_prompt).strip().lower()

        if required_type is not None:
            try:
                parsed_raw = required_type(raw)
            except TypeError:
                print()
                logger.log(level= WARNING, message= f"Warning: {raw.strip()} is invalid type.")
                print()
                continue
        else:
            parsed_raw = raw.strip()
        
        if valid_responses is not None:
            if parsed_raw not in valid_responses:
                print()
                logger.log(level= WARNING, message= f"Warning: {parsed_raw} is not one of the specified valid responses.")
                print()
                continue
                
        return parsed_raw

class Challenge:

    def __init__(self, meta_logger : ProjectLogger, ui_logger : ProjectLogger) -> None:
        self.meta_logger = meta_logger
        self.ui_logger = ui_logger
        self.initialized = False
    
    def startup_query(self) -> None:
        self.initialized = True

    def run(self, cards: list[Card]) -> bool:
        if not self.initialized:
            self.startup_query()

class ChallengeManager:

    def __init__(self, challenges: list[Challenge]) -> None:
        self.challenges = challenges
    
    def run(self, cards : list[Card]) -> bool:
        if True in [challenge.run(cards) for challenge in self.challenges]:
            return True

class Challenge_Sigil_Adder(Challenge):

    def __init__(self, meta_logger: ProjectLogger, ui_logger: ProjectLogger) -> None:
        super().__init__(meta_logger, ui_logger)

    def startup_query(self) -> None:
        return super().startup_query()
    
    def run(self, cards: list[Card]) -> bool:
        super().run(cards)

        for i, card in enumerate(cards):

            new_mod = CardModConfig()
            new_mod.abilities.append(choice(list(Ability)))
            new_mod.from_card_merge = True
        
            card.add_mod_config(new_mod)
        
        return True
    
class Challenge_BeeSwarm(Challenge):

    def __init__(self, meta_logger: ProjectLogger, ui_logger: ProjectLogger) -> None:
        super().__init__(meta_logger, ui_logger)

    def startup_query(self) -> None:
        return super().startup_query()
    
    def run(self, cards: list[Card]) -> bool:
        super().run(cards)

        cards.append(Card(Creature.BEEHIVE))
        
        return True

tribe_prompt_dict = {
    "avian" : Tribe.AVIAN,
    "reptile" : Tribe.REPTILE,
    "insect" : Tribe.INSECT,
    "avian" : Tribe.AVIAN,
    "canine" : Tribe.CANINE,
    "hooved" : Tribe.HOOVED
}

class Challenge_EnforceTribe(Challenge):

    def __init__(self, tribe: Tribe, meta_logger: ProjectLogger, ui_logger: ProjectLogger) -> None:
        super().__init__(meta_logger, ui_logger)

    def startup_query(self) -> None:
        super().startup_query()

        clear_term()

        self.maintain_rarity : bool = prompt_for_data(
            prompt= "[Enforce Tribe] Would you like rare cards to remain rares and standard cards remain standard?",
            logger= self.meta_logger,
            required_type= str,
            valid_responses= ['yes', 'no']
        )

        tribe_key = prompt_for_data(
            prompt= "[Enforce Tribe] Would you like rare cards to remain rares and standard cards remain standard?",
            logger= self.meta_logger,
            required_type= str,
            valid_responses= list(tribe_prompt_dict.keys())
        )

        self.maintain_sigil_count : bool = prompt_for_data(
            prompt= "[Enforce Tribe] Would you like to maintain that any replaced card's sigil count remain the same?",
            logger= self.meta_logger,
            required_type= str,
            valid_responses= ['yes', 'no']
        )

        self.tribe = tribe_prompt_dict[tribe_key]
    
    def card_is_of_tribe(self, card: Card) -> bool:

        if self.tribe not in card.base_stats.tribes and card.creature not in [creature for creature in pelt_cards]:
            return False
        
        return True

    def new_card_is_good(self, original_card : Card, new_card : Card) -> bool:       

        if self.tribe not in new_card.base_stats.tribes:
            return False
        
        if self.maintain_rarity:
            if original_card.base_stats.rare != new_card.base_stats.rare:
                return False

        if self.maintain_sigil_count:
            if len(original_card.abilities) < len(new_card.abilities):
                return False
        
        return True

    def run(self, cards: list[Card]) -> bool:
        super().run(cards)

        any_wrong_tribe = False
        for i, card in enumerate(cards):
            
            # Replace card if it isn't a part of this challenge's tribe
            if not self.card_is_of_tribe(card):

                self.meta_logger.log(level= INFO, message= f"[Enforce Tribe] Card {card.base_stats.display_name} is not a member of the tribe {self.tribe.name}.")
                any_wrong_tribe = True

                new_card = Card(card.creature)

                # Until the card is adequate
                while not self.new_card_is_good(original_card= card, new_card= new_card):

                    if self.maintain_rarity:
                        if card.base_stats.rare:
                            if self.maintain_sigil_count:
                                creature_pool = [
                                    creature for creature in rare_standard_cards if (
                                        self.tribe in base_stat_dict[creature].tribes
                                        and len(base_stat_dict[creature].abilities) == len(card.abilities)
                                    )
                                ]

                                if creature_pool:
                                    new_creature = choice(creature_pool)
                                else:
                                    creature_pool = [
                                        creature for creature in rare_standard_cards if (
                                            self.tribe in base_stat_dict[creature].tribes
                                            and len(base_stat_dict[creature].abilities) < len(card.abilities)
                                        )
                                    ]
                                    new_creature = choice(creature_pool)
                            else:
                                new_creature = choice(rare_standard_cards)
                        else:
                            if self.maintain_sigil_count:
                                creature_pool = [
                                    creature for creature in not_rare_standard_cards if (
                                        self.tribe in base_stat_dict[creature].tribes
                                        and len(base_stat_dict[creature].abilities) == len(card.abilities)
                                    )
                                ]

                                if creature_pool:
                                    new_creature = choice(creature_pool)
                                else:
                                    creature_pool = [
                                        creature for creature in not_rare_standard_cards if (
                                            self.tribe in base_stat_dict[creature].tribes
                                            and len(base_stat_dict[creature].abilities) < len(card.abilities)
                                        )
                                    ]
                                    new_creature = choice(creature_pool)
                            else:
                                new_creature = choice(not_rare_standard_cards)
                    
                    else:
                        new_creature = choice(standard_cards)

                    new_card = Card(new_creature)

                    needed_sigil_count = len(card.abilities) - len(new_card.abilities)
                    if self.maintain_sigil_count and needed_sigil_count > 0 :
                        new_mod = CardModConfig()
                        for _ in range(needed_sigil_count):
                            new_mod.abilities.append(choice(list(Ability)))
                        new_card.add_mod_config(new_mod)

                cards[i] = new_card
                self.meta_logger.log(level= INFO, message= f"[Enforce Tribe] Replacing card {card.base_stats.display_name} with {new_card}.")
                self.ui_logger.log(level= INFO, message= f"[Enforce Tribe] Card {card.base_stats.display_name} replaced with {new_card}.")

        return any_wrong_tribe

class Challenge_Deck_Randomizer(Challenge):

    def __init__(self, meta_logger : ProjectLogger, ui_logger : ProjectLogger) -> None:
        super().__init__(meta_logger, ui_logger)
    
    def startup_query(self) -> None:

        self.maintain_rarity : bool = prompt_for_data(
            prompt= "Would you like rare cards to remain rares and standard cards remain standard?",
            logger= self.meta_logger,
            required_type= str,
            valid_responses= ['yes', 'no']
        )

        self.maintain_sigil_count : bool = prompt_for_data(
            prompt= "Would you like to maintain that each card's sigil count remain the same?",
            logger= self.meta_logger,
            required_type= str,
            valid_responses= ['yes', 'no']
        )

        self.maintain_stats : bool = prompt_for_data(
            prompt= "Would you like to maintain each card's total attack / health stat sum?",
            logger= self.meta_logger,
            required_type= str,
            valid_responses= ['yes', 'no']
        )

        self.maintain_stats_exactly : bool = prompt_for_data(
            prompt= "Would you like to maintain each card's total attack / health stat sum?",
            logger= self.meta_logger,
            required_type= str,
            valid_responses= ['yes', 'no']
        )

        if not self.maintain_buffs:
            self.maintain_buffs : bool = prompt_for_data(
                prompt= "Would you like to maintain each card's buffs / debuffs?",
                logger= self.meta_logger,
                required_type= str,
                valid_responses= ['yes', 'no']
            )
        else:
            self.maintain_buffs = False
        
        self.initialized = True

    def generate_random_replacement_card(self, card : Card) -> Card:

        if self.maintain_rarity:
            if card.base_stats.rare:
                if card.base_stats.rare:
                    new_creature = choice(rare_standard_cards).value
                else:
                    new_creature = choice(not_rare_standard_cards).value
            else:
                new_creature = choice(not_rare_standard_cards).value
        
        else:
            new_creature = choice(standard_cards).value

        return Card(new_creature)

    def run(self, cards : list[Card]) -> bool:

        for i, card in enumerate(cards):

            sigil_count = len(card.abilities)
            stat_sum = card.attack + card.health

            # Take an initial swing at generating a random card
            new_card = self.generate_random_replacement_card(card)

            if self.maintain_sigil_count:

                # If it has more sigils than the original card,
                # Generate new cards until you find one that has the same
                # or less amount of sigils
                while len(new_card.abilities) > sigil_count:

                    new_card = self.generate_random_replacement_card(card)
                
                # If the new card now has less sigils,
                # Add a card mod config with random
                # additional sigils to make upthe difference
                if len(new_card.abilities) < sigil_count:

                    new_mod = CardModConfig()
                    new_mod.from_card_merge = True

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

                if random() > 0.99:
                    new_blood_cost += 1
                    self.ui_logger.log(level= INFO, message= f"Card {new_card.base_stats.display_name} blood cost {color_text('increased', color= Color.RED)} by 1 to {new_blood_cost}")
                
                if random() > 0.99:
                    new_blood_cost -= 1
                    self.ui_logger.log(level= INFO, message= f"Card {new_card.base_stats.display_name} blood cost {color_text('decreased', color= Color.GREEN)} by 1 to {new_blood_cost}")
            
            # Bone card
            else:

                if random() > 0.99:
                    new_bone_cost += 1
                    self.ui_logger(level= INFO, message= f"Card {new_card.base_stats.display_name} bone cost {color_text('increased', color= Color.RED)} by 1 to {new_bone_cost}")
                
                if random() > 0.99:
                    new_bone_cost -= 1
                    self.ui_logger(level= INFO, message= f"Card {new_card.base_stats.display_name} bone cost {color_text('decreased', color= Color.GREEN)} by 1 to {new_bone_cost}")

            new_blood_cost = clamp(new_blood_cost, 0, 4)
            new_bone_cost = clamp(new_bone_cost, 0, 8)

            new_mod = CardModConfig()
            new_mod.attack_adjustment = new_attack_stat - new_card.attack
            new_mod.health_adjustment = new_health_stat - new_card.health
            new_mod.blood_cost_adjustment = new_blood_cost - new_card.base_stats.blood_cost
            new_mod.bones_cost_adjustment = new_bone_cost - new_card.base_stats.bone_cost
            new_card.add_mod_config(new_mod)

            cards[i] = new_card
        
        self.meta_logger.log(level= INFO, message= f"New cards:")
        for card in cards:
            self.meta_logger.log(level= INFO, message= f"{card}")

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

if __name__ == "__main__":

    challenges_logger = ProjectLogger(
        file_logger_name= __file__ + "_file", file_log_level= DEBUG, file_log_format_string= standard_file_format_string,
        file_filename= __file__ + ".log", file_max_size= 10 * 1024 * 1024, file_backup_count= 0,
        stream_logger_name= __file__ + "_stream", stream_log_level= INFO, stream_log_format_string= standard_stream_format_string
    )

    valid_num : int = prompt_for_data(
        prompt= "Please enter a number between 1 and 10: ",
        logger= challenges_logger,
        required_type= int,
        valid_responses= [i for i in range(1, 11)]
    )
    print()
    challenges_logger.log(level= INFO, message= f"User selected '{valid_num}'")
