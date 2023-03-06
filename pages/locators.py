# вынесли селекторы внешними переменными, переменная - кортеж из двух элементов
from selenium.webdriver.common.by import By

#class MainPageLocators():    # (v.4.2 step 7)
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")       # (v.4.2 step 7)


class BasePageLocators():
    USER_ICON                   = (By.CSS_SELECTOR, ".icon-user")                                                                                                                                   # (v.4.3 step 13)
    SELECT_LANGUAGE_LINK        = (By.CSS_SELECTOR, "#language_selector > div > select")                                                                                                            # Выпадающий список языков
    BUTTON_PERFORM_LINK         = (By.CSS_SELECTOR, '#language_selector > button')                                                                                                                  # Кнопка "Выполнить"
    BUTTON_SIGN_IN_OR_UP        = (By.CSS_SELECTOR, '#login_link')                                                                                                                                  # Кнопка "Войти или зарегистрироваться"
    BUTTON_SIGN_IN_OR_UP_INVALID= (By.CSS_SELECTOR, '#login_link_inc')                                                                                                                              # Кнопка Инвалид "Войти или зарегистрироваться"
    BUTTON_ACCOUNTS_LINK        = (By.CSS_SELECTOR, '#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a')                                                   # Кнопка "Аккаунт"
    BUTTON_LOGOUT_LINK          = (By.CSS_SELECTOR, '#logout_link')                                                                                                                                 # Кнопка "Выход"
    BUTTON_VIEW_BASKET_LINK     = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')                                                   # Кнопка "Посмотреть корзину"
    FIELD_FIND_LINK             = (By.CSS_SELECTOR, '#id_q')                                                                                                                                        # Поле: "Найти"
    BUTTON_FIND_LINK            = (By.CSS_SELECTOR, '#default > header > div.navbar.primary.navbar-static-top.navbar-inverse > div > div.navbar-collapse.primary-collapse.collapse > form > input') # Кнопка "Найти"
    BUTTON_CLOTHING_LINK        = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(3) > a')                                                                                                      # Кнопка "Clothing"
    BUTTON_BOOKS_LINK           = (By.CSS_SELECTOR, '#browse > li > ul > li.dropdown-submenu > a')                                                                                                  # Кнопка "Books"
    BUTTON_OFFERS_LINK          = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(6) > a')                                                                                                      # Кнопка "Предложения"


class LoginAndRegistrationLocators():                                               # http://selenium1py.pythonanywhere.com/ru/accounts/login/
    LOGIN_EMAIL_LINK            = (By.CSS_SELECTOR, '#id_login-username')           # Поле ввода email
    LOGIN_PASSWORD_LINK         = (By.CSS_SELECTOR, '#id_login-password')           # Поле ввода пароля
    LOGIN_BUTTON_LINK           = (By.CSS_SELECTOR, '#login_form > button')         # Кнопка "Войти"
    REGISTER_EMAIL_LINK         = (By.CSS_SELECTOR, '#id_registration-email')       # Поле ввода email
    REGISTER_PASSWORD1_LINK     = (By.CSS_SELECTOR, '#id_registration-password1')   # Поле ввода пароля
    REGISTER_PASSWORD2_LINK     = (By.CSS_SELECTOR, '#id_registration-password2')   # Поле ввода подтверждения пароля
    REGISTER_BUTTON_LINK        = (By.CSS_SELECTOR, '#register_form > button')      # Кнопка "Зарегистрироваться"


class LoginPageLocators():
    LOGIN_BUTTON_LINK = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTER_BUTTON_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')
    

class StoreLocators():                                                                          # https://selenium1py.pythonanywhere.com/ru/
    SUCCESS_REGISTER_ICON_LINK = (By.CSS_SELECTOR, '[class="icon-ok-sign"]')                    # Ярлык успешной регистрации
    SUCCESS_TEXT_EN = (By.CSS_SELECTOR, ' Welcome back ')                                       # Текст успешного повторного захода "Welcome back"
    SUCCESS_TEXT_RU = (By.CSS_SELECTOR, ' Рады видеть вас снова ')                              # Текст успешного повторного захода "Рады видеть вас снова"
    BUTTON_ALL_PRODUCTS_LINK = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(1) > a')     # Кнопка "Все товары"


