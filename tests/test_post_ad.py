from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPage, LoginWindow, PostAd, ProfileWindow
from data import ACCOUNT_DATA, URL, TEXTS, AD_DATA


class TestPostAd:
    def test_post_ad_no_account(self, driver):
        driver.get(URL["url_page"])
        driver.find_element(*StartPage.POST_AD_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PostAd.NOTE_NEED_ACCOUNT))

        text = driver.find_element(*PostAd.NOTE_NEED_ACCOUNT).text
        assert text == TEXTS["need_account"]

    def test_post_ad_with_account(self, driver):
        driver.get(URL["url_page"])
        driver.find_element(*StartPage.ENTRY_AND_LOGIN_BUTTON).click()
        email = ACCOUNT_DATA["email"]
        password = ACCOUNT_DATA["password"]

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginWindow.NO_ACCOUNT_BUTTON))

        driver.find_element(*LoginWindow.EMAIL).send_keys(email)
        driver.find_element(*LoginWindow.PASSWORD).send_keys(password)
        driver.find_element(*LoginWindow.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element(LoginWindow.ENTER_BUTTON))

        driver.find_element(*StartPage.POST_AD_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PostAd.NAME))

        driver.find_element(*PostAd.NAME).send_keys(AD_DATA["name"])
        driver.find_element(*PostAd.DESCRIPTION).send_keys(AD_DATA["description"])
        driver.find_element(*PostAd.PRICE).send_keys(AD_DATA["price"])
        driver.find_element(*PostAd.DROPDOWN_CATEGORIES).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PostAd.TECHNOLOGY_CATEGORY_BUTTON))
        driver.find_element(*PostAd.TECHNOLOGY_CATEGORY_BUTTON).click()
        driver.find_element(*PostAd.DROPDOWN_CITIES).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PostAd.SAINT_PETERSBURG_BUTTON))
        driver.find_element(*PostAd.SAINT_PETERSBURG_BUTTON).click()
        driver.find_element(*PostAd.RADIOREGULAR_BUTTON).click()
        driver.find_element(*PostAd.PUBLIC_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element(PostAd.PUBLIC_BUTTON))

        driver.find_element(*StartPage.AVATAR_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ProfileWindow.SAVE_CHANGES_BUTTON))

        assert AD_DATA["name"] == driver.find_element(*ProfileWindow.CREATED_AD_NAME).text


