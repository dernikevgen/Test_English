import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor


class ConnectDB:
    def select_table(self, column_name, table_name, id):
        '''
        Сonnect to database
        '''
        with closing(psycopg2.connect(dbname='verbs',
                                      user='postgres',
                                      password='654123',
                                      host='localhost')) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute("SELECT {} FROM {} WHERE id={}".format(
                    column_name,
                    table_name,
                    id)
                )
                res = cursor.fetchone()
                return "".join(res)

    def len_table(self, table_name):
        '''
        Get len table
        '''
        with closing(psycopg2.connect(dbname='verbs',
                                      user='postgres',
                                      password='654123',
                                      host='localhost')) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT max(id) FROM {table_name}")
                res = cursor.fetchone()
                return int(''.join(map(str, res)))

    def insert_table(self, table_name, v1, v2, v3, vt):
        '''
        Insert values in table
        '''
        with closing(psycopg2.connect(dbname='verbs',
                                      user='postgres',
                                      password='654123',
                                      host='localhost')) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO {table_name}"
                               f" (one_form, two_form, three_form, translate)"
                               f" VALUES ('{v1}','{v2}','{v3}','{vt}')")
                conn.commit()

    def delete_val_table(self, table_name, id):
        '''
        Delete values form table
        '''
        with closing(psycopg2.connect(dbname='verbs',
                                      user='postgres',
                                      password='654123',
                                      host='localhost')) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table_name} WHERE id={id}")
                conn.commit()

