from selenium.webdriver.common.by import By

class HomePageLocators():
    #Navigation Elements
    NAVIGATION_DICT = {
        'Home': (By.CLASS_NAME, 'sc-e51d44c4-0'),
        'Drops': (By.LINK_TEXT, 'DROPS'),
        'Marketplace': (By.LINK_TEXT, 'MARKETPLACE'),
        'Challenges': (By.LINK_TEXT, 'CHALLENGES'),
        'Community': (By.LINK_TEXT, 'COMMUNITY'),
        'Blog': (By.LINK_TEXT, 'BLOG'),
        'Log In': (By.LINK_TEXT, 'LOG IN'),
        'Sign Up': (By.LINK_TEXT, 'SIGN UP')
    }
    #Home Page elements
    CONTENT_TITLE = (By.CLASS_NAME, 'chakra-heading')
    CONTENT_TEXT = (By.CLASS_NAME, 'chakra-text')
    CONTENT_BUTTON = (By.CLASS_NAME, 'chakra-button')