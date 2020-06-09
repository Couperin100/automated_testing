from typing import List

from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from helpers.file_io import get_the_expected_text


class SeleniumTestPage:
    """Page object for the Selenium Test Page."""

    def __init__(self, driver: WebDriver, env: dict) -> None:
        """Set the required variables."""

        self.driver = driver
        self.env = env
        self.timeout = self.env['timeout']
        self.lang = self.env['language']

    @property
    def url(self) -> str:
        """Return the expected URL."""
        return self.env['site']

    locators = {
        "page": (By.TAG_NAME, "html"),
        "submit_button": (By.CSS_SELECTOR, 'input[type="submit"]'),
        "title": (By.CSS_SELECTOR, 'p:first-child'),
        "value_titles": (By.CSS_SELECTOR, "strong, ul"),
        "username_field": (By.NAME, "username"),
        "password_field": (By.NAME, "password"),
        "username_value": (By.ID, "_valueusername"),
        "password_value": (By.ID, "_valuepassword")


    }  # locators dict

    EXPECTED_TEXT_FILE = 'expected_text.yaml'
    MAIN_NODE = 'selenium_test_page'

    def wait_for_load(self, driver: WebDriver) -> None:
        """Wait until the root element is visible."""
        WebDriverWait(driver=driver, timeout=self.timeout).until(
            visibility_of_element_located(
                locator=self.locators['submit_button']))

    def click_submit_button(self) -> None:
        """Click the submit button."""
        self.driver.find_element(*self.locators['submit_button']).click()

    def get_title(self) -> str:
        """Get the title of the results page."""
        return self.driver.find_element(*self.locators['title']).text

    def get_expected_text(self, text: str) -> str:
        """Get the expected text."""
        return get_the_expected_text(file_name=self.EXPECTED_TEXT_FILE,
                                     language=self.lang,
                                     main_node=self.MAIN_NODE,
                                     second_node=text)

    def __get_all_result_values(self) -> List[WebElement]:
        """Get all the result values from the results page."""
        return self.driver.find_elements(*self.locators['value_titles'])

    def get_result_value_by_text(self, text: str) -> str:
        """Get the result value by the given text."""
        elements = self.__get_all_result_values()
        return [i.text for i in elements if i.text == text].pop()

    def enter_text_into_the_username_field(self, username) -> None:
        """Enter the given text into the username field."""
        self.driver.find_element(
            *self.locators['username_field']).send_keys(username)

    def enter_text_into_the_password_field(self, password) -> None:
        """Enter the given text into the password field."""
        self.driver.find_element(
            *self.locators['password_field']).send_keys(password)