class ProductPageLocators():                                                                    # https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/
    NAME_LINK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > :nth-child(1)')                  # Наименование товара
    PRICE_LINK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > :nth-child(2)')                 # Стоимость товара  = <p class="price_color">9,99&nbsp;£</p>
    BUTTON_BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')                                # Кнопка добавления в корзину     # add_to_basket_form > button
    CONFIRMATION_NAME_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')   # Название товара в строке подтверждения успешного добавления в корзину.
    CONFIRMATION_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')                 # Запись с результатом добавления в корзину.
    OFFER_DEFERRED_BENEFIT_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div')       # Строка с заключением о соответствии корзины предложению "Deferred benefit offer"
    NAME_OFFER_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div > strong')          # Наименование активного предложения: "Deferred benefit offer"
    OFFER_SHIPPING_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div')               # Строка с заключением о соответствии корзины предложению "Shipping offer"
    OFFER_NORMAL_SITE_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(4) > div')            # Строка с заключением о соответствии корзины предложению "Normal site offer"
    #SUCCESS_TEXT_OF_BASKET_EN = (By.CSS_SELECTOR, ' Your basket now qualifies for the ')                            # Текст: " Your basket now qualifies for the "
    #SUCCESS_TEXT_OF_BASKET_RU = (By.CSS_SELECTOR, ' Ваша корзина удовлетворяет условиям предложения ')              # Текст: " Ваша корзина удовлетворяет условиям предложения "
    #FAILURE_TEXT_OF_BASKET_EN = (By.CSS_SELECTOR, ' Your basket no longer qualifies for the ')                      # Текст: " Your basket no longer qualifies for the " - может быть более 1 записи
    #FAILURE_TEXT_OF_BASKET_RU = (By.CSS_SELECTOR, ' Ваша корзина больше не удовлетворяет условиям предложения ')    # Текст: " Ваша корзина больше не удовлетворяет условиям предложения " - может быть более 1 записи
    # PRODUCT_TEXT2_ACTION_LINK = (By.CSS_SELECTOR, ' offer.')                                                      # Текст: " offer." - "предложение" - нет такого поля -> https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/
    BASKET_TOTAL_LINK = (By.CSS_SELECTOR, 'div.alert-noicon > div > p:nth-child(1) > strong')                       # Стоимость корзины + "&nbsp;£" = "<strong>19,98&nbsp;£</strong>"


class BasketLocators():
    EMPTY_BASKET_LINK = (By.CSS_SELECTOR, '#content_inner > p')                                                 # Запись подтверждающая, что корзина пуста
    LIST_OF_ITEMS_IN_BASKET = (By.CSS_SELECTOR, '#basket_formset')                                              # Список приобретаемых товаров в корзине
    NAME_PAGE_LINK = (By.CSS_SELECTOR, 'div.page-header.action > h1')                                            # Наименование страницы
    ORDER_TOTAL_LINK = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[10]/td/h3/text()')                    # Общая сумма корзины
    NAME_PRODUCT1_LINK = (By.CSS_SELECTOR, '#basket_formset > div:nth-child(6) > div > div.col-sm-4 > h3 > a')   # Наменование первого товара
    AMOUNT_PRODUCT1_LINK = (By.CSS_SELECTOR, '#id_form-0-quantity')                                              # Количество первого товара
    PRICE_PRODUCT1_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[1]/div/div[4]/p/text()')                     # Цена первого товара
    TOTAL_PRODUCT1_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[1]/div/div[5]/p/text()')                     # Сумма первого товара
    NAME_PRODUCT2_LINK = (By.CSS_SELECTOR, '#basket_formset > div:nth-child(7) > div > div.col-sm-4 > h3 > a')   # Наименование второго товара
    AMOUNT_PRODUCT2_LINK = (By.CSS_SELECTOR, '#id_form-1-quantity')                                              # Количество второго товара
    PRICE_PRODUCT2_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[2]/div/div[4]/p/text()')                     # Цена второго товара
    TOTAL_PRODUCT2_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[2]/div/div[5]/p/text()')                     # Сумма второго товара
    CHECKOUT_BUTTON_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[2]/div/div[5]/p/text()')                    # Кнопка "Перейти к оформлению"

class ShippingAddressLocators():
    SHIPPING_RETURN_BUTTON_LINK = (By.CSS_SELECTOR, '#new_shipping_address > div:nth-child(14) > div > a')  # Кнопка "Вернуться в корзину"
    SHIPPING_CONTINUE_BUTTON_LINK = (By.CSS_SELECTOR, 'button.btn-primary')                                 # Кнопка "Продолжить"
    
