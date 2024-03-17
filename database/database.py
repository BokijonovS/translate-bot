import sqlite3

class DataBase:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = sqlite3.connect(self.path_to_db)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data


    def create_table_users(self):
        sql = '''create table if not exists users(
        telegram_id integer primary key,
        full_name varchar(50),
        phone_number varchar(13)
        )'''
        self.execute(sql, commit=True)

    def insert_telegram_id(self, telegram_id):
        sql = '''insert into users(telegram_id) values(?) on conflict do nothing'''
        self.execute(sql, parameters=(telegram_id,), commit=True)

    def check_user(self, telegram_id):
        sql = '''select full_name, phone_number from users where telegram_id = ?'''

        return self.execute(sql, parameters=(telegram_id,), fetchone=True)

    def update_user(self, full_name, phone_number, telegram_id):
        sql = '''update users set full_name = ? , phone_number = ? where telegram_id = ?'''
        self.execute(sql, parameters=(full_name, phone_number, telegram_id), commit=True)