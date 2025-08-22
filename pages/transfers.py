import allure

from base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from dashboard import DASHBOARD_PAGE

class TRANSFERS_PAGE(BasePage):

    PAGE_URL = Links.TRANSFERS_PAGE
    
    @allure.step("Click on buttom_transfer")
    def click_buttom_transfer(self):
        dashboard = DASHBOARD_PAGE(self.driver)
        dashboard.click_transfers()

    account_select = ('xpath', '//select[@data-testid="from-account-select"]')
    account_source = ('xpath', '(//select[@data-testid="from-account-select"])//option[2]')
    
    account_select_2 = ('xpath', '//select[@data-testid="to-account-select"]')
    account_source_2 = ('xpath', '(//select[@data-testid="to-account-select"])//option[2]')

    amount = ('xpath', '//input[@data-testid="amount-input"]') #Вписать сумму

    button = ('xpath', '//button[@class="sc-gahYZc cCfCQV"]')

    @allure.step("Click on 'select source account'")
    def select_source_account(self):
        self.wait.until(EC.element_to_be_clickable(self.account_select)).click()
    
    @allure.step("Click on from account")
    def сlick_from_account(self):
        self.wait.until(EC.element_to_be_clickable(self.account_source)).click()
    
    @allure.step("Click on 'select destination account'")
    def select_destination_account(self):
        self.wait.until(EC.element_to_be_clickable(self.account_select_2)).click()
    
    @allure.step("Click on 'to my account'")
    def сlick_my_account(self):
        self.wait.until(EC.element_to_be_clickable(self.account_source_2)).click()
    
    def amount_fild(self, total):
        with allure.step(f"Change amount fild on {total}"):
            first_amount_fild = self.wait.until(EC.element_to_be_clickable(self.amount))
            first_amount_fild.clear()
            first_amount_fild.send_keys(total)
            self.total = total

    @allure.step("Change saved")
    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.amount,self.total))

    @allure.step("Click transfer money")
    def button_transfer_money (self):
        self.wait.until(EC.element_to_be_clickable(self.button)).click()
    
    



