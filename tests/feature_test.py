import random
import allure
import pytest
import time

from pages.base_test import BaseTest
from conftest import driver

@allure.feature("Profile functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()

        self.dashboard.is_opened() #Проверить
        self.dashboard.click_transfers()
        
        self.transfers.open()
        self.transfers.click_buttom_transfer()
        self.transfers.select_source_account()
        self.transfers.сlick_from_account()
        self.transfers.select_destination_account()
        self.transfers.сlick_my_account()
        self.transfers.amount_fild(f"{random.randint(1,100)}")
        self.transfers.is_changes_saved()
        self.transfers.button_transfer_money()
        driver.quit()
        


    
        
