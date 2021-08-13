from concurrent.futures import ThreadPoolExecutor

from common.driver import Driver


def main():
    with ThreadPoolExecutor() as executor:
        for i in range(10):
            executor.submit(driver_dr, i)


def driver_dr(i):
    dr = Driver()
    dr.get("https://www.amazon.co.jp/")
    dr.quit()
    print(f"{i+1}回目成功")


if __name__ == "__main__":
    main()
