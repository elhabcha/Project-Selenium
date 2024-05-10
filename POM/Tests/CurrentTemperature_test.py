import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POM.Tests.Pages.Current_Temperature import CurrentTemperature

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def test_CurrentTemperature(driver):
    Current_Temperature = CurrentTemperature(driver)
    #Current_Temperature.open_page("https://weathershopper.pythonanywhere.com/")
    driver.get("https://weathershopper.pythonanywhere.com/")
    time.sleep(3)
    CurrentTemperature.click_Buy_sunscreens()
    time.sleep(3)


