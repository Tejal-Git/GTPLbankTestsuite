import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pageobject.LoginPage import LoginPage
import time
from Utilities.readProperties import Readconfig
from Utilities.customeLogger import LogGen
from Utilities import XLUtility

class Test_002_DDT_Login:
    baseURL=Readconfig.getApplicationURL()
    path=".//TestData/testdata2(GTP).xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("Test_002_DDT_Login")
        self.logger.info("Verifying Test_002_DDT_Login")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtility.getRowCount(self.path, "Sheet1")
        print("Number of rows in a excel:", self.rows)

        lst_status=[]

        for r in range (2, self.rows+1):
            self.user=XLUtility.readData(self.path, 'Sheet1', r, 1)
            self.password=XLUtility.readData(self.path, 'Sheet1', r, 2)
            self.exp=XLUtility.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserID(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            try:
                self.logger.info("Login failed with username",self.user)
                WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                print("Alert is present with text:", alert.text)
                alert.accept()
                lst_status.append('pass')
            except:
                act_title = self.driver.title
                exp_title = "GTPL Bank Manager HomePage"
                if act_title == exp_title:
                    if self.exp == 'pass':
                        self.logger.info("Login passed with username", self.user)
                        self.lp.clickLogout();
                        alertwindow = self.driver.switch_to.alert
                        print(alertwindow.text)
                        alertwindow.accept()
                        lst_status.append("pass")

        if 'fail' not in lst_status:
            self.logger.info("Test_002_DDT_Login test is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Test_002_DDT_Login test is failed")
            self.driver.close()
            assert False

        self.logger.info("End of the login DDT test")
        self.logger.info("Test_002_DDT_Login test completed")


#webbrowser.open("report.html")
