import pytest

from resources.config import YAMLConfig, NoConfigFile, KeyUndefined
from resources import Resources
from tests.utility import (
    TEST_DIR,
    clear,
    fill_config
)


def test_NoConfig():
    res = Resources(TEST_DIR)

    class Config(YAMLConfig):
        token: str
        
    with pytest.raises(NoConfigFile):
        Config(res.path_to("config.yaml"))

    clear()
    

def test_KeyUndefined():
    res = Resources(TEST_DIR)

    class Config(YAMLConfig):
        token: str

    with pytest.raises(NoConfigFile):
        Config(res.path_to("config.yaml"))

    with pytest.raises(KeyUndefined):
        Config(res.path_to("config.yaml"))

    clear()


def test_keys():
    res = Resources(TEST_DIR)

    class Config(YAMLConfig):
        token: str
        name: str

    fill_config()

    cfg = Config(res.path_to("config.yaml"))

    assert cfg.token == "543534543"
    assert cfg.name == "marko"

    clear()
    

clear()
