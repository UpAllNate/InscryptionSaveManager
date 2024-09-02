
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
    file_logger_name= __file__ + "meta_file", file_log_level= LOW_DEBUG, file_log_format_string= standard_file_format_string,
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

from challenges import ChallengeManager, Challenge_Sigil_Adder

with open('filepath.txt', 'r') as f:
    for line in f:
        if "inscryption" in line.lower():
            save_file_path = line.strip()

challenge_manager = ChallengeManager(
    challenges= [
        Challenge_Sigil_Adder(
            meta_logger= meta_logger,
            ui_logger= ui_logger
        )
    ]
)

while True:

    if save_file_changed(save_file_path, meta_logger):

        clear_term()

        cards = parse_save_file(save_file_path, meta_logger)

        write_necessary = challenge_manager.run(cards)
        # write_necessary = True
        handle_save_write(cards, 'SaveFile.gwsave', write_necessary, meta_logger)

    time.sleep(1)