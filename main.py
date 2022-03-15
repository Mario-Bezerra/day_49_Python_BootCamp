from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_drive_path = "C:\\Users\\Pichau\\Desktop\\JAVASCRIPT\\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.maximize_window()
driver.get("https://www.linkedin.com/feed/")

sign_in = driver.find_element(By.CLASS_NAME, "main__sign-in-link")
sign_in.click()
time.sleep(1)

email = driver.find_element(By.NAME, "session_key")
email.send_keys("@gmail.com")
password = driver.find_element(By.NAME, "session_password")
password.send_keys("")

login_in_button = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container")
login_in_button.click()
time.sleep(3)

jobs = driver.find_element(By.ID, "ember20")
jobs.click()
time.sleep(1)
search = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__keywords-label + input")

search.send_keys("python brasil")
search.send_keys(Keys.TAB)
search.send_keys("Brasil")
search.send_keys(Keys.ENTER)
time.sleep(2)

search_submit_button = driver.find_element(By.CLASS_NAME, "jobs-search-box__submit-button")
search_submit_button.click()
time.sleep(3)

list_of_jobs_objects = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
for i in range(len(list_of_jobs_objects)):
    try:
        each_job = driver.find_element(By.CLASS_NAME, f"jobs-search-two-pane__job-card-container--viewport-tracking-{i}")
    except NoSuchElementException:
        print("No company found")
        continue
    else:
        each_job.click()
        time.sleep(2)
        save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply + .jobs-save-button")
        save_button.click()

time.sleep(3)
driver.quit()
