from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'  # Войти
    RESET_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'  # Восстановить пароль
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # поле ввода пароля
    PROFILE = By.XPATH, '//*[@href="/account/profile"]'  # Профиль
    ORDERS_HISTORY = By.XPATH, '//*[@href="/account/order-history"]'  # История заказов в ЛК
    EXIT = By.XPATH, '//*[contains(@class, "Account_button")]'  # кнопка Выход
    ORDER_STATUS = By.XPATH, '//p[text()="Выполнен"]'  # статус заказа
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'  # номер заказа в истории