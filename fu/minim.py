from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.example.com Wait for the update button to become visible
wait = WebDriverWait(driver, 10)
update_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nkbihfbeogaeaoehlefnkodbefgpgknn"]//*[@id="maskedImage"]')))

# Click the update button
update_btn.click()
