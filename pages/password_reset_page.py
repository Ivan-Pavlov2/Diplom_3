import allure
from locators.password_reset_locators import PasswordResetLocators
from pages.base_page import BasePage


class PasswordResetPage(BasePage):

    @allure.step('Вводим емейл в поле для восстановления пароля')
    def set_email_for_reset_password(self, email):
        self.set_text_to_element(PasswordResetLocators.INPUT_EMAIL, email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_button(self):
        self.move_to_element_and_click(PasswordResetLocators.RESET_BUTTON)

    @allure.step('Кликаем на кнопку Показать/скрыть пароль')
    def click_on_show_password_button(self):
        self.click_on_element(PasswordResetLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Найти кнопку сохарнения')
    def find_save_button(self):
        self.find_my_element(PasswordResetLocators.SAVE_BUTTON)

    @allure.step('Найти активное поле пароля')
    def find_input_active(self):
        return self.find_my_element(PasswordResetLocators.INPUT_ACTIVE)
