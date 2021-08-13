from common.driver import Driver


def main():
    dr = Driver()
    dr.get("https://www.amazon.co.jp/")
    dr.quit()
    print("class成功")


if __name__ == "__main__":
    main()
