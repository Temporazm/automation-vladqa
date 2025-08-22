import allure

from base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class DASHBOARD_PAGE(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE 

    BUTTON_TRANSFERS = ('xpath', '//div/button[3]')

    @allure.step("Go to click_transfers ")
    def click_transfers(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_TRANSFERS)).click()
         