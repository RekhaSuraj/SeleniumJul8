import pytest
# Fixtures
# To execute a function before the required test, we use fixtures

# Here's a breakdown of what fixtures entail in Selenium:
# Setup and Teardown:
# Fixtures handle the "arrange" phase of a test, which involves setting up the necessary prerequisites before a test runs, and the "teardown" phase, which cleans up resources after the test completes. For Selenium, this often includes:
# Browser Initialization: Launching a web browser (e.g., Chrome, Firefox) and initializing the WebDriver instance.
# URL Navigation: Opening a specific URL or navigating to a particular page.
# Test Data Preparation: Setting up or loading test data, such as creating user accounts or populating a database.
# Browser Termination: Closing the browser and quitting the WebDriver instance.

# practice website
# driver.get("https://pos.aksharatraining.in/pos/public/")
@pytest.fixture(autouse=True)
def login():
    print('Login to app') #pre condition
    yield
    print('Logout from app') #post condition


def test_create_customer():
    print('create customer')


def test_delete_customer():
    print('delete customer')


# collecting ... collected 2 items
#
# test_demo4.py::test_create_customer Login to app
# PASSED                               [ 50%]create customer
# Logout from app
#
# test_demo4.py::test_delete_customer Login to app
# PASSED                               [100%]delete customer
# Logout from app
