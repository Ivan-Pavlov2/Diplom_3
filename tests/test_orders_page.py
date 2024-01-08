import allure
from locators.orders_page_locators import OrdersPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
from pages.orders_page import OrdersPage
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderListPage:
    @allure.title('Проверка на открытие всплывающего окна с деталями')
    def test_get_order_popup(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()
        page = OrdersPage(driver)
        page.click_order()

        assert page.check_presense(OrdersPageLocators.ORDER_STRUCTURE).is_displayed() == True

    @allure.title('Проверка на отображение созданного заказа в Ленте заказов')
    def test_find_order_in_list(self, driver, login):
        main_page = MainPage(driver)
        main_page.create_order()
        profile_page = PersonalAccountPage(driver)
        profile_page.click_account_button()
        profile_page.click_order_list_link()
        profile_page.find_my_element(PersonalAccountLocators.ORDER_STATUS)
        order = profile_page.get_order_number()
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()
        orders_page = OrdersPage(driver)
        orders_page.find_my_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        order2 = orders_page.get_order_in_orderlist(order)
        assert order2.is_displayed()

    @allure.title('Проверка на увеличение счетчика заказов за сегодня после создания заказа')
    def test_today_orders_counter(self, driver, login):
        main_page = MainPage(driver)
        main_page.find_my_element(MainPageLocators.BUN)
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()
        order_page = OrdersPage(driver)
        order_page.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)
        today_number = order_page.get_today_orders_number()
        header_page.click_constructor_button()
        main_page.wait_until_element_visibility(MainPageLocators.CREATE_BURGER)
        main_page.create_order()
        header_page.click_orders_list_button()
        order_page.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)
        new_today_number = order_page.get_today_orders_number()
        assert int(new_today_number) == int(today_number) + 1

    @allure.title('Проверка на наличие созданного заказа среди заказов в работе')
    def test_new_order_appears_in_work_list(self, driver, login):
        mainpage = MainPage(driver)
        new_order = mainpage.create_order()
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()
        orders_page = OrdersPage(driver)
        orders_page.wait_until_element_invisibility(OrdersPageLocators.ALL_READY)
        order_in_work = orders_page.get_order_number_in_work()
        assert new_order in order_in_work

    @allure.title('Проверка на изменение счетчика "Выполнено за все время" после создания заказа')
    def test_change_total_orders_number(self, driver, login):

        main_page = MainPage(driver)
        main_page.find_my_element(MainPageLocators.BUN)
        header_page = HeaderPage(driver)
        header_page.click_orders_list_button()
        feed_page = OrdersPage(driver)
        feed_page.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)
        total_number = feed_page.get_total_orders_number()
        header_page.click_constructor_button()
        main_page.wait_until_element_visibility(MainPageLocators.CREATE_BURGER)
        main_page.create_order()
        header_page.click_orders_list_button()
        feed_page.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)
        new_total_number = feed_page.get_total_orders_number()
        assert int(new_total_number) == int(total_number) + 1