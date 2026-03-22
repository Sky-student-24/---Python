from selenium import webdriver
from Pages.MainShopPage import MainShopPage
from Pages.ShopPage import ShopPage
from Pages.BasketPage import BasketPage
from Pages.FormPage import FormPage


def test_calculator():
    driver = webdriver.Firefox()

    main_page = MainShopPage(driver)
    main_page.authorization()

    shop_page = ShopPage(driver)
    shop_page.shop()

    basket_page = BasketPage(driver)
    basket_page.get()
    basket_page.check()

    form_page = FormPage(driver)
    form_page.form()

    total = form_page.total()
    total_value = total.split("$")[-1]
    assert total_value == "58.29"

    driver.quit()
