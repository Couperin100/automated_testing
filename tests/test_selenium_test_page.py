from functools import partial
from pytest import fixture
from pytest_bdd import given, parsers, then, scenario, when

from selenium.webdriver.remote.webdriver import WebDriver

from pages.selenium_test_page import SeleniumTestPage


scenario = partial(scenario, '../feature/selenium_test_page.feature')


@scenario('I submit the form in its default state')
def test_i_submit_the_form_in_its_default_state():
    """I submit the form in its default state."""
    pass


@scenario('I submit the form with a username and password')
def test_i_submit_the_form_with_username_and_password():
    """I submit the form with a username and password."""
    pass


@given('I am on the Selenium Test Page')
def i_am_on_the_selenium_test_page(driver: WebDriver, env: dict):
    """Given I am on the Selenium test page."""
    page = SeleniumTestPage(driver, env)
    driver.get(env['site'])
    page.wait_for_load(driver=driver)
    print(f"Page url is: {page.url}")


@when("I click on the submit button")
def i_click_on_the_submit_button(driver: WebDriver, env: dict):
    """Click on the 'submit' button."""
    page = SeleniumTestPage(driver, env)
    page.click_submit_button()


@then("I should see the title 'Submitted Values'")
def i_should_see_the_title_submitted_values(driver: WebDriver, env: dict):
    """Assert that the page title is correct."""
    page = SeleniumTestPage(driver, env)
    assert page.get_title() == page.get_expected_text(text='title')
    print(f"Page title has been verified!")


@then("I should see <value> on the results page")
def i_should_see_value_on_the_results_page(
        driver: WebDriver, env: dict, value: str):
    """Assert that the results page has the correct values set."""
    page = SeleniumTestPage(driver, env)
    page_value = page.get_result_value_by_text(value)
    expected_value = page.get_expected_text(text=value)
    assert page_value == expected_value
    print(f"Page value: '{page_value}' matches the localised expected text.")


@fixture
@when(parsers.parse("I enter the username '{username}' into the form"))
def i_enter_a_username_into_the_form(
        driver: WebDriver, env: dict, username: str, module_context: dict):
    """Entering a username into the form."""
    page = SeleniumTestPage(driver, env)
    page.enter_text_into_the_username_field(username=username)
    module_context['username'] = username



@fixture
@when(parsers.parse("I enter the password '{password}' into the form"))
def i_enter_a_password_into_the_form(
        driver: WebDriver, env: dict, password: str, module_context: dict):
    page = SeleniumTestPage(driver, env)
    page.enter_text_into_the_password_field(password=password)
    module_context['password'] = password


@then("I should see the correct value for the username")
def i_should_see_the_correct_value_for_the_username(
        driver: WebDriver, env: dict, module_context: dict):
    """Assert that the correct value for the username has been set."""
    page = SeleniumTestPage(driver, env)
    username_value = page.get_result_value_by_text(module_context['username'])
    assert username_value == module_context['username']
    print(f"Username value: '{module_context['username']}' has been verified!")


@then("I should see the correct value for the password")
def i_should_see_the_correct_value_for_the_password(
        driver: WebDriver, env: dict, module_context: dict):
    """Assert that the correct value for the password has been set."""
    page = SeleniumTestPage(driver, env)
    password_value = page.get_result_value_by_text(module_context['password'])
    assert password_value == module_context['password']
    print(f"Password value: '{module_context['password']}' has been verified!")


@then("I should not see a value for the username")
def i_should_not_see_a_value_for_the_username(driver: WebDriver, env: dict):
    """Assert that there is no value for the username."""
    page = SeleniumTestPage(driver, env)
    page_value = page.get_result_value_by_text('No Value for username')
    expected_value = page.get_expected_text(text='No Value for username')
    assert page_value == expected_value
    print(f"Page value: '{page_value}' matches the localised expected text.")


@then("I should not see a value for the password")
def i_should_not_see_a_value_for_the_password(driver: WebDriver, env: dict):
    """Assert that there is no value for the password."""
    page = SeleniumTestPage(driver, env)
    page_value = page.get_result_value_by_text('No Value for password')
    expected_value = page.get_expected_text(text='No Value for password')
    assert page_value == expected_value
    print(f"Page value: '{page_value}' matches the localised expected text.")
