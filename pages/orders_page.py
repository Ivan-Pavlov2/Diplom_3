import allure
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage


class OrdersPage(BasePage):
    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        self.click_on_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Ищем заказ по номеру в Ленте заказов')
    def get_order_in_orderlist(self, order):
        method, locator = OrdersPageLocators.ORDER_NUMBER
        locator = locator.format(order)
        return self.find_my_element((method, locator))

    @allure.step('Получаем общее количество заказов, выполненных за все время')
    def get_total_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.COMPLETED_ORDERS_TOTAL)

    @allure.step('Получаем общее количество заказов, выполненных за сегодня')
    def get_today_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.TODAY_ORDERS)

    @allure.step('Ищем заказ по номеру в разделе "В работе"')
    def get_order_number_in_work(self):
        return self.get_text_of_element(OrdersPageLocators.IN_WORK)

    @allure.step('Проверка отображения состава')
    def check_order_structure(self):
        return self.check_presense(OrdersPageLocators.ORDER_STRUCTURE).is_displayed()

    @allure.step('Найти ленту заказа')
    def find_orders_list_title(self):
        return self.find_my_element(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Ожидание ленты заказов')
    def wait_orders_list_title(self):
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Дождатся когда все заказы будут готовы')
    def wait_all_ready(self):
        return self.wait_until_element_invisibility(OrdersPageLocators.ALL_READY)
