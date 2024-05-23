from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


# frontend = 'https://www.linkedin.com/jobs/search/?currentJobId=3469886374&f_AL=true&f_E=1%2C2&f_JT=F%2CI&f_PP=102201911%2C102571732%2C104361728%2C103913444%2C106081027%2C102340689&geoId=90000070&keywords=junior%20software%20engineer&location=New%20York%20City%20Metropolitan%20Area&refresh=true&sortBy=R'

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3359186467&f_AL=true&f_E=4&f_JT=F%2CP%2CI&f_PP=102571732%2C104361728%2C103913444%2C102340689&geoId=90000070&keywords=junior%20software%20engineer%20NOT%20Server&sortBy=R'


PHONE_NUMBER = '123456789'
EMAIL = 'email@gmail.com'
PASSWORD = ''



chrome_driver_path = '/Users/peter/Desktop/HTML/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
driver.implicitly_wait(10)



sign_in_link_element = driver.find_element(By.CSS_SELECTOR, value='a[class="nav__button-secondary btn-md btn-secondary-emphasis"]')
sign_in_link_element.click()

username_element = driver.find_element(By.ID, value='username')
username_element.send_keys(EMAIL)

password_element = driver.find_element(By.ID, value='password')
password_element.send_keys(PASSWORD)

sign_in_button_element = driver.find_element(By.CSS_SELECTOR, value='button[class="btn__primary--large from__button--floating"]')
sign_in_button_element.click()



# tests = driver.find_elements(By.CSS_SELECTOR, value='div[class="mr1 artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view"]')
# for test in tests:
#     test.click()
#     easy_apply_element = driver.find_element(By.CSS_SELECTOR, value='button[class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')
#     easy_apply_element.click()

# jobs_elements = driver.find_elements(By.CSS_SELECTOR, value='div[class="mr1 artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view"]')
# for element in jobs_elements:
#     print('list: ',element)

# jobs_elements = driver.find_element(By.CSS_SELECTOR,
#                                      value='div[class="mr1 artdeco-entity-lockup__image artdeco-entity-lockup__image--type-square ember-view"]')
# print(jobs_elements)1
    # driver.implicitly_wait(5)
    # try:
    #
    #     element.click()
    #
    #     easy_apply_element = driver.find_element(By.CSS_SELECTOR, value='button[class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')
    #     easy_apply_element.click()
    #
    #     phone_number_input = driver.find_element(By.CSS_SELECTOR, value='input[class=" artdeco-text-input--input"]')
    #     phone_number_input.send_keys(PHONE_NUMBER)
    #
    #     resume_choose_button_element = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Choose Resume"]')
    #     resume_choose_button_element.click()
    #
    # except:
    #     NoSuchElementException
    #     pass
    #
    # else:
    #
    #     submit_application_element = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Submit application"]')
    #     submit_application_element.click()
    #
    # finally:
    #     dismiss_button_element = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Dismiss"]')
    #     dismiss_button_element.click()
    #
    #     try:
    #         discard_button_element = driver.find_element(By.CSS_SELECTOR, value='button[data-control-name="discard_application_confirm_btn"]')
    #         discard_button_element.click()
    #     except:
    #         NoSuchElementException
    #         pass
    #     finally:
    #         time.sleep(3)





time.sleep(10000)