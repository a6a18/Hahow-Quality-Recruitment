import pytest
import allure
from selenium import webdriver
from time import sleep
import csv
import requests

class TestCase_UI():
    # 答案
    A1 = []
    A2 = []
    A3 = []

    def setup_class(self):
        # 開啟瀏覽器
        self.driver = webdriver.Chrome('C:/Users/a6a18/Desktop/allure-docker-python-pytest-example/tests/chromedriver.exe')
        self.driver.maximize_window()


    @allure.epic('UI')
    @allure.feature('此專案裡有幾個合作者，並且分別列出他們的名字')
    def test_contributors(self):
        self.driver.get('https://github.com/hahow/hahow-recruit')
        sleep(5)
        self.driver.find_element_by_css_selector('#repo-content-pjax-container > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(5) > div > h2 > a').click()
        sleep(5)
        contributors_box = self.driver.find_element_by_css_selector('#contributors > ol')
        contributors = contributors_box.find_elements_by_tag_name("li")

        for i in contributors:
            contributor = i.find_element_by_css_selector("h3 > a.text-normal").text
            TestCase_UI.A1.append(contributor)
            print(contributor)


    @allure.epic('UI')
    @allure.feature('請進入到 frontend.md 並且查看 "Wireframe" 的圖片是否存在')
    def test_wireframe(self):
        self.driver.get('https://github.com/hahow/hahow-recruit/blob/master/frontend.md')
        sleep(5)
        readme = self.driver.find_elements_by_css_selector('#readme')
        Wireframe_images_url = []

        # 取得專案文章中的圖片連結
        for elem in readme:
            images = elem.find_elements_by_tag_name('img')

            for image in images:
                Wireframe_images_url.append(image.get_attribute('src'))

        # 藉由請求圖片判斷是否存在：status_code = 200 表示存在，其他則表示不存在。
        for i in Wireframe_images_url:
            res = requests.get(i)
            
            if res.status_code == 200:
                TestCase_UI.A2.append('pass')
                print('圖片存在')
            else:
                TestCase_UI.A2.append(f'圖片不存在：{i}')
                print(f'圖片不存在：{i}')


    @allure.epic('UI')
    @allure.feature('最後一個 commit 的人是誰')
    def test_last_commit(self):
        self.driver.get('https://github.com/hahow/hahow-recruit')
        sleep(5)
        last_contributor_box = self.driver.find_element_by_css_selector('#repo-content-pjax-container > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.Box.mb-3 > div.Box-header.position-relative > div > div.flex-1.d-flex.flex-items-center.ml-3.min-width-0 > div.css-truncate.css-truncate-overflow.color-fg-muted > a')


        last_contributor = last_contributor_box.text
        TestCase_UI.A3.append(last_contributor)
        print(last_contributor)
    

    def teardown_class(self):
        # 關閉瀏覽器
        self.driver.quit()

        # 寫入文件答案
        with open('UI_Answer.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['問題', '答案'])

            writer.writerow(['此專案裡有幾個合作者，並且分別列出他們的名字', TestCase_UI.A1])
            writer.writerow(['請進入到 frontend.md 並且查看 "Wireframe" 的圖片是否存在', TestCase_UI.A2])
            writer.writerow(['最後一個 commit 的人是誰', TestCase_UI.A3])


# if __name__ == '__main__':
#     pytest.main()