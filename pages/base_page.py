from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure
import datetime
from PIL import Image
from PIL import ImageChops
import os
from Screenshot import Screenshot_Clipping
from io import BytesIO
import glob
import time


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step('Переход по ссылке')
    def open(self, url: str):
        self.logger.info(f'Переход по ссылке: {url}')
        self.browser.get(url)

    @allure.step('Проверка наличия заголовка страницы')
    def check_title(self, title: str, timeout: int):
        """
        :param title: Искомый заголовок страницы
        :param timeout: Максимальное время ожидания
        :return:
        """
        self.logger.info(f'Проверка наличия заголовка страницы "{title}" с таймаутом {timeout} сек.')
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.title_is(title=title))
        except TimeoutException:
            self.logger.error(f'Заголовок {title} не был найден')
            raise TimeoutError(f"Не дождались заголовка страницы {title}")

    @allure.step('Ожидание отображения элемента')
    def waiting_for_element_present(self, how: str, what: str, timeout: int = 3):
        """
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :param timeout: Максимальное время ожидания
        :return: None
        """
        self.logger.info(f'Ожидание отображения эелемента "{what}" с таймаутом {timeout} сек.')
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            self.logger.error(f'Элемент {what} не был найден')
            raise TimeoutError(f"Элемент {what} не был найден в течение {timeout} секунд(-ы)")

    @allure.step('Ожидание скрытия элемента')
    def waiting_for_element_not_present(self, how: str, what: str, timeout: int = 3):
        """
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :param timeout: Максимальное время ожидания
        :return: None
        """
        self.logger.info(f'Ожидание скрытия эелемента "{what}" с таймаутом {timeout} сек.')
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until_not(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            self.logger.error(f'Элемент {what} отображался')
            raise TimeoutError(f"Элемент {what} отображался в течение {timeout} секунд(-ы)")

    @allure.step('Ожидание скрытия текста')
    def waiting_for_text_not_present(self, how: str, what: str, text: str, timeout: int = 3):
        """
        :param text: Текст который должен быть скрыт
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :param timeout: Максимальное время ожидания
        :return: None
        """
        self.logger.info(f'Ожидание скрытия текста "{text}" с таймаутом "{timeout}"')
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until_not(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            self.logger.error(f'Текст {text} не был скрыт')
            raise TimeoutError(f"Текст {text} не был скрыт в течение {timeout} секунд(-ы)")

    @allure.step('Ожидание кликабельности элемента')
    def waiting_for_element_to_be_clickable(self, how: str, what: str, timeout: int = 5):
        """
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :param timeout: Максимальное время ожидания
        :return: None
        """
        self.logger.info(f'Ожидание кликабельности элемента "{what}" с таймаутом "{timeout}"')
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            self.logger.error(f'Элемент {what} был не кликабелен')
            raise TimeoutError(f"Элемент {what} был не кликабелен в течение {timeout} секунд(-ы)")

    @allure.step('Ожидание отображения текста')
    def waiting_for_text_present(self, how: str, what: str, text: str, timeout: int = 3):
        """
        :param text: Текст который должен отображать
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :param timeout: Максимальное время ожидания
        :return: None
        """
        self.logger.info(f'Ожидание отображения текста "{text}" с таймаутом "{timeout}"')
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            self.logger.error(f'Текст {text} не был найден')
            raise TimeoutError(f"Текст {text} не был найден в течение {timeout} секунд(-ы)")

    @allure.step('Ожидание отображения элемента в DOM дереве страницы')
    def waiting_for_dom_element_present(self, how: str, what: str, timeout: int = 3):
        """
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :param timeout: Максимальное время ожидания
        :return: None
        """
        self.logger.info(f'Ожидание отображения элемента {what} в DOM дереве страницы с таймаутом "{timeout}"')
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            self.logger.error(f'Элемент {what} не был найден в DOM дереве страницы')
            raise TimeoutError(f"Элемент {what} не был найден в DOM дереве страницы в течение {timeout} секунд(-ы)")

    @allure.step('Клик по элементу')
    def click_to_element(self, how: str, what: str):
        """
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :return: None
        """
        self.logger.info(f'Клик по элементу "{what}"')
        self.waiting_for_element_to_be_clickable(how, what)
        try:
            self.browser.find_element(how, what).click()
        except StaleElementReferenceException or NoSuchElementException as er:
            self.logger.error(f'Не удалось кликнуть по элементу {what}')
            raise Exception(f'Не удалось кликнуть по элементу {what}\n {er}')

    @allure.step('Клик по элементу со смещением')
    def click_to_element_with_offset(self, how: str, what: str, x: int = 14, y: int = 14):
        """
        :param x: Смещение по оси X
        :param y: Смещение по оси Y
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :return: None
        """
        self.logger.info(f'Клик по элементу "{what}" со смещением {x}, {y}')
        self.waiting_for_element_to_be_clickable(how, what)
        try:
            element = self.browser.find_element(how, what)
            ActionChains(self.browser).move_to_element_with_offset(element, xoffset=x, yoffset=y).click().perform()
        except StaleElementReferenceException or NoSuchElementException as er:
            self.logger.error(f'Не удалось кликнуть по элементу {what}')
            raise Exception(f'Не удалось кликнуть по элементу {what}\n {er}')

    @allure.step('Ввод текста')
    def enter_text(self, how: str, what: str, text: str or int):
        """
        :param text: Текст для ввода
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :return: None
        """
        self.logger.info(f'Ввод текста "{text}"')
        self.waiting_for_element_present(how, what)
        try:
            self.browser.find_element(how, what).send_keys(text)
        except NoSuchElementException as er:
            self.logger.error(f'Не удалось ввести текст {text}')
            raise Exception(f'Не удалось ввести текст {text}\n {er}')

    @allure.step('Получение значение атрибута')
    def get_value(self, how: str, what: str, attribute: str):
        """
        :param attribute: Название атрибута
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :return: None
        """
        self.logger.info(f'Получение значение атрибута {attribute} из поля "{what}"')
        self.waiting_for_element_present(how, what)
        return self.browser.find_element(how, what).get_attribute(attribute)

    @allure.step('Наведение курсора на элемент')
    def place_the_cursor(self, how: str, what: str):
        """
        :param how: Как искать (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор
        :return: None
        """
        self.logger.info(f'Наведение курсора на элемент "{what}"')
        self.waiting_for_element_present(how, what)
        try:
            ActionChains(self.browser).move_to_element(self.browser.find_element(how, what)).perform()
        except NoSuchElementException as er:
            self.logger.error(f'Не удалось навести курсор на элемент {what}')
            raise Exception(f'Не удалось навести курсор на элемент {what}\n {er}')

    @allure.step('Добавление товара из меню по ховеру')
    def add_items_from_the_menu_by_hover(self, how: str, what: str, how_basket: str, what_basket: str):
        """
        :param how: Как искать товар (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what: Составной селектор товара
        :param how_basket: Как искать иконку корзины (By.ID, By.CSS_SELECTOR, By.XPATH, и так далее...)
        :param what_basket: Составной селектор иконки корзины
        :return: None
        """
        self.logger.info(f'Добавление товара из меню по ховеру')
        self.place_the_cursor(how, what)
        self.click_to_element(how_basket, what_basket)

    @allure.step('Создание скриншота веб-элемента')
    def create_screenshot_element(self, request, locator: tuple, save_path: str = '../screenshots/',
                                  wait_time: int = 3):
        """
        :param request: Здесь указать стандартную фикстуру request
        :param locator: Кортеж из способа поиска и составного селектора веб-элемента
        (например: (By.CSS_SELECTOR, '.catalog_block.block div.col-lg-3'))
        :param save_path: Путь сохранения скриншота
        :param wait_time: Временная задержка перед работой метода
        :return: new_img_url: Путь до созданного скриншота
        """
        self.logger.info(f'Создание скриншота веб-элемента')
        time.sleep(wait_time)
        test_time = str(datetime.datetime.now()).replace('.', '').replace('-', '').replace(' ', '_').replace(':', '')
        current_path = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
        filename = "screenshots_" + request.node.name + "_" + test_time[:16] + ".png"
        ob = Screenshot_Clipping.Screenshot()
        img_url = ob.get_element(driver=self.browser, element=self.browser.find_element(*locator),
                                 save_location=save_path)
        new_img_url = os.path.normpath(os.path.join(os.path.join(current_path, save_path), filename))
        os.rename(img_url, new_img_url)
        os.remove(os.path.normpath(os.path.join(os.path.join(current_path, save_path), 'clipping_shot.png')))
        self.logger.info('Сохранено ' + new_img_url)
        return new_img_url

    @allure.step('Сверка изображений страницы')
    def reconciliation_with_images(self, request, image_path: str, save_path: str = '../screenshots/',
                                   expected_path: str = '../screenshots/expected/', clear_files: bool = True):
        """
        :param request: Здесь указать стандартную фикстуру request
        :param image_path: Путь до изображения которое нужно сравнить
        :param save_path: Путь сохранения скриншота различий
        :param expected_path: Путь до папки с ожидаемыми результатами
        :param clear_files: флаг очистки файлов
        :return: response: True - проверка пройдена
                           False - не пройдена
        """
        self.logger.info(f'Сверка изображений страницы')

        def buff(image):
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            return buffered.getvalue()

        response = False
        current_path = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
        file_list = os.listdir(expected_path)
        test_name = request.node.name
        samples_list = []
        img_res = Image.open(image_path)

        def clear(path=os.path.normpath(os.path.join(current_path, save_path))):
            if clear_files:
                files = glob.glob(path + '\\*.png')
                for f in files:
                    os.remove(f)

        for item in file_list:
            if test_name in item:
                samples_list.append(item)
        if not samples_list:
            self.logger.error('Не найдено ни одного образца для сравнения')
            raise Exception('Не найдено ни одного образца для сравнения')

        for file in samples_list:
            file = os.path.normpath(os.path.join(os.path.join(current_path, expected_path), file))
            img = Image.open(file)
            img_diff = ImageChops.difference(img_res, img)
            if img_diff.getbbox() is None:
                self.logger.info('Полученное изображение сходится с ожидаемым')
                response = True
                clear()
                break
            else:
                diff_path = os.path.normpath(os.path.join(save_path, "diff_" + test_name + ".png"))
                img_diff.save(diff_path)
                self.logger.error('Полученное изображение не сходится с ожидаемым')
                allure.attach(
                    body=buff(img_diff),
                    name='diff',
                    attachment_type=allure.attachment_type.PNG
                )
                allure.attach(
                    body=buff(img),
                    name='expected',
                    attachment_type=allure.attachment_type.PNG
                )
                allure.attach(
                    body=buff(img_res),
                    name='actual',
                    attachment_type=allure.attachment_type.PNG
                )
                clear()
                raise Exception('Полученное изображение не сходится с ожидаемым')

        return response
