# pages/products_page.py
from jinja2.filters import do_select
from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_title = By.XPATH, "//span[@class='title']"
        self.products_navbar = By.CLASS_NAME, "header_label"
        self.add_to_cart_button = By.ID, "add-to-cart-sauce-labs-backpack"
        self.cart_icon = By.CLASS_NAME, "shopping_cart_link"
        self.sort_dropdown = By.CLASS_NAME, "product_sort_container"
        self.product_names = By.CLASS_NAME, "inventory_item_name"
        self.product_prices = By.CLASS_NAME, "inventory_item_price"

    def is_products_page_navbar(self):
        """check if product page contain navbar"""
        return self.driver.find_element(*self.products_navbar).text

    def is_products_page(self):
        """检查是否在产品页面"""
        return self.driver.find_element(*self.products_title).text == "Products"

    def add_product_to_cart(self, product_name=None):
        """将产品添加到购物车"""
        if product_name:
            add_button = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/following-sibling::button")
        else:
            add_button = self.driver.find_element(*self.add_to_cart_button)
        add_button.click()

    def go_to_cart(self):
        """点击购物车图标进入购物车页面"""
        self.driver.find_element(*self.cart_icon).click()

    def sort_products_by_price_low_to_high(self):
        """按价格从低到高排序产品"""
        self.driver.find_element(*self.sort_dropdown).click()
        self.driver.find_element(By.XPATH, "//option[@value='lohi']").click()

    def sort_products_by_name(self):
        """按名称排序产品"""
        self.driver.find_element(*self.sort_dropdown).click()
        self.driver.find_element(By.XPATH, "//option[@value='az']").click()

    def sort_products_by_price_high_to_low(self):
        """按价格从高到低排序产品"""
        self.driver.find_element(*self.sort_dropdown).click()
        self.driver.find_element(By.XPATH, "//option[@value='hilo']").click()

    def get_product_names(self):
        """获取所有产品名称"""
        return [item.text for item in self.driver.find_elements(*self.product_names)]

    def get_product_prices(self):
        """获取所有产品价格"""
        return [float(item.text.replace("$", "")) for item in self.driver.find_elements(*self.product_prices)]

    def click_product(self, product_name):
        """点击产品进入详情页面"""
        self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']").click()