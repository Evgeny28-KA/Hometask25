from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://petfriends1.herokuapp.com/all_pets")
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.CLASS_NAME, "card-deck"))