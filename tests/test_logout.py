from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPage, LoginWindow
from data import ACCOUNT_DATA, URL, TEXTS


class TestLogout:
    def test_logout_account(self, driver):
        driver.get(URL["url_page"])
        driver.find_element(*StartPage.ENTRY_AND_LOGIN_BUTTON).click()
        email = ACCOUNT_DATA["email"]
        password = ACCOUNT_DATA["password"]

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginWindow.NO_ACCOUNT_BUTTON))

        driver.find_element(*LoginWindow.EMAIL).send_keys(email)
        driver.find_element(*LoginWindow.PASSWORD).send_keys(password)
        driver.find_element(*LoginWindow.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StartPage.EXIT_BUTTON))

        driver.find_element(*StartPage.EXIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StartPage.ENTRY_AND_LOGIN_BUTTON))

        text = driver.find_element(*StartPage.ENTRY_AND_LOGIN_BUTTON).text
        assert text == TEXTS["entry_and_login"]
