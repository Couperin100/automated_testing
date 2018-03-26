from functools import partial
from pytest_bdd import given, then, scenario, when
from pytest import fixture

from selenium import webdriver

from pages.plan_a_journey import PlanJourneySection

scenario = partial(scenario, '../feature/plan_a_journey_alerts.feature')

DRIVER = webdriver.Chrome()
FROM_ALERT_TEXT = "The From field is required."
TO_ALERT_TEXT = "The To field is required."


@fixture(scope='module')
def suite_setup(env: dict):
    DRIVER.get(env['site'])
    yield
    DRIVER.quit()


@scenario('I do not enter a station into the From field')
def test_i_do_not_enter_a_station_into_from_field(suite_setup):
    """I do not enter a station into the 'From' field."""
    pass


@scenario('I do not enter a station into the To field')
def test_i_do_not_enter_a_station_into_to_field(suite_setup):
    """I do not enter a station into the 'To' field."""
    pass


@scenario('I do not enter a station into the To or From field')
def test_i_do_not_enter_a_station_into_to_or_from_field(suite_setup):
    """I do not enter a station into the 'From' or 'To' field."""
    pass


@given('I am on the TFL website')
def i_am_on_the_tfl_website(env: dict):
    """Verify I am on the correct page."""
    if DRIVER.current_url != PlanJourneySection(DRIVER, env).url:
        DRIVER.switch_to.window(env['site'])


@given("I leave the 'From' field empty")
def i_leave_the_from_field_empty(env: dict):
    """Clear the 'From' field text."""
    PlanJourneySection(DRIVER, env).clear_from_field_text()


@given("I leave the 'To' field empty")
def i_leave_the_to_field_empty(env: dict):
    """Clear the 'To' field text."""
    PlanJourneySection(DRIVER, env).clear_to_field_text()


@when("I click on the plan my journey button")
def i_click_on_the_plan_my_journey_button(env: dict):
    """Click on the 'plan_my_journey' button."""
    PlanJourneySection(DRIVER, env).click_plan_my_journey_button()


@then("I should see the alert 'The From field is required'")
def i_should_see_alert_from_field_required(env: dict):
    """Assert that the 'From' alert has the expected text."""
    assert (PlanJourneySection(
        DRIVER, env).get_from_field_alert() == FROM_ALERT_TEXT)


@then("I should see the alert 'The To field is required'")
def i_should_see_alert_to_field_required(env: dict):
    """Assert that the 'To' alert has the expected text."""
    assert (PlanJourneySection(
        DRIVER, env).get_to_field_alert() == TO_ALERT_TEXT)
