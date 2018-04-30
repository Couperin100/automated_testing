import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from helpers.file_io import read_yaml_file
from helpers.paths import ENVS


def pytest_addoption(parser):
    """Add options to use when running the tests."""

    parser.addoption(
        '--browser', dest='browser', action='store',
        help='Specify the browser you want to use'
    )


def _provision_chrome():
    """Provision Chrome driver."""
    driver = webdriver.Chrome()
    return driver


def _provision_firefox():
    """Provision Firefox driver."""
    capabilities = DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False
    driver = webdriver.Firefox(capabilities=capabilities)
    return driver


@pytest.fixture(scope='session', autouse=True)
def env():
    """Get the environment config options."""
    yield read_yaml_file(ENVS)


@pytest.fixture(scope='session', autouse=True)
def driver():
    """Provisioning a driver based on pytest command line parameter."""
    browsers = {
        'chrome': _provision_chrome,
        'firefox': _provision_firefox,
    }
    browser = pytest.config.option.browser
    _driver = browsers[browser]()
    yield _driver
    _driver.quit()
