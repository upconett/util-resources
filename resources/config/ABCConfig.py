import os
from abc import ABC, abstractmethod

from .exceptions import NoConfigFile, KeyUndefined


class ABCConfig(ABC):
    def __init__(self, conf_path: str):
        self._path = conf_path
        self._check_no_config_file()
        self._check_undefined_keys()
        self._populate_keys()
        
    def _get_annotated(self) -> list[str]:
        return self.__class__.__annotations__.keys()

    def _undefined_keys(self, data: dict) -> list[str]:
        undefined_keys = []
        annotated_keys = self._get_annotated()
        for key in annotated_keys:
            if data.get(key) is None:
                undefined_keys.append(key)
        return undefined_keys

    def _populate_keys(self):
        annotated_keys = self.__class__.__annotations__.keys()
        for key, value in self._get_data().items():
            if key in annotated_keys:
                setattr(self, key, value)

    def _write_default(self):
        annotated_keys = self._get_annotated()
        data = self._get_data()
        values = [data.get(key) for key in annotated_keys]
        self._write_data(dict(zip(annotated_keys, values)))

    def _check_no_config_file(self):
        if not os.path.exists(self._path):
            self._write_default()
            raise NoConfigFile
        
    def _check_undefined_keys(self):
        if uk := self._undefined_keys(self._get_data()):
            self._write_default()
            raise KeyUndefined(uk[0])


    @abstractmethod
    def _get_data(self) -> dict:
        """ Have to return {} if file not exists """
        ...

    @abstractmethod
    def _write_data(self, data: dict): ...
