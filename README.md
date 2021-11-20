# Hahow Quality Recruitment

Hahow測試工程師徵才小專案

基於pytest與allure的測試框架。


## 🧰 安裝

- Python 3 環境
https://www.python.org/downloads/

- docker 軟體
https://www.docker.com/get-started

- Chrome WebDriver
https://chromedriver.chromium.org/downloads (下載對應chrome的版本)

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
├── tests/                      
│  ├── api_test.py              # API測試
│  ├── ui_test.py               # UI測試
│  ├── chromedriver.exe         # WebDriver
│  ├── condition
│  │  └── api_conditon.py       # API測試的參考資料
├── allure-reports/             # allure測試報告
├── allure-results/             # allure測試結果
├── README.md
├── API_Answer.csv              # API問題的答案
├── UI_Answer.csv               # UI問題的答案
├── requirements.txt
├── docker-compose.yml
└── run.py                      # 執行程式
```


## 專案講解：

藉由docker建立allure測試報告環境<br>

![docker畫面](https://github.com/a6a18/Hahow-Quality-Recruitment/blob/main/img/docker%E7%95%AB%E9%9D%A2.png)<br><br>


[Selenium]: https://www.selenium.dev/
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[Requests]: https://docs.python-requests.org/en/latest/
[Pytest]: https://docs.pytest.org/en/6.2.x/
[allure-pytest]: https://docs.qameta.io/allure-report/frameworks/python/pytest