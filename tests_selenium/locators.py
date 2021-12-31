from selenium.webdriver.common.by import By

class HomePageLocators(object):

    ABOUT_LINK = (By.CLASS_NAME, 'about-link')
    HOME_LINK = (By.CLASS_NAME, 'home-link')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT = (By.CLASS_NAME, 'button')
    REG_HEADING = (By.CLASS_NAME, 'reg-heading')
    SIGNALS_LINK = (By.CLASS_NAME, 'signals-link')

class AboutPageLocators(object):

    ABOUT_HEADING = (By.CLASS_NAME, 'about-heading')





