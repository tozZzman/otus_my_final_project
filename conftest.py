import os
import sys
import pytest
from selenium import webdriver
import logging
import allure

sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))), '..')))

from pages.base_page import BasePage
from pages.locators import HomePageLocators, BasePageLocators

logging.basicConfig(level=logging.INFO, filename='../logs/log.log', format='%(levelname)s %(asctime)s %(message)s')


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     help='Выбор браузера',
                     choices=['chrome', 'firefox', 'opera'],
                     default='chrome')
    parser.addoption('--url',
                     action='store',
                     help='Адрес тестируемого сервиса',
                     default='https://mebel.max-demo.ru/')
    parser.addoption('--executor',
                     action='store',
                     help='Адрес удаленного сервера для запуска тестов',
                     default='192.168.31.145')
    parser.addoption('--browser_ver',
                     action='store',
                     help='Версия браузера',
                     default='92')
    parser.addoption('--vnc',
                     action='store_true',
                     help='Опция Selenoid VNC',
                     )
    parser.addoption('--video',
                     action='store_true',
                     help='Опция Selenoid VIDEO',
                     )


@pytest.fixture(scope='function')
def browser(request):
    bwr = request.config.getoption('--browser')
    logger = logging.getLogger('BrowserLogger')
    executor = request.config.getoption('--executor')
    browser_ver = request.config.getoption('--browser_ver')
    vnc = request.config.getoption('--vnc')
    video = request.config.getoption('--video')

    logger.info(f'====== Запущен тест {request.node.name} ======')

    if executor == 'local':
        if bwr == 'chrome':
            caps = {'goog.chromeOptions': {}}
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(desired_capabilities=caps, options=options)
        elif bwr == 'firefox':
            driver = webdriver.Firefox()
        elif bwr == 'opera':
            driver = webdriver.Opera()
        else:
            raise ValueError(f"Driver not suported: {bwr}")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            'browserName': bwr,
            'browserVersion': browser_ver,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": video
            }
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps

        )
    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info('====== Тест завершен ======')

    request.addfinalizer(fin)

    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode):
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                    logging.info("Сделан снимок экрана")
                else:
                    logging.error('Не удалось сделать снимок экрана')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            logging.error('Не удалось сделать снимок экрана: {}'.format(e))


@pytest.fixture(scope='function')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='function')
def removing_products_from_the_sidebar(request, browser):
    logging.info('Очистка товаров в боковой панели добавленных товаров')

    def fin():
        client = BasePage(browser)
        client.click_to_element(*BasePageLocators.REMOVE_BASKET)

    request.addfinalizer(fin)


@pytest.fixture(scope='function')
def add_product_to_cart(browser, url):
    logging.info('Добавление товара в боковую панель')
    client = BasePage(browser)
    client.open(url)
    client.add_items_from_the_menu_by_hover(*HomePageLocators.PRODUCT_SOFA)
