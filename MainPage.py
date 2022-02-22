from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, _driver):
        self.driver = _driver
        self.actions = ActionChains(self.driver)

    def getheadertext(self):
        return self.driver.find_element(By.XPATH, "//div[@class='b-slider-main__title']").text

    def findtext(self, text):
        search = self.driver.find_element(By.XPATH, "//input[@id='title-search-input-main']")
        self.actions.send_keys_to_element(search, text).send_keys_to_element(search, Keys.ENTER).perform()
        catalog = "//div[@class='catalog__products']/div[@class='b-product']"
        catalogNames = []
        for i in range(1, len(self.driver.find_elements(By.XPATH, catalog)) + 1):
            catalogNames.append(self.driver.find_element(By.XPATH, f"{catalog}[{i}]//div[@class='b-product__title']/a").text)
        return self.driver.find_element(By.XPATH, "//div[@class='search']/h1").text, \
               self.driver.find_element(By.XPATH, "//input[@id='title-search-input-main']").get_attribute("value"), catalogNames

    def catalogtext(self, catalogname, type, name):
        if catalogname == '':
            self.driver.find_element(By.XPATH,
                                     "//a[@class='b-section__link--arrow link link--blue link--bold']").click()
            self.driver.find_element(By.XPATH, f"//ul/li/a[contains(text(), '{name}')]").click()
            self.driver.find_element(By.XPATH,
                                     f"//div[@class='catalog__category']/a[contains(text(), '{type}')]").click()
        else:
            self.driver.find_element(By.XPATH,
                                     f"//div[contains(text(), '{catalogname}')]/following-sibling::a[@class='link "
                                     f"link--blue link--bold']").click()
            self.driver.find_element(By.XPATH, f"//ul/li/a[contains(text(), '{name}')]").click()
        catalog = "//div[@class='catalog__products']/div[@class='b-product']"
        catalogText = []
        for i in range(1, len(self.driver.find_elements(By.XPATH, catalog)) + 1):
            catalogText.append(self.driver.find_element(By.XPATH, f"{catalog}[{i}]//div[@class='b-product__title']/a").text)
        return catalogText


# os.environ['PATH'] += 'C:/Users/Public/Pasha/Selenium_drivers'
# driver = webdriver.Chrome()
# driver.get('http://www.agatmedfarm.ru/')
# driver.maximize_window()
# mainpage = MainPage(driver)
# print(mainpage.getheadertext())
# print(mainpage.findtext('простыня'))
# mainpage.returnmainpage()
# print(mainpage.catalogtext('', 'Премиум', 'Урология'))
# mainpage.returnmainpage()
# print(mainpage.catalogtext('Одноразовая', '', 'Шапочки'))
# driver.quit()
