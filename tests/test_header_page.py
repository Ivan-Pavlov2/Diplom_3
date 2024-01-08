import allure
from locators.orders_page_locators import OrdersPageLocators
from pages.header_page import HeaderPage
from data.data import *


class TestHeaderPage:
    @allure.title('Проверка на переход в Ленту заказов')
    def test_redirection_to_order_list(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()
        current_url = header_page.get_current_url()
        assert current_url == Links.feed

    @allure.title('Проверка на переход в "Конструктор"')
    def test_go_to_constructor(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()
        header_page.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)
        header_page.click_constructor_button()
        current_url = header_page.get_current_url()
        assert current_url == Links.main_page