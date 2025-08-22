import pytest

from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard import DASHBOARD_PAGE
from pages.transfers import TRANSFERS_PAGE

class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard: DASHBOARD_PAGE
    transfers: TRANSFERS_PAGE

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
    
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard = DASHBOARD_PAGE(driver)
        request.cls.transfers = TRANSFERS_PAGE(driver)

