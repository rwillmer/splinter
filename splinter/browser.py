from splinter.driver.webdriver import WebDriver
from splinter.driver.chrome import WebDriver as ChromeWebDriver
from splinter.driver.zopetestbrowser import ZopeTestBrowser

_DRIVERS = {'webdriver': WebDriver,
            'zope.testbrowser': ZopeTestBrowser,
            'chrome': ChromeWebDriver}


def Browser(driver_name='webdriver'):
    driver = _DRIVERS[driver_name]
    return driver()