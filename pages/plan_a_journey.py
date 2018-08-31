from typing import Optional

from helpers.file_io import get_the_expected_text

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        return self.env['site']

    locators = {
        'root_element': (By.CSS_SELECTOR, '.widget-wrapper'),
        'from_field_alert': (By.ID, 'InputFrom-error'),
        'to_field_alert': (By.ID, 'InputTo-error'),
        'plan_my_journey': (By.CSS_SELECTOR, '.plan-journey-button'),
        'from_text_field': (By.CSS_SELECTOR, '.jpFrom.tt-input'),
        'to_text_field': (By.CSS_SELECTOR, '.jpTo.tt-input'),
        'change_departure': (By.CSS_SELECTOR, '.change-departure-time'),
        'remove_icon': (
            By.CSS_SELECTOR, '.remove-content-container:not(.empty) a.remove-content'),
        'plan_a_journey_button': (By.ID, 'hp-journey-planner'),
        'close_cookie_message': (By.CSS_SELECTOR, '.close3-icon.hide-text'),

    }  # locators dict

    EXPECTED_TEXT_FILE = 'tfl_expected_text.yaml'
    MAIN_NODE = 'plan_a_journey'

    def _click_and_send_keys(self, element: WebElement, text: str) -> None:
        """Private method to click and send keys with the given text.

            element: The located web element.
            text: The given text.

        """
        element.click()
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.TAB)

    def wait_for_load(self, driver: WebDriver) -> None:
        """Wait until the root element is visible."""
        WebDriverWait(driver=driver, timeout=self.timeout).until(
            visibility_of_element_located(
                locator=self.locators['root_element']))

    def get_from_field_alert(self) -> str:
        """Return the 'From' field alert."""
        return self.driver.find_element(
            *self.locators['from_field_alert']).text

    def get_from_field_text(self) -> str:
        """Return the current text value within the 'From' field."""
        return self.driver.find_element(
            *self.locators['from_text_field']).get_attribute("value")

    def get_to_field_text(self) -> str:
        """Return the current text value within the 'To' field."""
        return self.driver.find_element(
            *self.locators['to_text_field']).get_attribute("value")

    def get_to_field_alert(self) -> str:
        """Return the 'To' field alert."""
        return self.driver.find_element(*self.locators['to_field_alert']).text

    def click_plan_my_journey_button(self) -> str:
        """Click the 'Plan my journey' button."""
        return self.driver.find_element(
            *self.locators['plan_my_journey']).click()

    def click_change_time_text(self) -> str:
        """Click the 'Change time' text."""
        return self.driver.find_element(
            *self.locators['change_departure']).click()

    def click_remove_icon(self) -> str:
        """Click the 'Remove' icon within the 'From' or 'To'."""
        return self.driver.find_element(*self.locators['remove_icon']).click()

    def enter_from_text_value(self, text: str) -> None:
        """Click the 'From' text area and enter given text."""
        element = self.driver.find_element(*self.locators['from_text_field'])
        self._click_and_send_keys(element=element, text=text)

    def enter_to_text_value(self, text: str) -> None:
        """Click the 'To' text area and enter given text."""
        element = self.driver.find_element(*self.locators['to_text_field'])
        self._click_and_send_keys(element=element, text=text)

    def clear_from_field_text(self) -> None:
        """clear the 'From' field text box."""
        self.driver.find_element(*self.locators['from_text_field']).clear()

    def clear_to_field_text(self) -> None:
        """clear the 'To' field text box."""
        self.driver.find_element(*self.locators['to_text_field']).clear()

    def get_expected_from_alert_text(self) -> str:
        """Get the expected alert text for the 'From' field."""
        return get_the_expected_text(file_name=self.EXPECTED_TEXT_FILE,
                                     main_node=self.MAIN_NODE,
                                     second_node='from_text_alert')

    def get_expected_to_alert_text(self) -> str:
        """Get the expected alert text for the 'To' field."""
        return get_the_expected_text(file_name=self.EXPECTED_TEXT_FILE,
                                     main_node=self.MAIN_NODE,
                                     second_node='to_text_alert')

    def from_alert_is_displayed(self) -> bool:
        """Verifys whether the 'from' alert is displayed."""
        try:
            return self.driver.find_element(
                *self.locators['from_field_alert']).is_displayed()
        except NoSuchElementException:
            return False

    def to_alert_is_displayed(self) -> bool:
        """Verifies whether the 'to' alert is displayed."""
        try:
            return self.driver.find_element(
                *self.locators['to_field_alert']).is_displayed()
        except NoSuchElementException:
            return False

    def click_the_plan_a_journey_button(self) -> None:
        """Button appears when screen size is below a certain threshold.

        On smaller screens (i.e. mobile devices) the tfl site then hides
        the 'From' and 'To' fields within a widget-wrapper.  Clicking
        this button exposes the items hidden inside container.


        """
        self.driver.find_element(*self.locators['plan_a_journey_button']).click()

    def cookie_message_is_displayed(self) -> bool:
        """``True`` if the cookie message is displayed ``False`` if not."""
        return self.driver.find_element(
            *self.locators['close_cookie_message']).is_displayed()

    def click_close_cookie_message(self) -> None:
        """Click the close cookie message on the tfl.gov.uk page.

        Sometimes the cookie message will slightly obscure the widget when
        loading the page.  If this happens then the tests will fail.

        """
        self.driver.find_element(*self.locators['close_cookie_message']).click()
