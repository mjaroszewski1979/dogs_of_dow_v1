# Import WebDriver from Selenium
from selenium import webdriver
# Import unittest module for test case support
import unittest
# Import page module containing page object classes
import page


class TestBase(unittest.TestCase):
    """
    Base test case class that sets up and tears down the WebDriver instance for Selenium tests.
    """
    
    def setUp(self):
        """
        Set up method to initialize the WebDriver instance before each test method.
        """

        # Initialize Chrome WebDriver
        self.driver =  webdriver.Chrome('chromedriver.exe')
        # Set window size for consistent testing environment
        self.driver.set_window_size(1920, 1080)

    def tearDown(self):
        """
        Tear down method to close the WebDriver instance after each test method.
        """

        # Close the WebDriver instance
        self.driver.close()


class SeleniumTest(TestBase):
    """
    Test case class that defines Selenium tests for various pages of MJ TRADING.
    """
        
    def test_home_page(self):
        """
        Test method to verify functionality of the home page of MJ TRADING.
        """

        # Open the home page URL
        self.driver.get('http://127.0.0.1:8000')
        # Initialize HomePage object with WebDriver instance
        home_page = page.HomePage(self.driver)
        # Check if home page title matches
        assert home_page.is_title_matches()
        # Check if About link works
        assert home_page.is_about_link_works()
        # Check if Home link works
        assert home_page.is_home_link_works()
        # Check if registration form works
        assert home_page.is_register_form_works()

    def test_signals_page(self):
        """
        Test method to verify functionality of the signals page of MJ TRADING.
        """

        # Open signals page URL
        self.driver.get("http://mj%40gmail.com:password123@127.0.0.1:8000/signals")
        # Initialize SignalsPage object with WebDriver instance
        signals_page = page.SignalsPage(self.driver)
        # Check if signals page title matches
        assert signals_page.is_signals_title_matches()

    def test_about_page(self):
        """
        Test method to verify functionality of the about page of MJ TRADING.
        """

        # Open the about page URL
        self.driver.get('http://127.0.0.1:8000/about')
        # Initialize AboutPage object with WebDriver instance
        about_page = page.AboutPage(self.driver)
        # Check if about page title matches
        assert about_page.is_title_matches()
        # Check if about page heading is displayed
        assert about_page.is_about_heading_displayed()

        
if __name__ == '__main__':
    # Run the unittest framework to execute the test cases
    unittest.main()




        
