import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pageobject.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customeLogger import LogGen
import mysql.connector

class Test_003_DDT_Login:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("Starting Test_003_DDT_Login")
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)

        lst_status = []

        # Connect to DB and fetch login data
        try:
            con = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="NoAccess@240998",
                database="Bank"
            )
            curs = con.cursor()
            curs.execute("SELECT * FROM Login")

            rows = curs.fetchall()

            for row in rows:
                username = row[0]
                password = row[1]
                expected = row[2]

                self.driver.get(self.baseURL)
                lp.setUserID(username)
                lp.setPassword(password)
                lp.clickLogin()

                try:
                    WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    print(alert.text)
                    alert.accept()

                    if expected.lower() == "fail":
                        self.logger.info(f"Login failed as expected with username: {username}")
                        lst_status.append("pass")
                    else:
                        self.logger.warning(f"Unexpected login failure with username: {username}")
                        lst_status.append("fail")

                except:
                    # No alert => login success
                    actual_title = self.driver.title
                    expected_title = "GTPL Bank Manager HomePage"

                    if actual_title == expected_title:
                        if expected.lower() == "pass":
                            self.logger.info(f"Login passed as expected with username: {username}")
                            lp.clickLogout()
                            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                            self.driver.switch_to.alert.accept()
                            lst_status.append("pass")
                        else:
                            self.logger.warning(f"Unexpected login success with username: {username}")
                            lst_status.append("fail")
                    else:
                        self.logger.warning("Page title mismatch")
                        lst_status.append("fail")


        except Exception as e:
            self.logger.error(f"Database connection failed: {str(e)}")
            assert False

        self.driver.close()

        if 'fail' not in lst_status:
            self.logger.info("DDT Login Test Passed")
            assert True
        else:
            self.logger.error("DDT Login Test Failed")
            assert False
