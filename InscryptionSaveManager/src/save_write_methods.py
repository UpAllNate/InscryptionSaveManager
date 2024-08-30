from card_classes import Card, CardModConfig
from save_parse_methods import parse_text_between_substrings
from project_logger import ProjectLogger, INFO
import os

def formatted_true_false(i : bool) -> str:
    if i:
        return 'true'
    else:
        return 'false'

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

def write_save_file(save_file_path : str, cards : list[Card], logger : ProjectLogger) -> None:

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
                id = int(parse_text_between_substrings(line, first= '"$id": ', second= ",", logger= logger))

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


def handle_save_write(cards : list[Card], save_file_path : str, write_necessary : bool, logger : ProjectLogger) -> None:
    global last_modified

    if write_necessary:
        write_save_file(save_file_path= save_file_path, cards= cards, logger= logger)
        last_modified = os.path.getmtime(save_file_path)
        
        logger.log(level= INFO, message= f"{'#' * 20} Cards written:")
        for card in cards:
            logger.log(INFO, message= str(card))