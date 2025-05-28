# tests/test_products.py
import unittest
from selenium import webdriver

from pages import products_page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class ProductsTests(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作，初始化WebDriver和LoginPage、ProductsPage对象，并登录"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

    def tearDown(self):
        """测试后的清理工作，关闭浏览器"""
        self.driver.quit()

    def test_products_page_navbar(self):
        self.assertIn("Swag Labs", self.products_page.is_products_page_navbar())

    def test_products_page_display(self):
        """测试产品页面是否正确显示"""
        self.assertTrue(self.products_page.is_products_page())

    def test_add_product_to_cart(self):
        """测试将产品添加到购物车"""
        self.products_page.add_product_to_cart()
        self.products_page.go_to_cart()
        self.assertIn("cart", self.driver.current_url)

    def test_remove_product_from_cart(self):
        """测试从购物车中移除产品"""
        self.products_page.add_product_to_cart()
        self.products_page.go_to_cart()
        initial_item_count = self.cart_page.get_cart_item_count()
        self.cart_page.remove_product_from_cart()
        final_item_count = self.cart_page.get_cart_item_count()
        self.assertLess(final_item_count, initial_item_count)

    def test_sort_products(self):
        """测试产品排序功能"""
        self.products_page.sort_products_by_price_low_to_high()
        prices = self.products_page.get_product_prices()
        self.assertEqual(prices, sorted(prices))

    def test_sort_products_by_name(self):
        """测试按名称排序产品"""
        self.products_page.sort_products_by_name()
        product_names = self.products_page.get_product_names()
        self.assertEqual(product_names, sorted(product_names))

    def test_sort_products_by_price_high_to_low(self):
        """测试按价格从高到低排序产品"""
        self.products_page.sort_products_by_price_high_to_low()
        prices = self.products_page.get_product_prices()
        self.assertEqual(prices, sorted(prices, reverse=True))

    def test_product_details(self):
        """测试产品详情页面"""
        self.products_page.click_product("Sauce Labs Backpack")
        self.assertIn("inventory-item.html", self.driver.current_url)
        self.assertIn("Sauce Labs Backpack", self.driver.page_source)


if __name__ == "__main__":
    unittest.main()