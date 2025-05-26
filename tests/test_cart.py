# tests/test_cart.py
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class CartTests(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作，初始化WebDriver和LoginPage、ProductsPage、CartPage对象，并登录，添加产品到购物车"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        self.products_page.add_product_to_cart()
        self.products_page.go_to_cart()

    def tearDown(self):
        """测试后的清理工作，关闭浏览器"""
        self.driver.quit()

    def test_cart_page_display(self):
        """测试购物车页面是否正确显示"""
        self.assertTrue(self.cart_page.is_cart_page())

    def test_remove_product_from_cart(self):
        """测试从购物车中移除产品"""
        self.cart_page.remove_product_from_cart()
        self.assertEqual(self.cart_page.get_cart_item_count(), 0)

    def test_checkout(self):
        """测试从购物车页面点击结账"""
        self.cart_page.checkout()
        self.assertIn("checkout", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()