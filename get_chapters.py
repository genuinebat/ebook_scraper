from seleniumbase import SB
from selenium.webdriver.common.by import By
from time import sleep

URL = "https://lightnovelpub.vip/novel/the-beginning-after-the-end-548/chapter-" 

text_files_dir = "./text_files/"

START_CHAP = int(input("Enter starting chapter: "))
CHAP_NUM = int(input("Number of chapters to scrape: "))

for i in range(CHAP_NUM):
    curr_chap = START_CHAP + i
    with SB(uc=True) as driver:
        driver.uc_open_with_reconnect(URL + str(curr_chap))
        try:
            driver.assert_element('img[alt="Logo Assembly"]', timeout=4)
            driver.sleep(3)
        except Exception:
            if driver.is_element_visible('input[value*="Verify"]'):
                driver.uc_click('input[value*="Verify"]')
            else:
                driver.uc_gui_click_captcha()

        sleep(2) 

        src = driver.find_element(By.ID, "chapter-container").text

        file_name = "Chapter " + str(curr_chap) + ".txt"
        
        with open(text_files_dir + file_name, "w", encoding="utf-8") as f:
            f.write(src)
            f.close()