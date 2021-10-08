from pages.base_page import BasePage
from pages.locators import UserPageLocators
import allure


class UserPage(BasePage):
    @allure.step('Проверка формы авторизации')
    def check_login_form(self):
        self.logger.info('Проверка формы авторизации')
        self.waiting_for_element_present(*UserPageLocators.LOGIN)
        self.waiting_for_element_present(*UserPageLocators.PASS)
        self.waiting_for_element_present(*UserPageLocators.BUTTON_IN)
        self.waiting_for_element_present(*UserPageLocators.REGISTRATION_BUTTON)

    @allure.step('Заполнение формы данных нового пользователя')
    def fill_in_the_data_of_a_new_user(self, name, email, password):
        """
        :param name: ФИО пользователя
        :param email: Почта пользователя
        :param password: Пароль
        :return: None
        """
        self.logger.info('Заполнение формы данных нового пользователя')
        self.enter_text(*UserPageLocators.INPUT_NAME, text=name)
        self.enter_text(*UserPageLocators.INPUT_EMAIL, text=email)
        self.enter_text(*UserPageLocators.INPUT_PASS, text=password)
        self.enter_text(*UserPageLocators.INPUT_CONFIRM_PASS, text=password)
        self.click_to_element_with_offset(*UserPageLocators.LICENSES, x=0, y=0)
        self.click_to_element_with_offset(*UserPageLocators.REGISTRATION)
