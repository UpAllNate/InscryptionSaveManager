from enum import Enum, auto as enum_auto
from project_logger import (
    ProjectLogger,
    LOW_DEBUG,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL
)
from card_classes import Card, CardModConfig
from card_attribute_enums import Ability, Decal
from creatures import Creature

FS = "    " # Four Spaces

def parse_text_between_substrings(s : str, first : str, second : str, logger : ProjectLogger) -> str:

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

def parse_mod_text(mod_text_lines : list[str], cards : list[Card], logger : ProjectLogger) -> None:

    logger.log(level= LOW_DEBUG, message= f'Parsing mod text')
    vol_card_index = -1
    card_index = 0
    parse_mod_text = False
    parsing_abilities = False
    parse_negate_abilities = False
    parse_add_gem_cost = False
    parse_special_abilities = False
    parse_decal_ids = False
    

    for line in mod_text_lines:
        logger.log(LOW_DEBUG, message= f"Parsing mod text line: {line[:-1]}")
        if line.startswith(FS*7 + '"$k": '):
            card_name = parse_text_between_substrings(line, first= '"$k": "', second= '"', logger= logger)
            logger.log(LOW_DEBUG, message= f"Mod Config data for card name {card_name} detected")
            if "#" in card_name:
                s = card_name.split("#")
                card_name, card_dupe_num = s[0], int(s[1])
            else:
                card_dupe_num = 0
            logger.log(level= LOW_DEBUG, message= f'Parsed card name {card_name} and card duplicate number {card_dupe_num}')

            for i in range(0, card_dupe_num + 1):
                temp_cards_list = [c.creature.value for c in cards[vol_card_index+ 1:]]
                vol_card_index = temp_cards_list.index(card_name)
                card_index += vol_card_index
                if i > 0:
                    card_index += 1
                logger.log(level= LOW_DEBUG, message= f'Card name {card_name} found at index {vol_card_index} in cards list {temp_cards_list}... primary list index {card_index}')
    
        if line.startswith(FS*9 + '{'):
            parse_mod_text = True
            mod_config = CardModConfig()
        
        if parse_mod_text:

            if line.startswith(FS*10 + '"nameReplacement":'):
                replacement_name = parse_text_between_substrings(line, first= " ", second= ",", logger= logger)
                if ': "' in replacement_name:
                    mod_config.replacement_name = parse_text_between_substrings(line, first= ': "', second= '"', logger= logger)

            if line.startswith(FS*10 + '"attackAdjustment":'):
                mod_config.attack_adjustment = int(parse_text_between_substrings(line, first= ": ", second= ",", logger= logger))

            if line.startswith(FS*10 + '"healthAdjustment":'):
                mod_config.health_adjustment = int(parse_text_between_substrings(line, first= ": ", second= ",", logger= logger))

            if line.startswith(FS*10 + '"abilities": {'):
                parsing_abilities = True

            if parsing_abilities:
                if line.startswith(FS*12):
                    if "," not in line:
                        ability_number = int(line.strip())
                    else:
                        ability_number = int(line.strip().split(",")[0])
                    mod_config.abilities.append(Ability(ability_number))

                if line.startswith(FS*11 + ']'):
                    parsing_abilities = False


            if line.startswith(FS*10 + '"negateAbilities": {'):
                parse_negate_abilities = True

            if parse_negate_abilities:
                if line.startswith(FS*12):
                    if "," not in line:
                        ability_number = int(line.strip())
                    else:
                        ability_number = int(line.strip().split(",")[0])
                    mod_config.negate_abilities.append(ability_number)

                if line.startswith(FS*11 + ']'):
                    parse_negate_abilities = False


            if "bloodCostAdjustment" in line:
                mod_config.blood_cost_adjustment = int(
                    parse_text_between_substrings(line.strip(), " ", ",", logger= logger)
                )
                logger.log(LOW_DEBUG, message= f"Blood Cost Adjustment for card name {card_name}: {mod_config.blood_cost_adjustment}")

            if line.startswith(FS*10 + '"bonesCostAdjustment":'):
                mod_config.bones_cost_adjustment = int(
                    parse_text_between_substrings(line.strip(), " ", ",", logger= logger)
                )
                logger.log(LOW_DEBUG, message= f"Bone Cost Adjustment for card name {card_name}: {mod_config.blood_cost_adjustment}")

            if line.startswith(FS*10 + '"energyCostAdjustment":'):
                mod_config.energy_cost_adjustment = int(
                    parse_text_between_substrings(line.strip(), " ", ",", logger= logger)
                )

            if line.startswith(FS*10 + '"nullifyGemsCost":'):
                mod_config.nullify_gems_cost = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'
            
            if line.startswith(FS*10 + '"addGemCost": {'):
                parse_add_gem_cost = True

            if parse_add_gem_cost:
                if line.startswith(FS*12):
                    if "," not in line:
                        gem_text = line.strip()
                    else:
                        gem_text = line.strip().split(",")[0]
                    mod_config.add_gem_cost.append(gem_text)

                if line.startswith(FS*11 + ']'):
                    parse_add_gem_cost = False

            if line.startswith(FS*10 + '"gemify":'):
                mod_config.gemify = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"specialAbilities": {'):
                parse_special_abilities = True

            if parse_special_abilities:
                if line.startswith(FS*12):
                    if "," not in line:
                        special_abilities_text = line.strip()
                    else:
                        special_abilities_text = line.strip().split(",")[0]
                    mod_config.special_abilities.append(special_abilities_text)

                if line.startswith(FS*11 + ']'):
                    parse_special_abilities = False


            if line.startswith(FS*10 + '"statIcon":'):
                mod_config.stat_icon = int(parse_text_between_substrings(line.strip(), " ", ",", logger= logger))

            if line.startswith(FS*10 + '"fromCardMerge":'):
                mod_config.from_card_merge = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"fromDuplicateMerge":'):
                mod_config.from_duplicate_merge = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"fromTotem":'):
                mod_config.from_totem = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"fromLatch":'):
                mod_config.from_latch = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"fromOverclock":'):
                mod_config.from_overclock = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"sideDeckMod":'):
                mod_config.side_deck_mod = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"nonCopyable":'):
                mod_config.non_copyable = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"fromEvolve":'):
                mod_config.from_evolve = parse_text_between_substrings(line.strip(), " ", ",", logger= logger) == 'true'

            if line.startswith(FS*10 + '"transformerBeastCardId":'):
                mod_config.transformer_beast_card_id = parse_text_between_substrings(line.strip(), " ", ",", logger= logger)

            if line.startswith(FS*10 + '"deathCardInfo":'):
                mod_config.death_card_info = parse_text_between_substrings(line.strip(), " ", ",", logger= logger)

            if line.startswith(FS*10 + '"bountyHunterInfo":'):
                mod_config.bounty_hunter_info = parse_text_between_substrings(line.strip(), " ", ",", logger= logger)

            if line.startswith(FS*10 + '"buildACardPortraitInfo":'):
                mod_config.build_a_card_portrait_info = parse_text_between_substrings(line.strip(), " ", ",", logger= logger)

            if line.startswith(FS*10 + '"decalIds": {'):
                parse_decal_ids = True

            if parse_decal_ids: 
                if line.startswith(FS*12):

                    decal_id_text = parse_text_between_substrings(line.strip(), '"', '"', logger= logger)
                    mod_config.decal_ids.append(Decal(decal_id_text))

                if line.startswith(FS*11 + ']'):
                    parse_decal_ids = False

            if line.startswith(FS*9 + "}"):
                parse_mod_text = False
                cards[card_index].add_mod_config(mod_config)

class SaveSection(Enum):
    INIT = enum_auto()
    ASCENSION = enum_auto()

class SaveParsingState(Enum):
    INIT = enum_auto()
    CURRENT_RUN = enum_auto()
    CARD_IDS = enum_auto()
    CARD_MODS = enum_auto()
    COLLECTING_MOD_BLOCK = enum_auto()

def parse_save_file(save_file_path : str, logger : ProjectLogger) -> list[Card]:
    
    save_section = SaveSection.INIT
    parsing_state = SaveParsingState.INIT

    cards : list[Card] = []

    with open(save_file_path, 'r') as f:

        for line in f:
            line_stripped = line.strip()

            if line_stripped.startswith('"ascensionData"'):
                save_section = SaveSection.ASCENSION
                parsing_state = SaveParsingState.INIT
                logger.log(level= LOW_DEBUG, message= "Ascension detected")

            if save_section == SaveSection.ASCENSION:

                # Control State
                match parsing_state:

                    case SaveParsingState.INIT:

                        if line_stripped.startswith('"currentRun"'):
                            parsing_state = SaveParsingState.CURRENT_RUN
                            logger.log(level= LOW_DEBUG, message= "Current Run detected")
                    
                    case SaveParsingState.CURRENT_RUN:

                        if line.startswith(FS*2 + "}"):
                            parsing_state = SaveParsingState.INIT
                            logger.log(level= LOW_DEBUG, message= "Current Run parsing complete!")

                        elif parsing_state == SaveParsingState.CURRENT_RUN and line_stripped.startswith('"cardIds"'):
                            parsing_state = SaveParsingState.CARD_IDS
                            logger.log(level= LOW_DEBUG, message= "Parsing cards...")

                        elif line_stripped.startswith('"cardIdModInfos"'):
                            parsing_state = SaveParsingState.CARD_MODS
                            logger.log(level= LOW_DEBUG, message= "Card Mods detected")

                    case SaveParsingState.CARD_IDS:
                        if line_stripped.startswith("]"):
                            parsing_state = SaveParsingState.CURRENT_RUN
                            logger.log(level= LOW_DEBUG, message= "All card IDs parsed")
                    
                    case SaveParsingState.CARD_MODS:
                        if line.startswith(FS*5 + "]"):
                            parsing_state = SaveParsingState.CURRENT_RUN
                        
                        if line.startswith(FS*6 + "{"):
                            parsing_state = SaveParsingState.COLLECTING_MOD_BLOCK
                            capture_mod_lines : list[str] = []

                    case SaveParsingState.COLLECTING_MOD_BLOCK:
                        if line.startswith(FS*6 + "}"):
                            parsing_state = SaveParsingState.CARD_MODS
                            parse_mod_text(mod_text_lines= capture_mod_lines, cards= cards, logger= logger)

                # Collect Data
                match parsing_state:

                    case SaveParsingState.CARD_IDS:
                        if line.startswith(' ' * 24):
                            creature_name = parse_text_between_substrings(line_stripped, '"', '"', logger= logger)
                            creature = Creature(creature_name)
                            cards.append(Card(creature))         
                
                    case SaveParsingState.COLLECTING_MOD_BLOCK:
                        capture_mod_lines.append(line)
                        
    
    logger.log(level= INFO, message= f"Parsed Cards:")
    for card in cards:
        logger.log(level= INFO, message= str(card))
    
    return cards