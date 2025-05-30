import dotenv
from contextlib import contextmanager
from typing import Generator, TextIO
from abc import ABC

from .ABCConfig import ABCConfig
from .exceptions import NoConfigFile, InvalidAnnotation


class DotEnvConfig(ABCConfig, ABC):
    """ Config working with dotenv files

    Valid Annotations:
    - `str`
    - `int`
    - `float`
    """

    def __init__(self, conf_path: str):
        self._check_valid_annotations()
        super().__init__(conf_path)

    def _check_valid_annotations(self):
        annotations = self._get_annotations()
        for a in annotations.values():
            if a not in (int, str, float):
                raise InvalidAnnotation(DotEnvConfig, a)


    def _populate_keys(self):
        annotations = self._get_annotations()
        for key, value in self._get_data().items():
            if key in annotations:
                type_to_cast = annotations[key]
                setattr(self, key, type_to_cast(value))


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
                return dict([
                    (key, value if value != '' else None)
                    for key, value
                    in dotenv.dotenv_values(stream=file).items()
                ])
        except NoConfigFile:
            return {}
        
    def _write_data(self, data: dict):
        with self._open_file('w') as file:
            file.writelines([
                f"{key} = {value if value else ''}\n" 
                for key, value in data.items()
            ])
