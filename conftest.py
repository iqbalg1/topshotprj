import pytest
from selenium import webdriver
from lib.pages.HomePage import HomePage
from lib.pages.MarketplacePage import MarketplacePage

@pytest.fixture()
def create_homepageobj():
    driver = webdriver.Firefox()
    home_page = HomePage(driver)

    yield home_page

    driver.quit()

@pytest.fixture()
def create_marketplacepageobj():
    driver = webdriver.Firefox()
    marketplace_page = MarketplacePage(driver)

    yield marketplace_page

    driver.quit()