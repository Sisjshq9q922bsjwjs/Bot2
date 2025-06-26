from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from threading import Thread
from keep_alive import keep_alive

# ===========================
# 🔧 Configuration
# ===========================
FAKE_USERNAME = "anushkax.journal"
FAKE_PASSWORD = "Anu@2025Journal"
TARGET_USERNAME = "samxforreal"

# ===========================
# 🚀 Chrome Options
# ===========================
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# ===========================
# 🔁 Automation Function
# ===========================
def automate_followers():
    driver = webdriver.Chrome(options=options)

    def login_fastfollow():
        try:
            driver.get("https://fastfollow.in")
            time.sleep(2)
            driver.find_element(By.ID, "loginAsUser").click()
            time.sleep(2)
            driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(FAKE_USERNAME)
            driver.find_element(By.NAME, "password").send_keys(FAKE_PASSWORD)
            driver.find_element(By.ID, "login_insta").click()
            time.sleep(5)
            driver.switch_to.default_content()

            send_follower = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/tools/send-follower']"))
            )
            driver.execute_script("arguments[0].click();", send_follower)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            ).send_keys(TARGET_USERNAME)

            driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()
            time.sleep(4)

            adet_input = driver.find_element(By.NAME, "adet")
            adet_input.clear()
            adet_input.send_keys("500000")

            submit_btn = driver.find_element(By.ID, "formTakipSubmitButton")
            driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
            driver.execute_script("arguments[0].click();", submit_btn)
            time.sleep(50)
            print("\u2705 fastfollow.in: Followers sent")
        except Exception as e:
            print("\u274c fastfollow.in: Error \u2192", str(e))

    def login_takipcikrali():
        try:
            driver.get("https://takipcikrali.com/login")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            ).send_keys(FAKE_USERNAME)

            driver.find_element(By.NAME, "password").send_keys(FAKE_PASSWORD)
            driver.find_element(By.ID, "login_insta").click()
            time.sleep(4)

            send_follower = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/tools/send-follower']"))
            )
            driver.execute_script("arguments[0].click();", send_follower)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            ).send_keys(TARGET_USERNAME)

            driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()
            time.sleep(3)

            adet_input = driver.find_element(By.NAME, "adet")
            adet_input.clear()
            adet_input.send_keys("500000")

            driver.find_element(By.ID, "formTakipSubmitButton").click()
            time.sleep(50)
            print("\u2705 takipcikrali.com: Followers sent")
        except Exception as e:
            print("\u274c takipcikrali.com: Error \u2192", str(e))

    def login_takipcigir():
        try:
            driver.get("https://takipcigir.com/login")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(FAKE_USERNAME)
            driver.find_element(By.NAME, "password").send_keys(FAKE_PASSWORD)
            driver.find_element(By.ID, "login_insta").click()
            time.sleep(5)

            send_follower = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/tools/send-follower']"))
            )
            driver.execute_script("arguments[0].click();", send_follower)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(TARGET_USERNAME)
            driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()
            time.sleep(3)

            adet_input = driver.find_element(By.NAME, "adet")
            adet_input.clear()
            adet_input.send_keys("500000")

            driver.find_element(By.ID, "formTakipSubmitButton").click()
            time.sleep(50)
            print("\u2705 takipcigir.com: Followers sent")
        except Exception as e:
            print("\u274c takipcigir.com: Error \u2192", str(e))

    def login_takipcimx():
        try:
            driver.get("https://takipcimx.net/login")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(FAKE_USERNAME)
            driver.find_element(By.NAME, "password").send_keys(FAKE_PASSWORD)
            driver.find_element(By.ID, "login_insta").click()
            time.sleep(5)

            send_follower = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/tools/send-follower']"))
            )
            driver.execute_script("arguments[0].click();", send_follower)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(TARGET_USERNAME)
            driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()
            time.sleep(3)

            adet_input = driver.find_element(By.NAME, "adet")
            adet_input.clear()
            adet_input.send_keys("500000")

            driver.find_element(By.ID, "formTakipSubmitButton").click()
            time.sleep(50)
            print("\u2705 takipcimx.net: Followers sent")
        except Exception as e:
            print("\u274c takipcimx.net: Error \u2192", str(e))

    login_fastfollow()
    login_takipcikrali()
    login_takipcigir()
    login_takipcimx()
    driver.quit()

# ===========================
# 📅 Background Loop
# ===========================
def main_loop():
    for i in range(30):
        print(f"\n\ud83d\udd01 Cycle {i+1}/30 Started")
        automate_followers()
        if i < 29:
            print("\u23f3 Sleeping for 20 minutes...\n")
            time.sleep(1200)

keep_alive()
Thread(target=main_loop).start()
