import os
import shutil

from resources import Resources


TEST_DIR = "tests/test-resources/"


# region tests

def test_create_dir():
    Resources(TEST_DIR)
    assert os.path.exists(TEST_DIR)
    remdir(TEST_DIR)


def test_list():
    res = Resources(TEST_DIR)

    assert res.list() == [] # empty directory

    fill_dir() # filling directory with something
    assert res.list() == ["images", "config.yaml"]

    clear()


def test_list_full_paths():
    res = Resources(TEST_DIR)

    assert res.list(full_paths=True) == [] # empty directory

    test_paths = [
        os.path.join(TEST_DIR, "images"),
        os.path.join(TEST_DIR, "config.yaml")
    ]
    fill_dir() # filling directory with something
    assert res.list(full_paths=True) == test_paths

    clear()


def test_has():
    res = Resources(TEST_DIR)

    assert not res.has("something")

    fill_dir()
    assert res.has("images")
    assert res.has(os.path.join(TEST_DIR, "images"))

    assert res.has("config.yaml")
    assert res.has(os.path.join(TEST_DIR, "config.yaml"))

    clear()


def test_get_str():
    res = Resources(TEST_DIR)
    
    fill_dir()
    assert res.get_str("config.yaml") == "token=123"

    clear()

# endregion


# region utility

def clear():
    remdir(TEST_DIR)


def remdir(dir_path: str):
    shutil.rmtree(dir_path, ignore_errors=True)


def fill_dir():
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)

    os.mkdir(os.path.join(TEST_DIR, "images"))
    with open(os.path.join(TEST_DIR, "config.yaml"), 'w') as cfg:
        cfg.write("token=123")

# endregion


clear()
