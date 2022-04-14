import unittest
import re
import requests


class DummyApiTests(unittest.TestCase):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}

    def test_count_over_30(self):
        headers = self.headers
        r = requests.get('http://dummy.restapiexample.com/api/v1/employees', headers=headers)
        self.assertEqual(r.status_code, 200)
        response = r.text
        age_pattern = '"employee_age":([1-9][0-9][0-9]|[1-9][0-9]|[1-9])'
        age_list = re.findall(age_pattern, response)
        count = sum(int(age) > 30 for age in age_list)

    def test_add_employee(self):
        headers = self.headers
        employee = {"name": "Dan", "salary": "123", "age": "102"}
        r = requests.post('http://dummy.restapiexample.com/api/v1/create', data=employee, headers=headers)
        self.assertEqual(r.status_code, 200)

    if __name__ == '__main__':
        unittest.main(warnings='ignore')
