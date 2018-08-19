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
    driver = webdriver.Firefox(capabilities=capabilities)
    return driver


def _provision_safari():
    """Provision Safari driver."""
    driver = webdriver.Safari()
    return driver


def _provision_ios():
    """Provision iOS driver."""
    capabilities = DesiredCapabilities().IPHONE
    capabilities['browserName'] = 'Safari'
    capabilities['deviceName'] = 'iPhone 7'
    capabilities['platformVersion'] = '11.4'
    capabilities['platformName'] = 'iOS'
    capabilities['nativeWebTap'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
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
        'ios': _provision_ios,
        'safari': _provision_safari,
    }
    browser = pytest.config.option.browser
    _driver = browsers[browser]()
    yield _driver
    _driver.quit()
