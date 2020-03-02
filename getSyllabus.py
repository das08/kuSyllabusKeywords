import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

options = Options()
# ヘッドレスモードで実行する場合
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


def getSyllabus(i, url):
    driver.get(url)
    time.sleep(2)

    lectureName = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/div[2]/div/div/div/h2")

    semester = driver.find_element_by_xpath(
        "/html/body/div[1]/table/tbody/tr/td[2]/div[2]/div/div/div/table/tbody/tr[2]/td[2]")

    teacherName = driver.find_element_by_xpath(
        "/html/body/div[1]/table/tbody/tr/td[2]/div[2]/div/div/div/table/tbody/tr[8]/td[2]/ul/li")

    overview = driver.find_element_by_xpath(
        "/html/body/div[1]/table/tbody/tr/td[2]/div[2]/div/div/div/table/tbody/tr[9]/td[2]")
    goal = driver.find_element_by_xpath(
        "/html/body/div[1]/table/tbody/tr/td[2]/div[2]/div/div/div/table/tbody/tr[10]/td[2]")
    plan = driver.find_element_by_xpath(
        "/html/body/div[1]/table/tbody/tr/td[2]/div[2]/div/div/div/table/tbody/tr[11]/td[2]")

    savetxt = lectureName.text + "\n" + teacherName.text + "\n" + semester.text + "\n" + overview.text + goal.text + plan.text

    file = open(f'./syllabus/{i}-{url[-7:]}.txt', 'w')
    file.write(savetxt)
    file.close()


def getAllLec():
    for i in range(1, 80):
        try:
            driver.get(f"https://ocw.kyoto-u.ac.jp/syllabuses2019/la/{i}")
            time.sleep(2)

            getList = driver.find_elements_by_class_name("course-title")
            tmpList = []
            for _ in getList:
                tmpList.append(_.find_element_by_tag_name('a').get_attribute('href'))

            for url in tmpList:
                getSyllabus(i, url)
                print(i, url)
        except:
            continue


getAllLec()
