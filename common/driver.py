from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.util import fetch_user_agent


class Driver:
    def __init__(self):
        self.driver = self.driver_setting()

    def driver_setting(self):
        user_agent_random = fetch_user_agent()
        # ドライバーの読み込み
        options = Options()

        # ヘッドレスモードの設定
        # if os.name == "posix" or headless_flg:  # Linux　➙　本番環境のためHeadless
        options.add_argument("--headless")

        # options.add_argument("--user-agent=" + user_agent)
        options.add_argument("--user-agent=" + user_agent_random)
        # self.options.add_argument('log-level=3')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--incognito")  # シークレットモードの設定を付与
        options.add_argument("disable-infobars")  # AmazonLinux用
        # options.add_argument("--start-maximized")  # 画面最大化
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("log-level=3")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-desktop-notifications")
        options.add_argument("--disable-application-cache")
        options.add_argument("--lang=ja")

        try:
            driver = webdriver.Chrome(options=options)
            return driver
        except Exception:
            print("ドライバーの読み込みに失敗")
            return None

    def get(self, url: str):
        self.driver.get(url)

    def el_selector(self, s: str):
        return self.driver.find_element_by_css_selector(s)

    def els_selector(self, s: str):
        return self.driver.find_elements_by_css_selector(s)

    def el_id(self, s: str):
        return self.driver.find_element_by_id(s)

    def els_id(self, s: str):
        return self.driver.find_elements_by_id(s)

    def el_class(self, s: str):
        return self.driver.find_element_by_class_name(s)

    def els_class(self, s: str):
        return self.driver.find_elements_by_class_name(s)

    def el_xpath(self, s: str):
        return self.driver.find_element_by_xpath(s)

    def els_xpath(self, s: str):
        return self.driver.find_elements_by_xpath(s)

    def script_click(self, s: str):
        return self.driver.execute_script(f"document.querySelector({s}).click()")

    def quit(self):
        return self.driver.quit()
