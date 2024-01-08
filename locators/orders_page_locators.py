from selenium.webdriver.common.by import By


class OrdersPageLocators:
    ORDERS_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'  # Состав
    ORDER_NUMBER = By.XPATH, '//p[text()="{}"]'  # номер заказа в ленте
    ALL_READY = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'  # надпись "Все текущие заказы готовы!"
    IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'  # номер заказа в работе
    ALL_ORDERS = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'# заказы за всё время
    TODAY_ORDERS = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'



    COMPLETED_ORDERS_TOTAL = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'
    # количество заказов, выполненных за все время