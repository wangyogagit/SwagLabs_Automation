# tests/test_checkout.py
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class CheckoutTests(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作，初始化WebDriver和LoginPage、ProductsPage、CartPage、CheckoutPage对象，并登录，添加产品到购物车，进入结账页面"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        self.products_page.add_product_to_cart()
        self.products_page.go_to_cart()
        self.cart_page.checkout()

    def tearDown(self):
        """测试后的清理工作，关闭浏览器"""
        self.driver.quit()

    def test_checkout_page_display(self):
        """测试结账页面是否正确显示"""
        self.assertTrue(self.checkout_page.is_checkout_page())

    def test_complete_checkout(self):
        """测试完成结账流程"""
        self.checkout_page.fill_checkout_info("John", "Doe", "12345")
        self.checkout_page.finish_checkout()
        self.assertIn("checkout-complete", self.driver.current_url)
        self.assertEqual("Thank you for your order!", self.checkout_page.get_order_complete_message())

if __name__ == "__main__":
    unittest.main()