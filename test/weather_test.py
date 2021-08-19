import allure

from unittest import TestCase
from ..library.httpclient import HttpClient

@allure.feature('Test Weather api')
class Weather(TestCase):
    """Weather api test cases"""

    def setUp(self):
        """Setup of the test"""

        self.host = ' http://d1.weather.com.cn '
        self.ep_path = '/sk_2d'
        self.client = HttpClient()

    @allure.story('Test of BeiJing')
    def test_1_BJ(self):
        city_code = '101010100.html?_=1629300463809'
        exp_city = '北京'
        self._test(city_code,exp_city)

    @allure.story('Test of ShenZhen')
    def test_2_SZ(self):
        city_code = '101280601.html?_=1629214546735'
        exp_city = '深圳'
        self._test(city_code,exp_city)

    @allure.story('Test of WuHan')
    def test_3_WH(self):
        city_code = '101200101.html?_=1629301259059'
        exp_city = '武汉'
        self._test(city_code,exp_city)

    def _test(self,city_code,exp_city):
        url = f'{self.host}{self.ep_path}/{city_code}'
        response = self.client.Get(url=url)
        act_city = response.json()['var dataSK']['cityname']
        print(f'Expect city = {exp_city} , while actual city = {act_city}')
        self.assertEqual(exp_city, act_city,f'Expect city = {exp_city}, while actual city = {act_city}')