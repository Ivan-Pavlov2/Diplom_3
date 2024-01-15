import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка на появление всплывающего окна при клике на ингредиент')
    def test_popup_of_ingredient(self, driver):
        page = MainPage(driver)
        page.click_on_crator_bun()
        assert page.get_ingredient_details() == "Детали ингредиента"

    @allure.title('Проверка на закрытие всплывающего окна кликом по крестику')
    def test_close_ingredient_details_window(self, driver):
        page = MainPage(driver)
        page.click_on_crator_bun()
        page.click_cross_button()
        page.invisibility_ingredient_details()
        assert page.check_displayed_ingredient_details() == False

    @allure.title('Проверка на изменение счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        start_quantity = main_page.check_quantity_of_ingredients()
        main_page.add_filling_to_order()
        end_quantity = main_page.check_quantity_of_ingredients()
        assert end_quantity == '1' and start_quantity == '0'

    @allure.title('Проверка на успешное создание заказа')
    def test_successful_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.find_the_crater_bun()
        main_page.add_bun_to_order()
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.find_the_order_number()
        assert main_page.check_displayed_order_status_text() == True
