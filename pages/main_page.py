import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Переходим на страницу логина кликом по кнопке "Войти в аккаунт"')
    def click_on_enter_account(self):
        self.move_to_element_and_click(MainPageLocators.ENTER_ACCOUNT)

    @allure.step('Клик на ингредиент "Краторная булка"')
    def click_on_crator_bun(self):
        self.move_to_element_and_click(MainPageLocators.BUN)

    @allure.step('Закрываем попап крестиком')
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Добавить краторную булку в заказ')
    def add_bun_to_order(self):
        self.drag_and_drop_element(MainPageLocators.BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавить "Говяжий метеорит (отбивная)" в заказ')
    def add_filling_to_order(self):
        self.drag_and_drop_element(MainPageLocators.FILLING_FILE, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавить "Соус Spicy-X" в заказ')
    def add_sauce_to_order(self):
        self.drag_and_drop_element(MainPageLocators.SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Получить количество добавленного в заказ ингредиента')
    def check_quantity_of_ingredients(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Найти краторную булку')
    def find_the_crater_bun(self):
        self.find_my_element(MainPageLocators.BUN)

    @allure.step('Найти номер заказа во всплывающем окне')
    def find_the_order_number(self):
        self.find_my_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Получить детали ингредиентов')
    def get_ingredient_details(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Проверить скрытость деталей ингредиентов')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Проверить наличие деталей ингредиентов на экране')
    def check_displayed_ingredient_details(self) -> bool:
        return self.check_presense(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Проверить наличие, что заказа начали готовить')
    def check_displayed_order_status_text(self) -> bool:
        return self.check_presense(MainPageLocators.ORDER_STATUS_TEXT).is_displayed()

    @allure.step('Дождаться кнопки создать бургер')
    def wait_create_burger(self):
        return self.wait_until_element_visibility(MainPageLocators.CREATE_BURGER)

    @allure.step('Создаем заказ и получаем его номер')
    def create_order(self):
        self.wait_until_element_visibility(MainPageLocators.BUN)
        self.drag_and_drop_element(MainPageLocators.BUN, MainPageLocators.ORDER_BASKET)
        self.drag_and_drop_element(MainPageLocators.FILLING_FILE, MainPageLocators.ORDER_BASKET)
        self.find_my_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_until_element_visibility(MainPageLocators.ORDER_STATUS_TEXT)
        self.wait_until_element_invisibility(MainPageLocators.DEFAULT_ORDER_NUMBER)
        order = self.get_text_of_element(MainPageLocators.ORDER_NUMBER)
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)
        return order
