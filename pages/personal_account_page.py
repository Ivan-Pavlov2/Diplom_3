import allure
from locators.personal_account_locators import PersonalAccountLocators
from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_on_element(PersonalAccountLocators.RESET_PASSWORD_LINK)

    @allure.step('Переход в личный кабинет')
    def click_account_button(self):
        self.click_on_element(HeaderPageLocators.PERSONAL_ACCOUNT)
        self.wait_until_element_visibility(PersonalAccountLocators.PROFILE)


    @allure.step('Нажатие на кнопку "Выход"')
    def click_logout_button(self):
        self.click_on_element(PersonalAccountLocators.EXIT)

    @allure.step('Переход в раздел "История заказов"')
    def click_order_list_link(self):
        self.click_on_element(PersonalAccountLocators.ORDERS_HISTORY)

    @allure.step('Получаем номер заказа в Истории заказов')
    def get_order_number(self):
        return self.get_text_of_element(PersonalAccountLocators.ORDER_NUMBER)