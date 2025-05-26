# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        self.username_input = By.ID, "user-name"
        self.password_input = By.ID, "password"
        self.login_button = By.ID, "login-button"
        self.error_message = By.XPATH, "//h3[@data-test='error']"

    def open(self):
        """打开登录页面"""
        self.driver.get(self.url)

    def login(self, username, password):
        """输入用户名和密码并点击登录按钮"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        """获取登录失败时的错误信息"""
        return self.driver.find_element(*self.error_message).text