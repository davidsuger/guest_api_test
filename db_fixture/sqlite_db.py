import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('C:/Users/Quan/PycharmProjects/guest/db.test.sqlite3')
        self.cursor = self.conn.cursor()

    def clear(self, table_name):
        real_sql = 'delete from ' + table_name + ";"

        self.cursor.execute(real_sql)
        self.conn.commit()

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = 'INSERT INTO ' + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        self.cursor.execute(real_sql)
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    table_name = 'sign_event'
    data = {'id': 1, 'name': '红米', '`limit`': 500, 'status': 1, 'address': '北京', 'start_time': '2017-09-23 00:12:32','create_time':'2017-08-05 00:23:45'}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
