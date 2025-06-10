import webbrowser

import pytest

from Pageobject.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customeLogger import LogGen

class Test_001_Login:
    baseURL=Readconfig.getApplicationURL()
    userID=Readconfig.getUserID()
    password=Readconfig.getPassword()

    logger=LogGen.loggen()
    @pytest.mark.regression

    def test_homePageTitle (self, setup):
        self.logger.info("Test_001_Login")
        self.logger.info("Verifying Home Page Title")
        print("This is base URL")
        print(self.baseURL)
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title== "GTPL Bank Home Page":
            assert True
            self.driver.close()
            self.logger.info("Home page title test is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("Home page title is failed")
            assert False

    @pytest.mark.Sanity
    @pytest.mark.regression

    def test_login(self,setup):
        self.logger.info("Test_002_Login")
        self.logger.info("Verifying Login Test")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserID(self.userID)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="GTPL Bank Manager HomePage":
            assert True
            self.driver.close()
            self.logger.info("Login test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            assert False
            # self.driver.close()
            # self.driver.error("Login test failed")


webbrowser.open("report.html")

