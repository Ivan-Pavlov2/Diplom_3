import allure
from data.data import Links
from locators.personal_account_locators import PersonalAccountLocators
from locators.header_page_locators import HeaderPageLocators
from pages.personal_account_page import PersonalAccountPage
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.header_page import HeaderPage


class TestPersonalAccount:
    @allure.title('Проверка на открытие страницы "Личный кабинет" по клику на кнопку Личный кабинет')
    def test_go_to_account_from_header(self, driver, login):
        page = PersonalAccountPage(driver)
        page.find_constructor()
        page.click_account_button()
        current_url = page.get_current_url()
        assert current_url == Links.profile_page

    @allure.title('Проверка на переход в раздел История заказов')
    def test_go_to_order_history(self, driver, login):
        page = PersonalAccountPage(driver)
        page.find_constructor()
        page.click_account_button()
        page.click_order_list_link()
        current_url = page.get_current_url()
        assert current_url == Links.orders_history

    @allure.title('Проверка на выход из аккаунта')
    def test_logout(self, driver, login):

        main_page = MainPage(driver)
        main_page.find_the_crater_bun()
        header_page = HeaderPage(driver)
        header_page.click_on_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_profile()
        personal_account_page.click_logout_button()
        personal_account_page.wait_enter()
        text = personal_account_page.get_text_enter()
        assert text == 'Войти'