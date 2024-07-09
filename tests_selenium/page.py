# Import WebDriverWait as W from Selenium
from selenium.webdriver.support.ui import WebDriverWait as W
# Import expected_conditions as EC from Selenium
from selenium.webdriver.support import expected_conditions as EC
# Import locators for different pages
from locators import HomePageLocators, AboutPageLocators, SignalsPageLocators


class BasePage(object):
    """
    BasePage class that contains common methods for interacting with web elements using Selenium WebDriver.
    """

    def __init__(self, driver):
        """
        Initialize BasePage with a WebDriver instance.

        Args:
            driver: WebDriver instance to interact with web elements.
        """
        self.driver = driver

    def do_click(self, locator):
        """
        Perform a click action on the web element identified by the locator.

        Args:
            locator: Locator for finding the web element.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_clear(self, locator):
        """
        Clear the input field identified by the locator.

        Args:
            locator: Locator for finding the input field.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_send_keys(self, locator, text):
        """
        Send keys (text input) to the input field identified by the locator.

        Args:
            locator: Locator for finding the input field.
            text: Text to be sent to the input field.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        """
        Get a single web element identified by the locator.

        Args:
            locator: Locator for finding the web element.

        Returns:
            WebElement: The web element found.
        """
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        """
        Get multiple web elements identified by the locator.

        Args:
            locator: Locator for finding the web elements.

        Returns:
            List[WebElement]: List of web elements found.
        """
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        """
        Get the text content of a web element identified by the locator.

        Args:
            locator: Locator for finding the web element.

        Returns:
            str: Text content of the web element.
        """
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def do_submit(self, locator):
        """
        Submit a form element identified by the locator.

        Args:
            locator: Locator for finding the form element.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()


class HomePage(BasePage):
    """
    HomePage class that extends BasePage and contains methods specific to the home page of MJ TRADING.
    """

    def is_title_matches(self):
        """
        Verify if the current page title matches the expected title for the home page.

        Returns:
            bool: True if the title matches, False otherwise.
        """
        return "MJ TRADING - HOME" in self.driver.title

    def is_about_link_works(self):
        """
        Click on the About link and verify if the page title changes to the expected About page title.

        Returns:
            bool: True if the About link works correctly, False otherwise.
        """
        self.do_click(HomePageLocators.ABOUT_LINK)
        return "MJ TRADING - ABOUT" in self.driver.title

    def is_home_link_works(self):
        """
        Click on the Home link and verify if the page title changes back to the home page title.

        Returns:
            bool: True if the Home link works correctly, False otherwise.
        """
        self.do_click(HomePageLocators.HOME_LINK)
        return "MJ TRADING - HOME" in self.driver.title

    def is_register_form_works(self):
        """
        Fill out and submit the registration form with valid email and password.
        Verify if the registration success message appears.

        Returns:
            bool: True if registration form works correctly, False otherwise.
        """
        self.do_clear(HomePageLocators.EMAIL)
        self.do_clear(HomePageLocators.PASSWORD)
        self.do_send_keys(HomePageLocators.EMAIL, 'mj@gmail.com')
        self.do_send_keys(HomePageLocators.PASSWORD, 'password123')
        self.do_click(HomePageLocators.SUBMIT)
        reg_msg = self.get_element_text(HomePageLocators.REG_HEADING)
        return "THANK YOU MJ@GMAIL.COM FOR REGISTERING!" in reg_msg 

    def click_signals_link(self):
        """
        Click on the Signals link.

        This method navigates to the Signals page.
        """
        self.do_click(HomePageLocators.SIGNALS_LINK)


class AboutPage(BasePage):
    """
    AboutPage class that extends BasePage and contains methods specific to the About page of MJ TRADING.
    """

    def is_title_matches(self):
        """
        Verify if the current page title matches the expected title for the About page.

        Returns:
            bool: True if the title matches, False otherwise.
        """
        return "MJ TRADING - ABOUT" in self.driver.title

    def is_about_heading_displayed(self):
        """
        Verify if the About page heading matches the expected text.

        Returns:
            bool: True if the About page heading is displayed correctly, False otherwise.
        """
        about_heading = self.get_element_text(AboutPageLocators.ABOUT_HEADING)
        return 'DOGS OF THE DOW IS AN INVESTMENT STRATEGY THAT ATTEMPTS TO BEAT THE DOW JONES' in about_heading

class SignalsPage(BasePage):
    """
    SignalsPage class that extends BasePage and contains methods specific to the Signals page of MJ TRADING.
    """

    def is_signals_title_matches(self):
        """
        Verify if the current page title matches the expected title for the Signals page.

        Returns:
            bool: True if the title matches, False otherwise.
        """
        return "MJ TRADING - SIGNALS" in self.driver.title








   
