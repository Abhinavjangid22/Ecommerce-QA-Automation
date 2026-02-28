from utilities.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

def test_add_to_cart():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()

    time.sleep(2)

    assert inventory.get_cart_count() == "1"

    driver.quit()