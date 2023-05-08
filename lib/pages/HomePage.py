from lib.pages.BasePage import BasePage
from lib.locators.HomePageLocators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver):
        self.url = 'https://www.nbatopshot.com'
        super().__init__(driver)

    def verify_navigation_links_visible(self):
        for link in HomePageLocators.NAVIGATION_DICT:
            if not self.is_element_visibile(HomePageLocators.NAVIGATION_DICT[link]):
                return False
        
        return True
    
    def get_content_titles(self):
        content_title_web_elements = self.get_all_elements(HomePageLocators.CONTENT_TITLE)
        return list(map(lambda x: x.text,content_title_web_elements))
    
    def get_content_texts(self):
        content_text_web_elements = self.get_all_elements(HomePageLocators.CONTENT_TITLE)
        return list(map(lambda x: x.text,content_text_web_elements))
    
    def get_content_buttons(self):
        content_action_buttons = self.get_all_elements(HomePageLocators.CONTENT_BUTTON)
        return list(map(lambda x: x.text,content_action_buttons))
    
    def goto_page(self, page):
        if page in HomePageLocators.NAVIGATION_DICT:
            self.click(HomePageLocators.NAVIGATION_DICT[page])
        else:
            print("Invalid navigation page requested")
            raise