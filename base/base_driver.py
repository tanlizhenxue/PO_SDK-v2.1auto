from appium import webdriver


def init_driver(no_reset=True):
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = '192.168.206.101:5555'
    # 要启动的app信息
    desired_caps['appPackage'] = 'com.android.gallery3d'
    desired_caps['appActivity'] = 'com.android.gallery3d.app.GalleryActivity'
    # True:不重置应用 False:重置应用
    desired_caps['noReset'] = no_reset
    # 使输入中文有效
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 获取toast
    desired_caps['automationName'] = 'Uiautomator2'

    # 连接appium服务器
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
