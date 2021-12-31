from selenium import webdriver
import page
import unittest


class TestBase(unittest.TestCase):


    def setUp(self):
        self.driver =  webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_size(1920, 1080)


    def tearDown(self):
        self.driver.close()


class SeleniumTest(TestBase):
        
    def test_home_page(self):
        self.driver.get('http://127.0.0.1:8000')
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_about_link_works()
        assert home_page.is_home_link_works()
        assert home_page.is_register_form_works()

    def test_signals_page(self):
        self.driver.get("http://mj%40gmail.com:password123@127.0.0.1:8000/signals")
        signals_page = page.SignalsPage(self.driver)
        assert signals_page.is_signals_title_matches()

    def test_about_page(self):
        self.driver.get('http://127.0.0.1:8000/about')
        about_page = page.AboutPage(self.driver)
        assert about_page.is_title_matches()
        assert about_page.is_about_heading_displayed()

        
if __name__ == '__main__':
    unittest.main()




        