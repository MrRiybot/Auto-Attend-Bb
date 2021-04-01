from autoattend import AutoAttend as AA
from datetime import datetime
import time
print(" _   _          _____ _                 _                                                     __")
print("| \ | |        / ____| |               | |                                                _  \\ \\")
print("|  \| | ___   | |    | | __ _ ___ ___  | |_ ___  _ __ ___   ___  _ __ _ __ _____      __ (_)  | |")
print("| . ` |/ _ \  | |    | |/ _` / __/ __| | __/ _ \| '_ ` _ \ / _ \| '__| '__/ _ \ \ /\ / /      | |")
print("| |\  | (_) | | |____| | (_| \__ \__ \ | || (_) | | | | | | (_) | |  | | | (_) \ V  V /   _   | |")
print("|_| \_|\___/   \_____|_|\__,_|___/___/  \__\___/|_| |_| |_|\___/|_|  |_|  \___/ \_/\_/   (_)  | |")
print("   from MrRiybot by Selenium                                                                   /_/ ")
driverpath = input(
    "Enter your driverpath (must be in the same folder) example 'Chromedriver.exe': ")
url = input("copy the url of your LMS(BlackBoard) and enter it here: ")
login = input("your id or username: ")
password = input("your password: ")
driver = AA.login(url, login, password, driverpath)

index = int(input("how many classes do you have tommorow ?: "))
first_hour = int(input("what hour does your first class begin ?: "))
last_hour = int((input("what hour does your last class finish ?: ")))

list_hour_of_class = list()
list_index_of_url = list()
list_index_of_button = list()
list_end_time = list()

for i in range(1, index + 1):
    url_list = driver.find_element_by_xpath(
        '//*[@id="_3_1termCourses_noterm"]/ul')
    action = url_list.find_elements_by_tag_name("li")
    for i, c in enumerate(action):
        print(i, "- " + c.find_elements_by_tag_name("a")[0].text)
    index_url = input("choose your class from these numbers: ")
    list_index_of_url.append(int(index_url))
    url = action[int(index_url)].find_elements_by_tag_name("a")[0]
    name = url.text
    url.click()
    time.sleep(6)
    driver.switch_to.frame('collabUltraLtiFrame')
    time.sleep(2)
    button_list = driver.find_element_by_xpath(
        '//*[@id="main-content"]/div[1]/div')
    action = button_list.find_elements_by_tag_name("button")
    print("0- " + action[0].text)
    expand = driver.find_elements_by_xpath(
        '//*[@id="body-content"]/div[3]//*[@aria-expanded="false"]')
    for e in expand:
        e.click()
    button_list = driver.find_element_by_xpath(
        '//*[@id="body-content"]/div[3]')
    action = button_list.find_elements_by_tag_name("button")
    for i, c in enumerate(action):
        print((i + 1), "- " + c.text)
    button = input("which one is the name of your class session: ")
    list_index_of_button.append(int(button))
    hour = input("what hour does your class (" + name + ") begin?: ")
    list_hour_of_class.append(int(hour))
    end_time = input("what hour does your class end?: ")
    list_end_time.append(int(end_time))
    print("perfect!")
    print("---------------------------------------------------")
    driver.switch_to.default_content()
    driver.find_element_by_link_text('Home').click()
    time.sleep(3)

count = 0
while True:
    if(datetime.now().hour == list_hour_of_class[count]):
        AA.attending(
            driver, list_index_of_url[count], list_index_of_button[count], list_end_time[count])
        count += 1
    else:
        AA.keep_alive(driver, datetime.now().hour)
    if(datetime.now().hour == last_hour):
        break
