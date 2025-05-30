import os
import shutil

TEST_DIR = "tests/test-resources/"

def clear():
    remdir(TEST_DIR)


def remdir(dir_path: str):
    shutil.rmtree(dir_path, ignore_errors=True)


def fill_dir():
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)

    os.mkdir(os.path.join(TEST_DIR, "images"))
    with open(os.path.join(TEST_DIR, "config.yaml"), 'w') as cfg:
        cfg.write("token: 123")

def fill_config():
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)

    with open(os.path.join(TEST_DIR, "config.yaml"), 'w') as cfg:
        cfg.write(
            "token: '543534543'\n"
            "name: 'marko'\n"
        )


def fill_config_list():
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)

    with open(os.path.join(TEST_DIR, "config.yaml"), 'w') as cfg:
        cfg.write(
            "token: '543534543'\n"
            "admins:\n"
            "- 5434fsda453\n"
            "- 345333da453\n"
        )