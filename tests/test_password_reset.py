import allure
from data.data import Links
from locators.password_reset_locators import PasswordResetLocators
from pages.personal_account_page import PersonalAccountPage
from pages.password_reset_page import PasswordResetPage
from pages.header_page import HeaderPage


class TestPasswordReset:
    @allure.title('Проверка на переход по клику на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_on_account()
        page = PersonalAccountPage(driver)
        page.click_password_reset_link()
        current_url = page.get_current_url()
        assert current_url == Links.forgot_password_page

    @allure.title('Проверка на ввод почты и переход после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self, driver, create_and_delete_user):
        page = PasswordResetPage(driver)
        page.open_link(Links.forgot_password_page)
        page.set_email_for_reset_password(create_and_delete_user[0]['email'])
        page.click_reset_button()
        page.find_save_button()
        current_url = page.get_current_url()
        assert current_url == Links.reset_password_page

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_field_active(self, driver, create_and_delete_user):
        page = PasswordResetPage(driver)
        page.open_link(Links.forgot_password_page)
        page.set_email_for_reset_password(create_and_delete_user[0]['email'])
        page.click_reset_button()
        page.find_save_button()
        page.click_on_show_password_button()
        assert page.find_input_active()
