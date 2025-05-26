# tests/test_login.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

class LoginTests(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作，初始化WebDriver和LoginPage对象"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        """测试后的清理工作，关闭浏览器"""
        self.driver.quit()

    def test_login_success(self):
        """测试使用有效用户登录成功"""
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        url = self.driver.current_url
        self.assertIn("inventory", url)

    def test_login_failure(self):
        """测试使用无效用户登录失败"""
        self.login_page.open()
        self.login_page.login("invalid_user", "secret_sauce")
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", self.login_page.get_error_message())

    def test_locked_out_user(self):
        """测试使用被锁定的用户登录失败"""
        self.login_page.open()
        self.login_page.login("locked_out_user", "secret_sauce")
        self.assertEqual("Epic sadface: Sorry, this user has been locked out.", self.login_page.get_error_message())

    def test_problem_user(self):
        """测试使用问题用户登录成功"""
        self.login_page.open()
        self.login_page.login("problem_user", "secret_sauce")
        self.assertIn("inventory", self.driver.current_url)

    def test_problem_user_with_same_image(self):
        """<UNK>"""
        self.login_page.open()
        self.login_page.login("problem_user", "secret_sauce")

        inventory_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        image_sources = [item.find_element(By.TAG_NAME, "img").get_attribute("src") for item in inventory_items]

        if image_sources:
            first_image_source = image_sources[0]
            self.assertTrue(all(src == first_image_source for src in image_sources))
        else:
            self.fail("No images found")

    def test_performance_glitch_user(self):
        """测试使用性能故障用户登录成功"""
        self.login_page.open()
        self.login_page.login("performance_glitch_user", "secret_sauce")
        self.assertIn("inventory", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()