from selenium.webdriver.common.by import By

class MarketplacePageLocators():
    SEARCH_BAR = (By.ID, 'search-tags')
    SEARCH_BAR_INPUT = (By.ID, 'react-select-search-tags-input')
    
    PLAYER_DROPDOWN = (By.CLASS_NAME, 'css-1tqgitt-menu')

    PLAYER_CARD_XPATH = '//span[text()="{}"]'