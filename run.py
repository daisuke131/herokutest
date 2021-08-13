from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
        #読み込み先URL
        driver.get('https://www.google.com/')
        #読み込んだHTML内から取得するテキストのID属性を指定
        driver.quit()
        print("成功")
    except Exception:
        print("失敗")


if __name__ == '__main__':
    main()