from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_UserId_name="uid"
    textbox_password_name="password"
    btn_login_name="btnLogin"

    def __init__(self,driver):
        self.driver=driver

    def setUserID(self,userID):
        self.driver.find_element(By.NAME, self.textbox_UserId_name).clear()
        self.driver.find_element(By.NAME, self.textbox_UserId_name).send_keys(userID)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.NAME, self.btn_login_name).click()