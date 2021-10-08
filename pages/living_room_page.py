from pages.base_page import BasePage
from pages.locators import LivingRoomPageLocators, HomePageLocators
from selenium.webdriver.common.by import By
import allure
import time


class LivingRoom(BasePage):
    @allure.step('Переход к разделу Гостиная > Стенки')
    def go_to_living_room_walls(self):
        self.logger.info('Переход к разделу Гостиная > Стенки')
        self.click_to_element(*HomePageLocators.HEADER_LIVING_ROOM)
        self.click_to_element(*LivingRoomPageLocators.WALLS)

    @allure.step('Получение списка цен товаров')
    def get_list_goods_by_price(self, wait_time: int = 3):
        """
        :param wait_time: Временная задержка перед получением списка
        :return: list_price: Список цен всех отображаемых товаров
        """
        self.logger.info('Получение списка цен товаров')
        time.sleep(wait_time)
        elements = self.browser.find_elements(*LivingRoomPageLocators.BLOCK_ELEMENTS)
        elements = [i + 1 for i in range(len(elements))]
        list_price = []
        for i in elements:
            elem = self.browser.find_element(By.CSS_SELECTOR, LivingRoomPageLocators.BLOCK_ELEMENTS_PRICE.format(i))
            list_price.append(int(elem.text.replace(' ', '')))
        return list_price

    @allure.step('Проверка отображения стикера')
    def check_sticker_display_advise(self, wait_time: int = 3):
        """
        :param wait_time: Временная задержка перед получением списка
        :return: None
        """
        self.logger.info(f'Проверка отображения стикера')
        time.sleep(wait_time)
        elements = self.browser.find_elements(*LivingRoomPageLocators.BLOCK_ELEMENTS)
        print(len(elements))
        if len(elements) == 0:
            self.logger.error("Не найдено ни одного элемента")
            raise Exception("Не найдено ни одного элемента")
        else:
            elements = [i + 1 for i in range(len(elements))]
        for i in elements:
            self.waiting_for_element_present(By.XPATH, LivingRoomPageLocators.STICKER_ADVISE.format(i))
