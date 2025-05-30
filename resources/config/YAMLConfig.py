import yaml
from contextlib import contextmanager
from typing import Generator, TextIO
from abc import ABC

from .ABCConfig import ABCConfig
from .exceptions import NoConfigFile


class YAMLConfig(ABCConfig, ABC):

    @contextmanager
    def _open_file(self, mode: str) -> Generator[TextIO]:
        try:
            with open(self._path, mode, encoding="utf-8") as file:
                yield file
        except FileNotFoundError:
            raise NoConfigFile

    def _get_data(self) -> dict:
        try:
            with self._open_file('r') as file:
                return yaml.safe_load(file)
        except NoConfigFile:
            return {}

    def _write_data(self, data: dict):
        with self._open_file('w') as file:
            yaml.safe_dump(data, file)
