from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPage, LoginWindow, RegistrationWindow
from data import ACCOUNT_DATA, URL, REGISTRATION_PASSWORD, USER_DATA, ERRORS


class TestRegistration:
    def create_account(self, driver, email, password=REGISTRATION_PASSWORD["password"]):
        driver.get(URL["url_page"]) 

        driver.find_element(*StartPage.ENTRY_AND_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginWindow.NO_ACCOUNT_BUTTON))

        driver.find_element(*LoginWindow.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationWindow.EMAIL))

        driver.find_element(*RegistrationWindow.EMAIL).send_keys(email)
        driver.find_element(*RegistrationWindow.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationWindow.SUBMIT_PASSWORD).send_keys(password)
        driver.find_element(*RegistrationWindow.CREATE_ACCOUNT_BUTTON).click()

    def test_registration_correct_email(self, driver, generate_email):

        email = generate_email
        self.create_account(driver, email=email)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StartPage.USER_NAME))

        avatar = driver.find_element(*StartPage.AVATAR_BUTTON).get_attribute("xmlns")
        user_name = driver.find_element(*StartPage.USER_NAME).text
        assert avatar == URL["url_photo"]
        assert user_name == USER_DATA["user_name"]

    def test_registration_uncorrect_email(self, driver, generate_bad_email):

        email = generate_bad_email
        self.create_account(driver, email=email)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationWindow.RED_ERROR))

        error = driver.find_element(*RegistrationWindow.RED_ERROR).text
        email_border = driver.find_element(*RegistrationWindow.RED_EMAIL_BORDER).value_of_css_property("border")
        password_border = driver.find_element(*RegistrationWindow.RED_PASSWORD_BORDER).value_of_css_property("border")
        submit_password_border = driver.find_element(*RegistrationWindow.RED_SUBMIT_PASSWORD_BORDER).value_of_css_property("border")
        assert error == ERRORS["error"]
        assert email_border == ERRORS["error_color"]
        assert password_border == ERRORS["error_color"]
        assert submit_password_border == ERRORS["error_color"]

    def test_registration_with_existing_account(self, driver):

        email = ACCOUNT_DATA["email"]
        password = ACCOUNT_DATA["password"]
        self.create_account(driver, email=email, password=password)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationWindow.RED_ERROR))

        error = driver.find_element(*RegistrationWindow.RED_ERROR).text
        email_border = driver.find_element(*RegistrationWindow.RED_EMAIL_BORDER).value_of_css_property("border")
        password_border = driver.find_element(*RegistrationWindow.RED_PASSWORD_BORDER).value_of_css_property("border")
        submit_password_border = driver.find_element(*RegistrationWindow.RED_SUBMIT_PASSWORD_BORDER).value_of_css_property("border")
        assert error == ERRORS["error"]
        assert email_border == ERRORS["error_color"]
        assert password_border == ERRORS["error_color"]
        assert submit_password_border == ERRORS["error_color"]


