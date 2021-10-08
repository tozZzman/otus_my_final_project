from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import KitchenPageLocators, HomePageLocators
import allure


class KitchenPage(BasePage):
    @allure.step('Переход к разделу Кухни > Стулья')
    def go_to_kitchen_section_chairs(self):
        self.logger.info('Переход к разделу Кухни > Стулья')
        self.click_to_element(*HomePageLocators.HEADER_KITCHEN)
        self.click_to_element(*KitchenPageLocators.KITCHEN_CHAIRS)

    @allure.step('Проверка иконок товара по ховеру')
    def check_product_icons(self, product_id: str):
        """
        :param product_id: CSS-идентификатор продукта для которого необходимо проверить иконки
        :return: None
        """
        self.logger.info(f'Проверка иконок товара {product_id} по ховеру')
        self.place_the_cursor(By.ID, product_id)
        self.waiting_for_element_present(By.XPATH, KitchenPageLocators.ICON_POSTPONE.format(product_id))
        self.waiting_for_element_present(By.XPATH, KitchenPageLocators.ICON_COMPARE.format(product_id))
        self.waiting_for_element_present(By.XPATH, KitchenPageLocators.ICON_BUY.format(product_id))
        self.waiting_for_element_present(By.XPATH, KitchenPageLocators.ICON_VIEWING.format(product_id))
