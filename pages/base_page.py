import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть ссылку')
    def open_link(self, url):
        return self.driver.get(url)

    @allure.step('Кликнуть на элемент когда он кликабелен')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Кликнуть на элемент, когда он видимый')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator)).click()

    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Найти элемент на странице')
    def find_my_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверить присутствие элемента на странице')
    def check_presense(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Дождаться видимости элемента')
    def wait_until_element_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Дождаться невидимости элемента')
    def wait_until_element_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться открытия новой вкладки')
    def wait_for_new_tab(self, index):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(index))

    @allure.step('Дождаться открытия страницы {url}')
    def wait_for_load_page(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def drag_and_drop_element(self, locator_from, locator_to):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator_from))
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator_to))
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()