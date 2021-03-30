import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class JitSuSkip:
    def __init__(self):
        self.file_open()

    def start_browser(self):
        chrome_options = Options()
        user_path = f'./Browser_profile'
        chrome_options.add_argument(f'user-data-dir={user_path}')

        try:
            self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')
        except:
            return False
        return True

    def file_open(self):
        with open('last_url.txt', 'r') as f:
            self.link = f.read()

    def file_write(self, link):
        with open('last_url.txt', 'w') as f:
            f.write(link)

    def wait_opening_skiper(self):
        while True:
            try:
                self.driver.find_element_by_css_selector(
                    '[class="vjs-overlay vjs-overlay-bottom-left vjs-overlay-skip-intro vjs-overlay-background"]').click()
                break
            except:
                time.sleep(1)

    def wait_ending_skiper(self):
        while True:
            try:
                self.driver.find_element_by_css_selector(
                    '[class="vjs-overlay vjs-overlay-bottom-right vjs-overlay-skip-intro vjs-overlay-background"]').click()
                break
            except:
                time.sleep(1)

    def wait_new_page(self):
        while True:
            if self.driver.current_url == self.link:
                time.sleep(.1)
                continue
            self.link = self.driver.current_url
            self.file_write(self.link)
            break

    def start_new_part_and_full_screen(self):
        while True:
            try:
                self.driver.find_element_by_css_selector('[class="vjs-big-play-button"]').click()
                break
            except:
                time.sleep(.1)
        while True:
            try:
                self.driver.find_element_by_css_selector(
                    '[class="vjs-fullscreen-control vjs-control vjs-button"]').click()
                break
            except:
                time.sleep(.1)

    def run(self):
        self.start_browser()
        self.driver.get(self.link)
        self.start_new_part_and_full_screen()
        while True:
            self.wait_opening_skiper()
            self.wait_ending_skiper()
            self.wait_new_page()
            self.start_new_part_and_full_screen()

# пропуск опенинга 'class="vjs-overlay vjs-overlay-bottom-left vjs-overlay-skip-intro vjs-overlay-background"'
# переключение серии 'class="vjs-overlay vjs-overlay-bottom-right vjs-overlay-skip-intro vjs-overlay-background"'
# Кнопка плей 'class="vjs-big-play-button"'
# Кнопка fullscreen 'class="vjs-fullscreen-control vjs-control vjs-button"'

if __name__ == '__main__':
    pr = JitSuSkip()
    pr.run()