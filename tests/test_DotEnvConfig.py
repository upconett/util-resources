import pytest

from resources import Resources
from resources.config import DotEnvConfig
from resources.config import (
    InvalidAnnotation,
    NoConfigFile,
    KeyUndefined
)

from tests.utility import (
    TEST_DIR,
    fill_config_env,
    clear
)


def test_read():
    fill_config_env()

    class Config(DotEnvConfig):
        token: str
        limit: int

    res = Resources(TEST_DIR)
    cfg = Config(res.path_to(".env"))

    assert cfg.token == "123"
    assert cfg.limit == 5

    clear()


def test_valid_annotations():
    fill_config_env()

    class Config(DotEnvConfig):
        token: str
        limit: int
        threshold: float
    
    res = Resources(TEST_DIR)
    Config(res.path_to(".env"))

    class Config(DotEnvConfig):
        admins: list[str]
        resours: Resources

    with pytest.raises(InvalidAnnotation):
        Config(res.path_to(".env"))

    clear()


def test_generate_default():
    class Config(DotEnvConfig):
        token: str
        limit: int
        threshold: float

    res = Resources(TEST_DIR)

    with pytest.raises(NoConfigFile):
        Config(res.path_to(".env"))

    with pytest.raises(KeyUndefined):
        Config(res.path_to(".env"))
    
    clear()


clear()
