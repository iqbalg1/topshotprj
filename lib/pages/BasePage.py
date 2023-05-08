from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)
        if self.url:
            self.driver.get(self.url)

    def click(self, locator):
        try:
            self.wait.until(
                EC.element_to_be_clickable((*locator,))
            )
            self.driver.find_element(*locator).click()
        except Exception as err:
            print("Element not found or clickable. Error: ", err)
            raise
    
    def click_js(self, locator):
        try:
            self.wait.until(
                EC.element_to_be_clickable((*locator,))
            )
            field = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", field)
        except Exception as err:
            print("Element not found or clickable. Error: ", err)
            raise

    def enter_text(self, locator, text):
        try:
            self.wait.until(
                EC.visibility_of_element_located((*locator,))
            )
        except Exception as err:
            print("Unable to find input field. Error: ", err)
            raise
        self.driver.find_element(*locator).send_keys(text)

    def get_element(self, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located((*locator,))
            )
        except Exception as err:
            print("Unable to find element. Error: ", err)
            raise
        return self.driver.find_element(*locator)

    def wait_until_not_visible(self, locator):
        try:
            self.wait.until(
                EC.invisibility_of_element_located((*locator,))
            )
        except Exception as err:
            print("Element still visbile. Error: ", err)
            raise
            
    def wait_until_visible(self, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located((*locator,))
            )
        except Exception as err:
            print("Element not found. Error: ", err)
            raise

    def is_element_visibile(self, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located((*locator,))
            )
            return True
        except Exception as err:
            print("Cound not find element. Error: ", err)
            return False

    def get_all_elements(self, locator):
        try:
            self.wait_until_visible(locator)
            elements = self.driver.find_elements(*locator)
            return elements
        except Exception as err:
            print("Could not find elements. Error: ", err)
            raise

    def get_current_url(self):
        return self.driver.current_url
