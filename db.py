import sqlite3

# TODO Add ID functionality
class Database():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def create_table(self, name: str, fields: dict[str, str]):
        string_fields: str = 'id integer primary key autoincrement, '
        
        for item in fields.items():
            string_fields += item[0] + " " + item[1] + ", "
        string_fields = string_fields[:len(string_fields) - 2]

        self.cursor.execute(f'create table if not exists {name} ({string_fields})')
        self.conn.commit()

    def drop_table(self, name: str):
        self.cursor.execute(f'drop table if exists {name}')
        self.conn.commit()

    def get_data_from_table(self, table_name: str):
        self.cursor.execute(f'select * from {table_name}')
        data = self.cursor.fetchall()
        self.conn.commit()
        return data

    def get_fields(self, name: str):
        self.cursor.execute(f'select * from {name}')
        return [description[0] for description in self.cursor.description]

    def insert_data_into_table(self, name: str, data: dict[str, str]):
        keys = [k for k in data]

        data_items = " "
        data_keys = " "
        for key in keys:
            data_items += "'" + data[key] + "'" + ", "
            data_keys += "'" + key + "'" + ", "
        data_items = data_items[:len(data_items) - 2]
        data_keys = data_keys[:len(data_keys) - 2]

        self.cursor.execute(f'insert into {name} ({data_keys}) values ({data_items})')
        self.conn.commit()

    def delete_data_from_table(self, name: str, data: dict[str, str]):
        pass

    def alter_data_from_table(self, name: str, old: int, new: dict[str, str]):
        pass

    def __sql(self, command):
        self.cursor.execute(command)
        self.conn.commit()

    def close(self):
        self.conn.close()


