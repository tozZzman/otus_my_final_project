from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET = (By.CSS_SELECTOR, '.wraps_icon_block.basket')
    ENTRANCE = (By.CSS_SELECTOR, '.personal.top.login.font_upper')
    PRODUCT_BASKET = (By.CSS_SELECTOR, '#basket_form .basket_wrap .wrap.clearfix img')
    REMOVE_BASKET = (By.CSS_SELECTOR, 'span.remove_all_basket')
    FAVORITES = (By.CSS_SELECTOR, '.colored_theme_hover_text.wish_count.clicked')
    HEADER_TABS_FAVORITES = (By.XPATH, '//ul[@class="tabs"]/li[@item-section="DelDelCanBuy"]')
    PRODUCT_FAVORITES = (By.CSS_SELECTOR, '#basket_form .basket_wrap.delayed .wrap.clearfix img')
    COMPARISON = (By.CSS_SELECTOR, '.colored_theme_hover_text.compare_count.small')
    PRODUCT_COMPARISON = (By.CSS_SELECTOR, '#bx_560410812_3985 img.lazyloaded')
    REMOVE_PRODUCT_COMPARISON = (By.CSS_SELECTOR, '#bx_560410812_3985 .remove.colored_theme_hover_text')


class HomePageLocators:
    PRODUCT_SOFA = (By.ID, 'bx_3966226736_3051', By.ID, 'bx_3966226736_3051_basket_actions')
    PRODUCT_LITTLE_TABLE = (By.ID, 'bx_3966226736_3880', By.CSS_SELECTOR,
                            '#bx_3966226736_3880 .wish_item.to.rounded3.colored_theme_hover_bg')
    PRODUCT_KITCHEN = (By.ID, 'bx_3966226736_3985', By.CSS_SELECTOR, '#bx_3966226736_3985 .compare_item_button')
    HEADER_KITCHEN = (By.XPATH, '''//a/div[contains(text(),'Кухня и столовая')]''')
    HEADER_LIVING_ROOM = (By.XPATH, '''//a/div[contains(text(),'Гостиная')]''')


class PersonalDataLocators:
    PERSONAL_DATA = (By.XPATH, '//li[@class="v_bottom item    item "]/a[@href="/personal/private/"]')
    PERSONAL_DATA_NAME = (By.NAME, 'NAME')
    PERSONAL_DATA_EMAIL = (By.NAME, 'EMAIL')
    EXIT = (By.XPATH, "//div[@class='left_block sticky-sidebar']//a/span[contains(text(),'Выйти')]")


class UserPageLocators:
    LOGIN = (By.ID, 'USER_LOGIN_POPUP')
    PASS = (By.ID, 'USER_PASSWORD_POPUP')
    BUTTON_IN = (By.CSS_SELECTOR, '.form_footer button')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'div.buttons.clearfix  a')
    INPUT_NAME = (By.ID, 'input_NAME')
    INPUT_EMAIL = (By.ID, 'input_EMAIL')
    INPUT_PASS = (By.ID, 'input_PASSWORD')
    INPUT_CONFIRM_PASS = (By.ID, 'input_CONFIRM_PASSWORD')
    LICENSES = (By.CSS_SELECTOR, '.licence_block.filter.label_block.onoff label')
    REGISTRATION = (By.NAME, 'register_submit_button1')


class KitchenPageLocators:
    KITCHEN_CHAIRS = (By.CSS_SELECTOR, '#bx_1847241719_371 .image.with-icons')
    KITCHEN_BLOCK = (By.CSS_SELECTOR, '.inner_wrapper')
    ICON_SMALL_LIST = (By.CSS_SELECTOR, '.filter-panel__view.controls-linecount.pull-right .controls-view__link.muted')
    ICON_POSTPONE = '//div[@id="{}"]//span[@title="Отложить"]'
    ICON_COMPARE = '//div[@id="{}"]//span[@title="Сравнить"]'
    ICON_BUY = '//div[@id="{}"]//span[@title="Купить в 1 клик"]'
    ICON_VIEWING = '//div[@id="{}"]//span[@title="Быстрый просмотр"]'
    ID_PRODUCT_1 = 'bx_3966226736_3480'
    ID_PRODUCT_2 = 'bx_3966226736_3478'
    ID_PRODUCT_3 = 'bx_3966226736_3479'
    ID_PRODUCT_4 = 'bx_3966226736_3482'


class LivingRoomPageLocators:
    WALLS = (By.CSS_SELECTOR, '#bx_1847241719_358 .image.with-icons')
    SELECT_SORTING = (By.CSS_SELECTOR, '.dropdown-select')
    SELECT_SORTING_OPTIONS = '.dropdown-menu-inner.rounded3 div:nth-child({})'
    BLOCK_ELEMENTS = (By.CSS_SELECTOR, '.catalog_block.block div.col-lg-3')
    BLOCK_ELEMENTS_PRICE = '.catalog_block.block div.col-lg-3:nth-child({}) .price_value'
    FILTER_MIN_PRICE = (By.ID, 'MAX_SMART_FILTER_P1_MIN')
    FILTER_MAX_PRICE = (By.ID, 'MAX_SMART_FILTER_P1_MAX')
    STICKER_ADVISE = '//div[@id="bx_3966226736_3881"]/div[{}]//div[@class="sticker_sovetuem ' \
                     'font_sxs rounded2" and contains(text(),"Советуем")]'
    CHECKBOX_ADVISE = (By.XPATH, '//span[@title="Советуем"]')
