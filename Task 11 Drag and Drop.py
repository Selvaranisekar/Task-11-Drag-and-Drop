import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver


class draganddrop:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)
        iframe_element=self.driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
        self.driver.switch_to.frame(iframe_element)
        draggable_element = self.driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")
        droppable_element = self.driver.find_element(By.XPATH,"//p[normalize-space()='Drop here']")
        action=ActionChains(self.driver)
        action.drag_and_drop(draggable_element,droppable_element).perform()
        print("Drag and Drop: success")

if __name__=="__main__":
    DD=draganddrop("https://jqueryui.com/droppable/")
    DD.start()
    time.sleep(5)











