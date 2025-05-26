# pages/cart_page.py
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_title = By.XPATH, "//span[@class='title']"
        self.remove_button = By.ID, "remove-sauce-labs-backpack"
        self.cart_items = By.CLASS_NAME, "cart_item"
        self.checkout_button = By.ID, "checkout"

    def is_cart_page(self):
        """检查是否在购物车页面"""
        return self.driver.find_element(*self.cart_title).text == "Your Cart"

    def remove_product_from_cart(self):
        """从购物车中移除产品"""
        self.driver.find_element(*self.remove_button).click()

    def get_cart_item_prices(self):
        """获取购物车中的产品价格"""
        return [item.text for item in self.driver.find_elements(*self.cart_item_prices)]

    def get_cart_item_count(self):
        """获取购物车中的产品数量"""
        return len(self.driver.find_elements(*self.cart_items))

    def checkout(self):
        """点击结账按钮"""
        self.driver.find_element(*self.checkout_button).click()