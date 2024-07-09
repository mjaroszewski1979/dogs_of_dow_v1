# Importing By from Selenium WebDriver for locating elements
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """
    Class containing locators for elements on the Home page of DOGS OF DOW.
    """

    # Locator for the About link element
    ABOUT_LINK = (By.CLASS_NAME, 'about-link')
    # Locator for the Home link element
    HOME_LINK = (By.CLASS_NAME, 'home-link')
    # Locator for the Email input element
    EMAIL = (By.NAME, 'email')
    # Locator for the Password input element
    PASSWORD = (By.NAME, 'password')
    # Locator for the Submit button element
    SUBMIT = (By.CLASS_NAME, 'button')
    # Locator for the Registration heading element
    REG_HEADING = (By.CLASS_NAME, 'reg-heading')
    # Locator for the Signals link element
    SIGNALS_LINK = (By.CLASS_NAME, 'signals-link')

class AboutPageLocators(object):
    """
    Class containing locators for elements on the About page of MJ TRADING.
    """

    # Locator for the About page heading element
    ABOUT_HEADING = (By.CLASS_NAME, 'about-heading')





