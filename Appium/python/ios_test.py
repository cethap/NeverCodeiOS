import os
import unittest

from appium import webdriver


class iOSTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '10.2'
        desired_caps['deviceName'] = 'Apple iPhone 6s Plus'
        desired_caps['app'] = os.path.join(os.environ.get("GREENHOUSE_SYMROOT"),
                                           "Debug-iphoneos/testMasterDetail.app")
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertTrue(False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(iOSTests)
    unittest.TextTestRunner(verbosity=3).run(suite)