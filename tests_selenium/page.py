from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators, AboutPageLocators, SignalsPageLocators



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()


class HomePage(BasePage):

    def is_title_matches(self):
        return "MJ TRADING - HOME" in self.driver.title

    def is_about_link_works(self):
        self.do_click(HomePageLocators.ABOUT_LINK)
        return "MJ TRADING - ABOUT" in self.driver.title

    def is_home_link_works(self):
        self.do_click(HomePageLocators.HOME_LINK)
        return "MJ TRADING - HOME" in self.driver.title

    def is_register_form_works(self):
        self.do_clear(HomePageLocators.EMAIL)
        self.do_clear(HomePageLocators.PASSWORD)
        self.do_send_keys(HomePageLocators.EMAIL, 'mj@gmail.com')
        self.do_send_keys(HomePageLocators.PASSWORD, 'password123')
        self.do_click(HomePageLocators.SUBMIT)
        reg_msg = self.get_element_text(HomePageLocators.REG_HEADING)
        return "THANK YOU MJ@GMAIL.COM FOR REGISTERING!" in reg_msg 

    def click_signals_link(self):
        self.do_click(HomePageLocators.SIGNALS_LINK)



class AboutPage(BasePage):

    def is_title_matches(self):
        return "MJ TRADING - ABOUT" in self.driver.title

    def is_about_heading_displayed(self):
        about_heading = self.get_element_text(AboutPageLocators.ABOUT_HEADING)
        return 'DOGS OF THE DOW IS AN INVESTMENT STRATEGY THAT ATTEMPTS TO BEAT THE DOW JONES' in about_heading

class SignalsPage(BasePage):

    def is_signals_title_matches(self):
        return "MJ TRADING - SIGNALS" in self.driver.title








   