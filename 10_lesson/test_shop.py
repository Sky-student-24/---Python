from selenium import webdriver
from Pages.MainShopPage1 import MainShopPage
from Pages.ShopPage1 import ShopPage
from Pages.BasketPage1 import BasketPage
from Pages.FormPage1 import FormPage
import allure


@allure.title("Магазин")
@allure.feature("Mozilla Firefox")
@allure.severity("normal")
@allure.description("Проверка рабостоспособности всех элементов онлайн-магазина")
def test_calculator():
    driver = webdriver.Firefox()

    main_page = MainShopPage(driver)
    with allure.step("Авторизация"):
        main_page.authorization()

    shop_page = ShopPage(driver)
    with allure.step("Заполнение корзины товарами"):
        shop_page.shop()

    basket_page = BasketPage(driver)
    with allure.step("Переход в корзину"):
        basket_page.get()
    with allure.step("Проверка, что выбранные товары есть в корзине"):
        basket_page.check()

    form_page = FormPage(driver)
    with allure.step("Заполнение формы данными"):
        form_page.form()

    total = form_page.total()
    with allure.step("Сравнение итоговой цены"):
        total_value = total.split("$")[-1]
        assert total_value == "58.29"

    driver.quit()
