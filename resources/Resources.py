import os

from resources.ensure import ensure_directory
from resources.const import (
    RESOURCES_DIRECTORY
)


class Resources:
    def __init__(self, dir_path: str = RESOURCES_DIRECTORY):
        self._path = dir_path
        ensure_directory(self._path)


    def list(self, *, full_paths: bool = False) -> list[str]:
        """ Get list of resources paths """
        names = os.listdir(self._path)

        if full_paths:
            return [os.path.join(self._path, n) for n in names]
        else:
            return names


    def has(self, name_or_path: str) -> bool:
        return name_or_path in self.list() \
            or name_or_path in self.list(full_paths=True)

    
    def get_str(self, name_or_path: str) -> str:
        if not self.has(name_or_path):
            return None

        if self._path not in name_or_path:
            name_or_path = os.path.join(self._path, name_or_path)
            
        with open(name_or_path, 'r', encoding='utf-8') as file:
            return file.read()
        