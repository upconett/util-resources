import json
from contextlib import contextmanager
from typing import Generator, TextIO
from abc import ABC

from .ABCConfig import ABCConfig
from .exceptions import NoConfigFile


class JSONConfig(ABCConfig, ABC):

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
                return json.load(file)
        except NoConfigFile:
            return {}

    def _write_data(self, data: dict):
        with self._open_file('w') as file:
            json.dump(data, file,
                ensure_ascii=False,
                indent=2
            )
