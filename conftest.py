import pytest
from selenium import webdriver
from locators.personal_account_locators import PersonalAccountLocators
from locators.header_page_locators import HeaderPageLocators
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
import requests
from data.data import Links
import random
import string

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
   if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture
def create_and_delete_user():
    def random_generator(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    name = random_generator(10)
    email = random_generator(10)+'@yandex.ru'
    password = random_generator(10)

    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    login_data = payload.copy()
    login_data.pop("name")
    response = requests.post(Links.register_user, data=payload)
    access_token = response.json()["accessToken"]
    yield login_data, access_token
    requests.delete(Links.delete_user, headers={'Authorization': access_token})


@pytest.fixture
def login(driver, create_and_delete_user):
    main_page = MainPage(driver)
    main_page.click_on_enter_account()
    main_page.click_to_element(HeaderPageLocators.PERSONAL_ACCOUNT)
    personal_account_page = PersonalAccountPage(driver)
    personal_account_page.set_text_to_element(PersonalAccountLocators.INPUT_EMAIL, create_and_delete_user[0]['email'])
    personal_account_page.set_text_to_element(PersonalAccountLocators.INPUT_PASSWORD, create_and_delete_user[0]['password'])
    personal_account_page.click_on_element(PersonalAccountLocators.ENTER_BUTTON)