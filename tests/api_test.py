import pytest
import allure
import requests
from condition.api_condition import *
import csv

class TestCase_API():
    # 答案
    A1 = []
    A2 = []
    A3 = []

    def setup_class(self):
        pass

    @allure.epic('API')
    @allure.feature('有多少不同種族的人出現在第六部？')
    @pytest.mark.parametrize('exc', Q1exc)
    def test_howMany_species(self, exc):
        res = requests.get('https://swapi.dev/api/films/').json()
        result = None

        for i in res['results']:
            if i['episode_id'] == 6:
                result = len(i['species'])

        TestCase_API.A1.append(result)
        print(result)
        assert result == exc


    @allure.epic('API')
    @allure.feature('請依據電影集數去排序電影名字？')
    @pytest.mark.parametrize('exc', Q2exc)
    def test_sort_films(self, exc):
        res = requests.get('https://swapi.dev/api/films/').json()
        result = None

        film_list = {}

        for i in res['results']:
            film_list[i['episode_id']] = i['title']

        result = sorted(film_list.items(), key=lambda item: item[0])

        TestCase_API.A2.append(result)
        print(result)
        assert result == exc


    @allure.epic('API')
    @allure.feature('請幫我挑出電影裡所有的車輛，馬力超過１０００的。')
    @pytest.mark.parametrize('exc', Q3exc)
    def test_1000speed_Cars(self, exc):
        res = requests.get('https://swapi.dev/api/vehicles/').json()
        result = []

        for i in res['results']:
            if int(i['max_atmosphering_speed']) > 1000:
                result.append(i['name'])
                print(i['name'])
        
        result = sorted(result)
        TestCase_API.A3.append(result)
        assert sorted(result) == exc
    
    def teardown_class(self):
        with open('API_Answer.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['問題', '答案'])

            writer.writerow(['有多少不同種族的人出現在第六部？', TestCase_API.A1])
            writer.writerow(['請依據電影集數去排序電影名字？', TestCase_API.A2])
            writer.writerow(['請幫我挑出電影裡所有的車輛，馬力超過１０００的。', TestCase_API.A3])


# if __name__ == '__main__':
#     pytest.main()
