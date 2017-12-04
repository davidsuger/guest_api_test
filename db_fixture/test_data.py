import sys
from db_fixture.sqlite_db import DB

datas = {
    'sign_event': [
        {'id': 1, 'name': '红米1', '`limit`': 100, 'status': 1, 'address': '北京', 'start_time': '2017-09-01 00:12:32',
         'create_time': '2017-08-01 00:23:45'},
        {'id': 2, 'name': '红米2', '`limit`': 200, 'status': 0, 'address': '上海', 'start_time': '2017-09-02 00:12:32',
         'create_time': '2017-08-02 00:23:45'},
        {'id': 3, 'name': '红米3', '`limit`': 300, 'status': 1, 'address': '广州', 'start_time': '2017-09-03 00:12:32',
         'create_time': '2017-08-03 00:23:45'},
        {'id': 4, 'name': '红米4', '`limit`': 400, 'status': 1, 'address': '北京', 'start_time': '2017-09-04 00:12:32',
         'create_time': '2017-08-04 00:23:45'},
        {'id': 5, 'name': '红米5', '`limit`': 500, 'status': 1, 'address': '北京', 'start_time': '2017-09-05 00:12:32',
         'create_time': '2017-08-05 00:23:45'},
    ],
    'sign_guest': [
        {'id': 1, 'realname': 'alen', 'phone': 1324567154, 'email': 'alen@163.com', 'sign': 0, 'event_id': 1,
         'create_time': '2017-08-01 00:23:45'},
        {'id': 2, 'realname': 'david', 'phone': 13810960310, 'email': 'david@163.com', 'sign': 0, 'event_id': 1,
         'create_time': '2017-08-02 00:23:45'},
        {'id': 3, 'realname': 'jack', 'phone': 135485612, 'email': 'jack@163.com', 'sign': 0, 'event_id': 3,
         'create_time': '2017-08-03 00:23:45'},
        {'id': 4, 'realname': 'tom', 'phone': 133455498, 'email': 'tom@163.com', 'sign': 0, 'event_id': 4,
         'create_time': '2017-08-04 00:23:45'},
        {'id': 5, 'realname': 'helen', 'phone': 1394513123, 'email': 'helen@163.com', 'sign': 0, 'event_id': 5,
         'create_time': '2017-08-05 00:23:45'},
    ],
}


def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()
