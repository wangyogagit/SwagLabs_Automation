# pages/menu_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = By.ID, "react-burger-menu-btn"
        self.logout_button = By.ID, "logout_sidebar_link"
        self.reset_app_state_button = By.ID, "reset_sidebar_link"
        self.all_items_button = By.ID, "inventory_sidebar_link"
        self.about_button = By.ID, "about_sidebar_link"

    def open_menu(self):
        """打开菜单"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.menu_button)).click()

    def logout(self):
        """点击注销按钮"""
        self.open_menu()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button)).click()

    def reset_app_state(self):
        """点击重置应用状态按钮"""
        self.open_menu()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.reset_app_state_button)).click()

    def go_to_all_items(self):
        """点击所有商品按钮"""
        self.open_menu()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.all_items_button)).click()

    def go_to_about(self):
        """点击关于按钮"""
        self.open_menu()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.about_button)).click()