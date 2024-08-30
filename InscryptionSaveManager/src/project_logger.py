from termcolor_files import color_text, Color, Attribute
import logging
from logging.handlers import RotatingFileHandler
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET
import re
import datetime

LOW_DEBUG = 5
logging.addLevelName(LOW_DEBUG, "LODEBUG")

# Utility to strip ANSI codes
def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

class ColorFormatter(logging.Formatter):
    """Custom formatter to add colors only to the log level name and numbers in the message."""

    last_log_time = None  # static variable to keep track of the last log time

    def __init__(self, fmt=None, datefmt='%H:%M:%S', style='%'):
        super().__init__(fmt, datefmt, style)

    def formatTime(self, record, datefmt=None):
        ct = datetime.datetime.fromtimestamp(record.created)
        formatted_time = ct.strftime(self.datefmt)

        # Determine the color based on the time difference
        current_time = datetime.datetime.now()
        if ColorFormatter.last_log_time:
            elapsed_time = (current_time - ColorFormatter.last_log_time).total_seconds()
        else:
            elapsed_time = 0  # Default color for the first log

        # Update the last log time
        ColorFormatter.last_log_time = current_time

        # Decide the color based on elapsed time
        if elapsed_time < 3:
            color = Color.WHITE
        elif elapsed_time < 30:
            color = Color.LIGHT_MAGENTA
        else:
            color = Color.RED

        # Apply the color to the timestamp
        colored_time = color_text(formatted_time, color=color)
        return colored_time

    def format(self, record):
        new_record = logging.makeLogRecord(record.__dict__)
        new_record.levelname = f"{new_record.levelname:->7}"
        if len(new_record.levelname) > 7:
            new_record.levelname = new_record.levelname[:7]

        # Apply color to level names (assuming the mappings are correctly set)
        color_map = {
            LOW_DEBUG: Color.WHITE,
            logging.DEBUG: Color.LIGHT_CYAN,
            logging.INFO: Color.GREEN,
            logging.WARNING: Color.YELLOW,
            logging.ERROR: Color.RED,
            logging.CRITICAL: Color.RED
        }
        new_record.levelname = color_text(new_record.levelname, color=color_map.get(new_record.levelno, Color.WHITE))

        return super().format(new_record)

class CleanFormatter(logging.Formatter):
    """Formatter that removes ANSI color codes for file logging."""
    def format(self, record):
        record.msg = strip_ansi_codes(record.msg)
        return super().format(record)

standard_file_format_string = '[%(asctime)s] [%(levelname)s] [%(name)s {%(module)s:%(lineno)d}] %(message)s'
standard_stream_format_string = '%(levelname)s %(asctime)s: %(message)s'

message_only_format_string = '%(message)s'

class ProjectLogger:

    def __init__(self,
        file_logger_name : str,
        file_log_level : int,
        file_log_format_string : str,
        file_filename : str,
        file_max_size : int,
        file_backup_count : int,
        stream_logger_name : str,
        stream_log_level : int,
        stream_log_format_string : str
    ) -> None:

        # Setup loggers and handlers
        self.file_logger = logging.getLogger(file_logger_name)
        self.stream_logger = logging.getLogger(stream_logger_name)
        self.file_logger.setLevel(file_log_level)
        self.stream_logger.setLevel(stream_log_level)

        self.file_handler = RotatingFileHandler(file_filename, maxBytes=file_max_size, backupCount=file_backup_count)
        self.clean_formatter = CleanFormatter(file_log_format_string)

        self.file_handler.setFormatter(self.clean_formatter)
        self.file_logger.addHandler(self.file_handler)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(ColorFormatter(stream_log_format_string))
        self.stream_logger.addHandler(self.console_handler)

    def log(
        self,
        level = logging.DEBUG,
        message : str = None,
        file_text_header : str = None,
        file_text_footer : str = None
    ) -> None:

        if message:
            try:
                message = message.strip()
            except:
                pass

        if file_text_header:
            file_text_header = file_text_header.strip()

        if file_text_footer:
            file_text_footer = file_text_footer.strip()

        if message:
            if file_text_header:
                if file_text_footer:
                    file_text = "\n".join((file_text_header, message, file_text_footer))
                else:
                    file_text = "\n".join((file_text_header, message))

            else:
                if file_text_footer:
                    file_text = "\n".join((message, file_text_footer))
                else:
                    file_text = message

        else:
            if file_text_header:
                if file_text_footer:
                    file_text = "\n".join((file_text_header, file_text_footer))
                else:
                    file_text = file_text_header

            else:
                if file_text_footer:
                    file_text = file_text_footer
                else:
                    self.file_logger.error("Empty log entry")
                    return

            message = file_text

        self.stream_logger.log(level, message, stacklevel=2)
        self.file_logger.log(level, file_text, stacklevel=2)

logger = ProjectLogger(
    file_logger_name= __name__ + "__FILE__", file_log_level= INFO,
    file_log_format_string= standard_file_format_string,
    file_filename= __name__ + ".log", file_max_size= 10 * 1024 * 1024, file_backup_count= 0,
    stream_logger_name= __name__ + "__STREAM__", stream_log_level= INFO, stream_log_format_string= standard_stream_format_string
)

if __name__ == "__main__":

    if "\\" in __file__:
        name = __file__.split("\\")[-1]
    else:
        name = __file__

    test_logger = ProjectLogger(
        file_logger_name = name + "_file",
        file_log_level = 1,
        file_log_format_string= standard_file_format_string,
        file_filename = name + ".log",
        file_max_size = 10 * 1024, # 10 kB
        file_backup_count = 0,
        stream_logger_name = __name__[0] + "_stream",
        stream_log_level = DEBUG,
        stream_log_format_string= standard_stream_format_string
    )

    msg = f"This is a test of the {color_text(text= 'emergency broadcast system', color= Color.WHITE, on_color= Color.RED, attrs= [Attribute.BOLD])}"
    test_logger.log(level=INFO, message=msg, file_text_header="This is indeed very important info.")
    test_logger.log(level=DEBUG, message="This is a console message", file_text_header="This is a file message")
    test_logger.log(level=LOW_DEBUG, message="This is for file eyes only")
    test_logger.log(level=WARNING, file_text_header="Detailed warning information here.")
    test_logger.log(level=ERROR, message= "This is getting serious")
    test_logger.log(level=CRITICAL, message= "Oh... now it's serious...")
