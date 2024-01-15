import allure
from locators.header_page_locators import HeaderPageLocators
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list_button(self):
        self.move_to_element_and_click(HeaderPageLocators.ORDERS_LIST)
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(HeaderPageLocators.CONSTRUCTOR)

    @allure.step('Переход в Личный кабинет')
    def click_on_account(self):
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Ожидание ленты заказов')
    def wait_orders_list_title(self):
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)