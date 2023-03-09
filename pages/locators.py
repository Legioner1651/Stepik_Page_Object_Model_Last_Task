from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON                   = (By.CSS_SELECTOR, ".icon-user")                                                                                                                                   # Icon: Account
    SELECT_LANGUAGE_LINK        = (By.CSS_SELECTOR, "#language_selector > div > select")                                                                                                            # Выпадающий список языков
    BUTTON_PERFORM_LINK         = (By.CSS_SELECTOR, '#language_selector > button')                                                                                                                  # Кнопка "Выполнить"
    BUTTON_SIGN_IN_OR_UP        = (By.CSS_SELECTOR, '#login_link')                                                                                                                                  # Кнопка "Войти или зарегистрироваться"
    BUTTON_SIGN_IN_OR_UP_INVALID= (By.CSS_SELECTOR, '#login_link_inc')                                                                                                                              # Инвалид "Войти или зарегистрироваться"
    BUTTON_ACCOUNTS_LINK        = (By.CSS_SELECTOR, '#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a')                                                   # Кнопка "Аккаунт"
    BUTTON_LOGOUT_LINK          = (By.CSS_SELECTOR, '#logout_link')                                                                                                                                 # Кнопка "Выход"
    BUTTON_VIEW_BASKET_LINK     = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')                                                   # Кнопка "Посмотреть корзину"
    FIELD_FIND_LINK             = (By.CSS_SELECTOR, '#id_q')                                                                                                                                        # Поле: "Найти"
    BUTTON_FIND_LINK            = (By.CSS_SELECTOR, '#default > header > div.navbar.primary.navbar-static-top.navbar-inverse > div > div.navbar-collapse.primary-collapse.collapse > form > input') # Кнопка "Найти"
    BUTTON_ALL_PRODUCTS_LINK    = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(1) > a')                                                                                                      # Кнопка "All products"
    BUTTON_CLOTHING_LINK        = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(3) > a')                                                                                                      # Кнопка "Clothing"
    BUTTON_BOOKS_LINK           = (By.CSS_SELECTOR, '#browse > li > ul > li.dropdown-submenu > a')                                                                                                  # Кнопка "Books"
    BUTTON_OFFERS_LINK          = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(6) > a')                                                                                                      # Кнопка "Предложения"
    SUCCESS_REGISTER_ICON_LINK  = (By.CSS_SELECTOR, '[class="icon-ok-sign"]')                                                                                                                       # Ярлык успешного входа (login)


class LoginAndRegistrationLocators():
    LOGIN_EMAIL_LINK            = (By.CSS_SELECTOR, '#id_login-username')           # Поле ввода email
    LOGIN_PASSWORD_LINK         = (By.CSS_SELECTOR, '#id_login-password')           # Поле ввода пароля
    LOGIN_BUTTON_LINK           = (By.CSS_SELECTOR, '#login_form > button')         # Кнопка "Войти"
    REGISTER_EMAIL_LINK         = (By.CSS_SELECTOR, '#id_registration-email')       # Поле ввода email
    REGISTER_PASSWORD1_LINK     = (By.CSS_SELECTOR, '#id_registration-password1')   # Поле ввода пароля
    REGISTER_PASSWORD2_LINK     = (By.CSS_SELECTOR, '#id_registration-password2')   # Поле ввода подтверждения пароля
    REGISTER_BUTTON_LINK        = (By.CSS_SELECTOR, '#register_form > button')      # Кнопка "Зарегистрироваться"


class ProductPageLocators():
    NAME_LINK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > :nth-child(1)')                  # Наименование товара
    PRICE_LINK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > :nth-child(2)')                 # Стоимость товара
    BUTTON_BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')                                # Кнопка добавления в корзину
    CONFIRMATION_NAME_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')   # Название товара в строке подтверждения успешного добавления в корзину.
    CONFIRMATION_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')                 # Запись с результатом добавления в корзину.
    OFFER_DEFERRED_BENEFIT_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div')       # Строка с заключением о соответствии корзины предложению "Deferred benefit offer"
    NAME_OFFER_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div > strong')          # Наименование активного предложения: "Deferred benefit offer"
    OFFER_SHIPPING_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div')               # Строка с заключением о соответствии корзины предложению "Shipping offer"
    OFFER_NORMAL_SITE_LINK = (By.CSS_SELECTOR, '#messages > div:nth-child(4) > div')            # Строка с заключением о соответствии корзины предложению "Normal site offer"
    BASKET_TOTAL_LINK = (By.CSS_SELECTOR, 'div.alert-noicon > div > p:nth-child(1) > strong')   # Стоимость корзины


class BasketLocators():
    EMPTY_BASKET_LINK = (By.CSS_SELECTOR, '#content_inner > p')                                                 # Запись подтверждающая, что корзина пуста
    LIST_OF_ITEMS_IN_BASKET = (By.CSS_SELECTOR, '#basket_formset')                                              # Список приобретаемых товаров в корзине
    NAME_PAGE_LINK = (By.CSS_SELECTOR, 'div.page-header.action > h1')                                           # Наименование страницы
    ORDER_TOTAL_LINK = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[10]/td/h3/text()')                   # Общая сумма корзины
    NAME_PRODUCT1_LINK = (By.CSS_SELECTOR, '#basket_formset > div:nth-child(6) > div > div.col-sm-4 > h3 > a')  # Наименование первого товара
    AMOUNT_PRODUCT1_LINK = (By.CSS_SELECTOR, '#id_form-0-quantity')                                             # Количество первого товара
    PRICE_PRODUCT1_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[1]/div/div[4]/p/text()')                    # Цена первого товара
    TOTAL_PRODUCT1_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[1]/div/div[5]/p/text()')                    # Сумма первого товара
    NAME_PRODUCT2_LINK = (By.CSS_SELECTOR, '#basket_formset > div:nth-child(7) > div > div.col-sm-4 > h3 > a')  # Наименование второго товара
    AMOUNT_PRODUCT2_LINK = (By.CSS_SELECTOR, '#id_form-1-quantity')                                             # Количество второго товара
    PRICE_PRODUCT2_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[2]/div/div[4]/p/text()')                    # Цена второго товара
    TOTAL_PRODUCT2_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[2]/div/div[5]/p/text()')                    # Сумма второго товара
    CHECKOUT_BUTTON_LINK = (By.XPATH, '//*[@id="basket_formset"]/div[2]/div/div[5]/p/text()')                   # Кнопка "Перейти к оформлению"
