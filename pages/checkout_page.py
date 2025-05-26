# pages/checkout_page.py
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_title = By.XPATH, "//span[@class='title']"
        self.first_name_input = By.ID, "first-name"
        self.last_name_input = By.ID, "last-name"
        self.zip_code_input = By.ID, "postal-code"
        self.continue_button = By.ID, "continue"
        self.finish_button = By.ID, "finish"
        self.order_complete_message = By.XPATH, "//h2[@class='complete-header']"

    def is_checkout_page(self):
        """检查是否在结账页面"""
        return self.driver.find_element(*self.checkout_title).text == "Checkout: Your Information"

    def fill_checkout_info(self, first_name, last_name, zip_code):
        """填写结账信息"""
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def finish_checkout(self):
        """完成结账"""
        self.driver.find_element(*self.finish_button).click()

    def get_order_complete_message(self):
        """获取订单完成信息"""
        return self.driver.find_element(*self.order_complete_message).text