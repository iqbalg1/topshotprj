from lib.pages.BasePage import BasePage
from lib.locators.MarketplacePageLocators import MarketplacePageLocators
from selenium.webdriver.common.by import By


class MarketplacePage(BasePage):
    def __init__(self, driver):
        self.url = 'https://nbatopshot.com/marketplace'
        super().__init__(driver)

    def select_search_bar(self):
        self.click(MarketplacePageLocators.SEARCH_BAR)

    def type_search_bar(self,input):
        self.enter_text(MarketplacePageLocators.SEARCH_BAR_INPUT,input)

    def select_player_card(self, player_name):
        player_locator = (By.XPATH, MarketplacePageLocators.PLAYER_CARD_XPATH.format(player_name))
        self.is_element_visibile(player_locator)
        self.click(player_locator)

    def get_search_dropdown_results(self):
        #if able to get results, would need to parse into an array
        #since getting only No Options, just returning element as-is
        return self.get_element(MarketplacePageLocators.PLAYER_DROPDOWN)
    