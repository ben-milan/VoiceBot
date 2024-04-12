from selenium import webdriver
import time

def main():
    driver = webdriver.Chrome()

    time.sleep(2)

    url = driver.current_url
    print(url)



if __name__ == "__main__":
    main()