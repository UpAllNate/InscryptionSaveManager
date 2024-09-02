from project_logger import ProjectLogger, INFO
import os

last_modified = None
def save_file_changed(save_file_path : str, logger : ProjectLogger) -> bool:
    global last_modified

    current_modified = os.path.getmtime(save_file_path)
    if last_modified is None:
        last_modified = current_modified
    if current_modified != last_modified:
        time_diff_seconds = abs(current_modified - last_modified)
        last_modified = current_modified
        logger.log(INFO, f"{'#' * 20} File save detected")
        return time_diff_seconds > 10
    return False