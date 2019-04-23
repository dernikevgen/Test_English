import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor
from PyQt5.QtCore import QBasicTimer, QDate
from PyQt5.QtWidgets import *
from message_box import *
from PyQt5.QtGui import QPixmap, QBrush, QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import sys


class ConnectDB:
    def select_table(self, column_name, table_name, id):
        '''
        Делаем запрос к базе данных
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
        Получение длинны таблицы
        дла корректного перебора элементов.
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
        Добавление значений в таблицу
        '''
        with closing(psycopg2.connect(dbname='verbs',
                                      user='postgres',
                                      password='654123',
                                      host='localhost')) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO {table_name} (one_form, two_form, three_form, translate)"
                               f" VALUES ('{v1}','{v2}','{v3}','{vt}')")
                conn.commit()

    def delete_val_table(self, table_name, id):
        '''
        Удаление элементов из таблицы
        '''
        with closing(psycopg2.connect(dbname='verbs',
                                      user='postgres',
                                      password='654123',
                                      host='localhost')) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table_name} WHERE id={id}")
                conn.commit()


class MethodFunc:

    pass



conn_db = ConnectDB()

len__tb = conn_db.len_table('verbs_form')
# for i in range(1, len__tb+1):
#     a = conn_db.select_table('one_form', 'verbs_form', i)
#     two = conn_db.select_table('two_form', 'verbs_form', i)
#     three = conn_db.select_table('three_form', 'verbs_form', i)
#     trans = conn_db.select_table('translate', 'verbs_form', i)
#     print(a)
#     answer2 = input('Введите вторую форму: ')
#     print('True' if answer2 == two else 'False')
#     print(two)
#     answer3 = input('Введите третью форму: ')
#     print('True' if answer3 == three else 'False')
#     print(three)
#     answer_t = input('Введите перевод: ')
#     print('True' if answer_t == trans else 'False')
#     print(answer_t)
