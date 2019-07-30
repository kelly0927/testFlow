from appium import webdriver


def init_driver():
    driver_configure = {"platformName": "Android", "platformVersion": "4.4.4", "deviceName": "8c34fd6796d5",
                        "appPackage": "com.android.contacts", "appActivity": ".activities.DialtactsActivity",
                        "unicodeKeyboard": True, "resetKeyboard": True}
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", driver_configure)
    return driver


if __name__ == '__main__':
    print(init_driver())
