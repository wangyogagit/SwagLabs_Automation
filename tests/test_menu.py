# tests/test_menu.py
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.menu_page import MenuPage

class MenuTests(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作，初始化WebDriver和LoginPage、MenuPage对象，并登录"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.menu_page = MenuPage(self.driver)
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

    def tearDown(self):
        """测试后的清理工作，关闭浏览器"""
        self.driver.quit()

    def test_open_menu(self):
        """测试打开菜单"""
        self.menu_page.open_menu()
        self.assertIn("bm-menu", self.driver.page_source)

    def test_logout(self):
        """测试注销功能"""
        self.menu_page.logout()
        self.assertIn("saucedemo", self.driver.current_url)

    def test_reset_app_state(self):
        """测试重置应用状态功能"""
        self.menu_page.reset_app_state()
        self.assertIn("inventory", self.driver.current_url)

    def test_go_to_all_items(self):
        """测试点击所有商品按钮"""
        self.menu_page.go_to_all_items()
        self.assertIn("inventory", self.driver.current_url)

    def test_go_to_about(self):
        """测试点击关于按钮"""
        self.menu_page.go_to_about()
        self.assertIn("https://saucelabs.com/", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()