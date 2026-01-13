from selenium.webdriver.common.by import By


class StartPage:
    ENTRY_AND_LOGIN_BUTTON = (By.XPATH, ".//button[text()= 'Вход и регистрация']")
    USER_NAME = (By.CLASS_NAME, "profileText")
    AVATAR_BUTTON = (By.XPATH, ".//div[@class='flexRow']/button/*")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    POST_AD_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")


class LoginWindow:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text() = 'Нет аккаунта']")
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")


class RegistrationWindow:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT_PASSWORD = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text() = 'Создать аккаунт']")
    RED_ERROR = (By.XPATH, ".//span[text()='Ошибка']")
    RED_EMAIL_BORDER = (By.XPATH, ".//input[@name='email']/..")
    RED_PASSWORD_BORDER = (By.XPATH, ".//input[@name='password']/..")
    RED_SUBMIT_PASSWORD_BORDER = (By.XPATH, ".//input[@name='submitPassword']/..")

class PostAd:
    NOTE_NEED_ACCOUNT = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    NAME = (By.XPATH, ".//input[@placeholder='Название']")
    DESCRIPTION = (By.XPATH, ".//textarea[@placeholder='Описание товара']")
    PRICE = (By.XPATH, ".//input[@placeholder='Стоимость']")
    DROPDOWN_CATEGORIES = (By.XPATH, ".//input[@name='category']/../button")
    RADIOREGULAR_BUTTON = (By.CSS_SELECTOR, ".radioUnput_inputRegular__FbVbr")
    DROPDOWN_CITIES = (By.XPATH, ".//input[@name='city']/../button")
    PUBLIC_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
    TECHNOLOGY_CATEGORY_BUTTON = (By.XPATH, ".//button//span[text()='Технологии']")
    SAINT_PETERSBURG_BUTTON = (By.XPATH, ".//button//span[text()='Санкт-Петербург']")


class ProfileWindow:
    SAVE_CHANGES_BUTTON = (By.XPATH, ".//button[text()='Сохранить изменения']")
    CREATED_AD_NAME = (By.XPATH, ".//div[@class='card']/div[@class='description']/div[@class='about']/h2[text()='Фантом']")
