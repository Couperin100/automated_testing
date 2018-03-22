from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located)
from selenium.webdriver.support.ui import WebDriverWait


class PlanJourneySection:
    """Page object for the Plan a Journey section."""

    def __init__(self, driver: WebDriver, env: dict) -> None:
        """Set the required variables."""

        self.driver = driver
        self.env = env
        self.timeout = self.env['timeout']

    @property
    def url(self) -> Optional[str]:
        """Return the expected URL."""
        return self.env['url']

    locators = {
        'root_element': (By.CSS_SELECTOR, '.widget-wrapper'),
        'from_field': (By.ID, 'InputFrom-error'),
        'to_field': (By.ID, 'InputTo-error'),
    }  # locators dict

    def wait_for_load(self, driver: WebDriver) -> None:
        """Wait until the root element is visible."""
        WebDriverWait(driver=driver, timeout=self.timeout).until(
            visibility_of_element_located(
                locator=self.locators['root_element']))

    def get_from_field_alert(self) -> str:
        """Return the 'From' field alert."""
        return self.driver.find_element(*self.locators['from_field']).text

    def get_to_field_alert(self) -> str:
        """Return the 'To' field alert."""
        return self.driver.find_element(*self.locators['to_field']).text
