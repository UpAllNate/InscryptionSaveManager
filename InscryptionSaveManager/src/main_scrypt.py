
from project_logger import (
    ProjectLogger,
    color_text,
    Color,
    Attribute,
    LOW_DEBUG,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    standard_file_format_string,
    standard_stream_format_string,
    message_only_format_string
)

meta_logger = ProjectLogger(
    file_logger_name= __file__ + "meta_file", file_log_level= DEBUG, file_log_format_string= standard_file_format_string,
    file_filename= __file__ + "_meta.log", file_max_size= 10 * 1024 * 1024, file_backup_count= 0,
    stream_logger_name= __file__ + "meta_stream", stream_log_level= ERROR, stream_log_format_string= standard_stream_format_string
)

ui_logger = ProjectLogger(
    file_logger_name= __file__ + "ui_file", file_log_level= DEBUG, file_log_format_string= message_only_format_string,
    file_filename= __file__ + "_ui.log", file_max_size= 10 * 1024, file_backup_count= 0,
    stream_logger_name= __file__ + "ui_stream", stream_log_level= INFO, stream_log_format_string= message_only_format_string
)


import os
def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')

import time

from save_monitoring_methods import save_file_changed
from save_parse_methods import parse_save_file
from save_write_methods import handle_save_write

from challenges import challenge_card_randomizer, challenge_stat_clamp

with open('filepath.txt', 'r') as f:
    for line in f:
        if "inscryption" in line.lower():
            save_file_path = line.strip()

while True:

    if save_file_changed(save_file_path, meta_logger):

        clear_term()

        cards = parse_save_file(save_file_path, meta_logger)

        # logger.log(level= INFO, message= f"{'#' * 20} Cards parsed:")
        # for card in cards:
        #     logger.log(INFO, message= str(card))

        write_necessary = challenge_card_randomizer(cards, ui_logger)
        handle_save_write(cards, save_file_path, write_necessary, meta_logger)

    time.sleep(1)