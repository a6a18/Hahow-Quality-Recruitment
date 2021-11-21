# Hahow Quality Recruitment

Hahow測試工程師徵才小專案

基於pytest與allure的測試框架。


## 🧰 安裝

- Python 3 環境
https://www.python.org/downloads/

- docker 軟體
https://www.docker.com/get-started

- Chrome WebDriver
https://chromedriver.chromium.org/downloads (下載對應chrome的webdriver版本，並且放置於/tests目錄底下)

## 🛸 執行

- 確保 localhost:5050、localhost:5252 port 並未被占用。

```bash
git clone https://github.com/a6a18/Hahow-Quality-Recruitment.git
cd Hahow-Quality-Recruitment
pip3 install -r requirements.txt    # 下載相關套件
docker-compose up -d allure allure-ui    # 啟動docker環境
python3 run.py    # 執行測試
```

可以到這裡查看最新的測試報告：

http://localhost:5050/allure-docker-service/latest-report


## 🏸 專案資訊

- **UI Test**: [Selenium]
- **API Test**: [Requests]
- **Language**: Python 3.9.7
- **Coding Style**: [PEP8]
- **Test Framework**: [allure-pytest]


## 🗺️ 專案架構

```bash
.
├── allure-reports/             # allure測試報告
├── allure-results/             # allure測試結果
├── img/                        
├── tests/ 
│  ├── condition
│  │  └── api_conditon.py       # API測試的參考資料                     
│  ├── api_test.py              # API測試
│  ├── ui_test.py               # UI測試
│  └── chromedriver.exe         # WebDriver
├── .gitattributes
├── .gitignore
├── API_Answer.csv              # API問題的答案
├── docker-compose.yml          # dockerfile
├── README.md
├── requirements.txt
├── run.py                      # 執行程式
└── UI_Answer.csv               # UI問題的答案     
```


## 🐸 專案講解：

藉由docker建立allure測試報告環境<br>

![docker畫面](https://github.com/a6a18/Hahow-Quality-Recruitment/blob/main/img/docker%E7%95%AB%E9%9D%A2.png)<br><br>

docker環境讀取專案內allure-reports和allure-results的檔案並呈現測試報告於

http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html?redirect=false <br>

![Allure報告視窗](https://github.com/a6a18/Hahow-Quality-Recruitment/blob/main/img/Allure報告視窗.png)<br><br>

測試案例呈現<br>

![Testcase](https://github.com/a6a18/Hahow-Quality-Recruitment/blob/main/img/Testcase.png)<br><br>

可至 http://localhost:5252/allure-docker-service-ui/projects/default 查看測試管理介面 <br>

![測試管理](https://github.com/a6a18/Hahow-Quality-Recruitment/blob/main/img/測試管理.png)<br><br>


[Selenium]: https://www.selenium.dev/
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[Requests]: https://docs.python-requests.org/en/latest/
[Pytest]: https://docs.pytest.org/en/6.2.x/
[allure-pytest]: https://docs.qameta.io/allure-report/frameworks/python/pytest