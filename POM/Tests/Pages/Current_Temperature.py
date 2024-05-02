from selenium.webdriver.common.by import By


class CurrentTemperature:


    def __init__(self, driver):
        self.driver= driver
        self.i_button = (By.button, "")
        # Locator of this element how to do that ?
        self.Degre_temperature = (By.ID, "temperature")
        self.Buy_moisturizers_button = (By.button, "btn btn-primary")
        self.Buy_sunscreens_button = (By.button, "btn btn-primary")

     def open_page(self, url):
         self.driver.get(url)


      #def click_i(self):
      #  self.driver.find_element(self.i_button).click()

     def click_Buy_moisturizers(self):
         self.driver.find_element(self.Buy_moisturizers_button).click()

     def click_Buy_sunscreens(self):
         self.driver.find_element(self.Buy_sunscreens_button).click()




