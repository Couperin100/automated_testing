import pytest

from helpers.file_io import read_yaml_file
from helpers.paths import ENVS


@pytest.fixture(scope='session', autouse=True)
def env():
    """Get the environment config options."""
    yield read_yaml_file(ENVS)
