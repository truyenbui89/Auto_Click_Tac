from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver as sw_driver
import time
import requests
import random

# Cấu hình proxy và thông tin đăng nhập
proxies = [
    {
        "proxy": "svhn12.proxyno1.com:55653",
        "username": "truyen",
        "password": "truyen",
        "api": "https://app.proxyno1.com/api/change-key-ip/RW8Djr9cDwK981mNz3bEVf1721271399"
    },
    # Thêm nhiều proxy khác tại đây
]

def setup_chrome_with_proxy(proxy_info):
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    selenium_wire_options = {
        'proxy': {
            'http': f'http://{proxy_info["username"]}:{proxy_info["password"]}@{proxy_info["proxy"]}',
            'https': f'https://{proxy_info["username"]}:{proxy_info["password"]}@{proxy_info["proxy"]}',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    driver = sw_driver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options,
        seleniumwire_options=selenium_wire_options
    )
    return driver

def change_ip(proxy_info):
    try:
        response = requests.get(proxy_info["api"])
        if response.status_code == 200:
            print("IP đã được thay đổi thành công.")
            new_ip = response.json().get('ip')  # Giả sử API trả về IP mới trong response
            print(f"IP mới: {new_ip}")
        else:
            print(f"Không thể thay đổi IP. Mã lỗi: {response.status_code}")
    except Exception as e:
        print(f"Lỗi khi thay đổi IP: {e}")

def auto_scroll_and_click(driver):
    try:
        body = driver.find_element(By.TAG_NAME, 'body')
        
        # Cuộn xuống
        for _ in range(2):
            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(random.uniform(0.5, 1))  # Thời gian chờ ngẫu nhiên
        
        # Cuộn lên
        for _ in range(2):
            driver.execute_script("window.scrollBy(0, -window.innerHeight);")
            time.sleep(random.uniform(0.5, 1))  # Thời gian chờ ngẫu nhiên
        
        # Nhấp vào một liên kết ngẫu nhiên
        links = driver.find_elements(By.TAG_NAME, 'a')
        if links:
            random_link = random.choice(links)
            driver.execute_script("arguments[0].scrollIntoView();", random_link)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(random_link))
            random_link.click()
            time.sleep(3)  # Đợi 3 giây sau khi nhấp vào liên kết
    except Exception as e:
        print(f"Lỗi trong khi auto-scroll và click: {e}")

def search_and_click(keywords_domains, num_clicks, proxies):
    proxy_index = 0
    click_count = 0
    keyword_index = 0
    num_keywords = len(keywords_domains)

    while click_count < num_clicks:
        proxy_info = proxies[proxy_index]
        driver = setup_chrome_with_proxy(proxy_info)

        keyword, domain = list(keywords_domains.items())[keyword_index]
        
        try:
            driver.get('https://www.google.com')
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)
            
            time.sleep(random.uniform(1, 2))  # Đợi kết quả tìm kiếm tải
            
            found = False
            while not found:
                # Tìm kiếm các thẻ chứa kết quả
                results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
                for result in results:
                    try:
                        # Kiểm tra nếu nội dung của thẻ chứa domain
                        link = result.find_element(By.TAG_NAME, 'a')
                        href = link.get_attribute('href')
                        if domain in href:
                            # Cuộn tới vị trí của thẻ nếu cần
                            driver.execute_script("arguments[0].scrollIntoView();", result)
                            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(link))
                            link.click()  # Nhấp vào liên kết chứa domain
                            found = True
                            break
                    except Exception as e:
                        print(f"Lỗi khi kiểm tra kết quả tìm kiếm: {e}")
                
                if not found:
                    # Nếu không tìm thấy, cuộn xuống trang và tiếp tục tìm kiếm
                    driver.execute_script("window.scrollBy(0, window.innerHeight);")
                    time.sleep(random.uniform(0.5, 1))  # Thời gian chờ ngẫu nhiên

                if driver.execute_script("return window.scrollY") == 0:
                    # Nếu không tìm thấy và không thể cuộn thêm, thoát ra vòng lặp
                    break
            
            if found:
                time.sleep(1)  # Đợi 1 giây để chắc chắn trang đã tải xong
                auto_scroll_and_click(driver)
                time.sleep(3)  # Đợi 3 giây để các hành động trên trang có thể thực hiện xong
                click_count += 1
            else:
                print(f"Không tìm thấy domain: {domain} cho từ khóa: {keyword}")
            
            driver.quit()  # Tắt cửa sổ trình duyệt
            
            if click_count >= num_clicks:
                break
            
            change_ip(proxy_info)  # Thay đổi IP
            proxy_index = (proxy_index + 1) % len(proxies)  # Chuyển sang proxy tiếp theo
            keyword_index = (keyword_index + 1) % num_keywords  # Chuyển sang từ khóa tiếp theo
            
        except Exception as e:
            print(f"Lỗi: {e}")
            driver.quit()

if __name__ == "__main__":
    keywords_domains = {}
    num_keywords = int(input("Nhập số lượng từ khóa và domain: "))
    for _ in range(num_keywords):
        keyword = input("Nhập từ khóa tìm kiếm: ")
        domain = input("Nhập domain cần tìm kiếm (bao gồm https:// hoặc http://): ")
        keywords_domains[keyword] = domain

    while True:
        try:
            num_clicks = int(input("Nhập số lượt click: "))
            break
        except ValueError:
            print("Số lượt click phải là một số nguyên.")

    search_and_click(keywords_domains, num_clicks, proxies)
