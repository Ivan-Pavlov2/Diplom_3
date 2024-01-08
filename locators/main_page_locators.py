from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDERS_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'  # заголовок "Лента заказов"

    ENTER_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]'
    CREATE_BURGER = By.XPATH, '//h1[text()="Соберите бургер"]'  # надпись Соберите бургер
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка Оформить заказ

    SAUCES = By.XPATH, '//span[text()="Соусы"]/parent::div'  # Соусы
    FILLINGS = By.XPATH, '//span[text()="Начинки"]/parent::div'  # Начинки
    BUNS = By.XPATH, '//span[text()="Булки"]/parent::div'  # Булки

    BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'  # краторная булка
    # BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    FILLING_FILE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]'  #Филе Люминесцентного тетраодонтимформа
    SAUCE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]'  #ингредиент Соус фирменный Space Sauce
    INGREDIENT_COUNTER = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]//p[contains(@class, "counter__num")]' #счетчик ингредиента
    INGREDIENT_DETAILS_POPUP = By.XPATH, '//h2[text()="Детали ингредиента"]'  # Детали ингредиента
    INGREDIENT_POPUP = By.XPATH, '//*[contains(@class, "contentBox")]'  # всплывающее окно Детали ингредиента
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"basket")]'  # Корзина
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'  # номер заказа во всплывающем окне
    DEFAULT_ORDER = By.XPATH, '//h2[text()="9999"]'  # дефолтный номер заказа в попапе
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'  # Ваш заказ начали готовить в попапе
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'  # Крестик закрытия всплывающего окна
    DEFAULT_ORDER_NUMBER = By.XPATH, '//h2[text()="9999"]'