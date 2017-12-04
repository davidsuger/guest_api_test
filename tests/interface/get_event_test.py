import requests
import unittest


class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/get_event_list/'

    def test_get_event_null(self):
        r = requests.get(self.url, params={'eid': ''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_error(self):
        r=requests.get(self.url,params={'eid':999})
        result=r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'query result is empty')

    def test_get_event_success(self):
        r=requests.get(self.url,params={'eid':1})
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')
        self.assertEqual(result['data']['name'],'红米1')
        self.assertEqual(result['data']['address'],'北京')
        self.assertEqual(result['data']['start_time'],'2017-09-01T00:12:32Z')

if __name__=='__main__':
    unittest.main()
