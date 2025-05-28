import os
import logging


def ensure_directory(dir_path: str):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        logging.debug(f"Dir {dir_path} created")
        
