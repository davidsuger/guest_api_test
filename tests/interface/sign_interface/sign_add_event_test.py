import requests, time, hashlib, unittest


class AddEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_add_event/"
        # api_key
        self.api_key = '&Guest-Bugmaster'
        # 当前时间
        now_time = time.time()
        self.client_time = str(now_time).split('.')[0]
        # sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_request_error(self):
        r=requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'request error')


    # def test_add_event_all_null(self):
    #     payload = {'eid': '', '': '', 'limit': '', 'address': '', 'start_time': ''}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'], 10021)
    #     self.assertEqual(self.result['message'], 'parameter error')
    #
    # def test_add_event_eid_exist(self):
    #     payload = {'eid': 1, 'name': 'IphoneX', 'limit': 200, 'address': 'beijing', 'start_time': '2017-09-04 00:12:32'}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'], 10022)
    #     self.assertEqual(self.result['message'], 'event id already exists')
    #
    # def test_add_event_name_exist(self):
    #     payload = {'eid': 6, 'name': '红米1', 'limit': 200, 'address': 'beijing', 'start_time': '2017-09-04 00:12:32'}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'], 10023)
    #     self.assertEqual(self.result['message'], 'event name already exists')
    #
    # def test_add_event_data_type_error(self):
    #     payload = {'eid': 7, 'name': '红米7', 'limit': 200, 'address': 'beijing', 'start_time': '2017-09'}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'], 100241)
    #     self.assertIn('start_time format error', self.result['message'])
    #
    # def test_add_event_success(self):
    #     payload = {'eid': 8, 'name': '红米8', 'limit': 200, 'address': 'beijing', 'start_time': '2017-09-08 00:12:32'}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'], 200)
    #     self.assertEqual(self.result['message'], 'add event success')
