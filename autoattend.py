from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options


class AutoAttend:

    def login(url, id, password, driverpath):

        driver = webdriver.Chrome(executable_path=('./' + driverpath))
        driver.get(url)
        time.sleep(2)
        action = driver.find_element_by_name('user_id')
        action.send_keys(id)
        time.sleep(1)
        action = driver.find_element_by_name('password')
        action.send_keys(password)
        time.sleep(1)
        action = driver.find_element_by_id('entry-login')
        action.click()
        time.sleep(1)
        print("""\nAttention: Go to any class and allow the mic and camera then press any key in the cmd
                    then close the class tab and return to the home page \n""")
        input("")
        return driver

    def attending(driver, index_of_url, index_of_button, end_hour):
        time.sleep(2)
        url = driver.find_element_by_xpath(
            '//*[@id="_3_1termCourses_noterm"]/ul')
        action = url.find_elements_by_tag_name("li")
        action[index_of_url].find_elements_by_tag_name("a")[0].click()
        time.sleep(6)
        driver.switch_to.frame('collabUltraLtiFrame')
        time.sleep(2)
        if(0 == index_of_button):
            button = driver.find_element_by_xpath(
                '//*[@id="main-content"]/div[1]/div')
            action = button.find_elements_by_tag_name("button")
            action[0].click()
        else:
            expand = driver.find_elements_by_xpath(
                '//*[@id="body-content"]/div[3]//*[@aria-expanded="false"]')
            for e in expand:
                e.click()
            button = driver.find_element_by_xpath(
                '//*[@id="body-content"]/div[3]')
            action = button.find_elements_by_tag_name("button")
            action[index_of_button - 1].click()
        time.sleep(2)
        action = driver.find_element_by_xpath(
            '//*[@id="offcanvas-wrap"]/div[2]/div/div/div/div/div[2]/div/bb-loading-button/button')
        action.click()
        print("Parent window title: " + driver.title)
        time.sleep(2)
        # get current window handle
        p = driver.current_window_handle
        # get first child window
        attend = driver.window_handles[1]
        while True:
            time.sleep(45)
            if(datetime.now().hour == end_hour):
                driver.switch_to.window(window_name=attend)
                driver.close()
                break
        driver.switch_to.window(window_name=driver.window_handles[0])
        driver.find_element_by_link_text('Home').click()
        time.sleep(3)

    def keep_alive(driver, hour):
        while True:
            print("""im working ^_^ on keep the website alive!
                  you can go to sleep now
                  GoodNight!.. ugh its daytime I mean sleep well !""")
            driver.find_element_by_link_text('Home').click()
            if(datetime.now().hour == (hour + 1)):
                break
            time.sleep(60)
