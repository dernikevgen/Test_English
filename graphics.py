from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QBrush, QPainter, QColor
from PyQt5.QtCore import Qt
from class_method import ConnectDB, MethodFunc
import sys

i = 2


class Base(QMainWindow, ConnectDB, MethodFunc):

    def __init__(self):
        '''
        Основные параметры окна
        '''
        super().__init__()
        ConnectDB.__init__(self)
        MethodFunc.__init__(self)
        self.setWindowTitle('Тестирование знаний')
        self.setFixedSize(900, 600)
        self.general_window()
        self.center()

    def general_window(self):
        '''
        Создание меню, основных виджетов,
        кнопок и надписей
        '''
        global i

        cb = QCheckBox('Поставь галку', self)
        cb.move(60, 100)
        cb.adjustSize()
        cb.stateChanged.connect(self.change_title)

        menubar = self.menuBar()
        opt_ns_Menu = menubar.addMenu('&Опции')
        get_Action = QAction('&Начать', self)
        get_Action.setShortcut('Ctrl+r')
        get_Action.triggered.connect(self.doAction)
        opt_ns_Menu.addAction(get_Action)
        exit_Action = QAction('&Выход', self)
        exit_Action.setShortcut('Ctrl+Q')
        exit_Action.triggered.connect(self.close)
        opt_ns_Menu.addAction(exit_Action)

        try_Menu = menubar.addMenu('&Попытки')
        try_Action = QAction('&Статистика', self)
        try_Menu.addAction(try_Action)

        dop_Menu = menubar.addMenu('&Дополнительно')
        to_addAction = QAction('&О разработчика', self)
        to_addAction.triggered.connect(self.info)
        dop_Menu.addAction(to_addAction)

        self.setStatusTip('Строка состояния')
        get_Action.setStatusTip('Начать тест')
        exit_Action.setStatusTip('Выход из программы')
        try_Action.setStatusTip('Предыдущие попытки')
        to_addAction.setStatusTip('Важная информация')
        '''
        Пространство окна
        '''
        lbl_1 = QLabel('Заполните пробелы нужной формой глагола', self)
        lbl_1.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        lbl_1.adjustSize()
        lbl_1.move(200, 50)

        self.textEdit = QTextEdit()
        self.statusBar()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(350, 100, 200, 25)

        self.timer = QBasicTimer()
        self.step = 0

        btn_1 = QLabel('Первая ->', self)
        btn_1.move(60, 148)
        self.one = ConnectDB.select_table(self, 'one_form', 'verbs_form', i)
        self.line_1 = QLabel(self.one, self)
        self.line_1.move(153, 149)
        self.line_1_2 = QLabel(self.one, self)
        self.line_1_2.move(153, 198)

        btn_2 = QLabel('Вторая ->', self)
        btn_2.move(260, 150)
        self.line_2 = QLineEdit(self)
        self.line_2.setMaxLength(10)
        self.line_2.move(350, 150)

        self.line_2_2 = QLabel(self)
        self.line_2_2.move(353, 198)

        btn_3 = QLabel('Третья ->', self)
        btn_3.move(460, 150)
        self.line_3 = QLineEdit(self)
        self.line_3.setMaxLength(10)
        self.line_3.move(550, 150)

        self.line_3_2 = QLabel(self)
        self.line_3_2.move(553, 198)

        btn_t = QLabel('Перевод ->', self)
        btn_t.move(650, 150)
        self.line_t = QLineEdit(self)
        self.line_t.setMaxLength(10)
        self.line_t.move(750, 150)
        self.line_t_2 = QLabel(self)
        self.line_t_2.move(753, 198)

        pix_map = QPixmap("images.jpeg")
        img = QLabel(self)
        img.setPixmap(pix_map)
        img.setGeometry(60, 270, 225, 225)
        lbl_img = QLabel('Это - Чак Паланик', self)
        lbl_img.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        lbl_img.adjustSize()
        lbl_img.move(60, 520)
        img.setStatusTip('Чак Паланик')

        self.max_val = ConnectDB.len_table(self, 'verbs_form')
        lbl_limit = QLabel(f'{i} / {self.max_val}', self)
        lbl_limit.setFont(QtGui.QFont('Times', 24, QtGui.QFont.Bold))
        lbl_limit.adjustSize()
        lbl_limit.move(560, 290)

        lbl_lim_setStat = QLabel('Cтепень выполнения', self)
        lbl_lim_setStat.setFont(QtGui.QFont('Times', 12, QtGui.QFont.Bold))
        lbl_lim_setStat.adjustSize()
        lbl_lim_setStat.move(500, 370)

        btn_assert = QPushButton('Проверить', self)
        btn_assert.resize(btn_assert.sizeHint())
        btn_assert.clicked.connect(self.show_verbs)
        btn_assert.setGeometry(350, 440, 200, 25)

        lbl_assert = QLabel('Если вы не заполнили пропуски,\n'
                            'то при нажатии этой клавиши\n'
                            'вы не сможете записать ответ.', self)
        lbl_assert.adjustSize()
        lbl_assert.move(350, 480)

        btn_next = QPushButton('Далее', self)
        btn_next.resize(btn_assert.sizeHint())
        btn_next.clicked.connect(self.next_value)
        btn_next.setGeometry(650, 440, 200, 25)

        self.show()

    def draw_Lines(self, qp):
        '''
        Отрисовка дисплеев
        '''
        brush = QBrush(Qt.SolidPattern)
        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(QColor('white'))
        '''Окно лимита'''
        qp.drawRect(500, 270, 200, 80)
        qp.drawRect(524, 285, 150, 50)
        '''Первая'''
        qp.drawRect(150, 152, 100, 25)
        qp.drawRect(150, 200, 100, 25)
        '''Вторая'''
        qp.drawRect(350, 200, 100, 25)
        '''Третья'''
        qp.drawRect(550, 200, 100, 25)
        '''Перевод'''
        qp.drawRect(750, 200, 100, 25)

    def change_title(self, state):
        '''
        Изменение названия окна
        '''
        if state == Qt.Checked:
            self.setWindowTitle('Галочку сними')
        else:
            self.setWindowTitle('Проверка знаний')

    def timerEvent(self, e):
        '''
        переопределение метода
        для обработки события
        '''
        if self.step >= 100:
            self.timer.stop()
            return

        self.step = self.step + 25
        self.pbar.setValue(self.step)

    def doAction(self):
        '''
        Запуск и установка таймера
        '''

        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)

    def printer_func(self):
        '''
        Перебор элементов по id
        '''
        self.max_val = ConnectDB.len_table(self, 'verbs_form')
        val_list = [j for j in range(1, self.max_val)]

    def show_verbs(self):
        '''
        Вывод правильных значений в нижние табло
        '''
        self.doAction()
        self.two = ConnectDB.select_table(self, 'two_form', 'verbs_form', i)
        self.three = ConnectDB.select_table(self, 'three_form', 'verbs_form', i)
        self.trans = ConnectDB.select_table(self, 'translate', 'verbs_form', i)
        self.line_2_2.setText(self.two)
        self.line_3_2.setText(self.three)
        self.line_t_2.setText(self.trans)
        self.line_2.setMaxLength(0)
        self.line_3.setMaxLength(0)
        self.line_t.setMaxLength(0)

    def next_value(self):
        '''
        Следующее значение
        и обнуление подсказок
        '''
        self.str_empty = ''
        self.line_2_2.setText(self.str_empty)
        self.line_3_2.setText(self.str_empty)
        self.line_t_2.setText(self.str_empty)
        self.line_2.setMaxLength(10)
        self.line_3.setMaxLength(10)
        self.line_t.setMaxLength(10)

    def center(self):
        '''
        Центрирование окна
        на запускаемом устройстве
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, e):
        '''
        Для отрисовки дисплея
        '''
        qp = QPainter()
        qp.begin(self)
        self.draw_Lines(qp)
        qp.end()

    def info(self):
        '''
        Вывод информации о разработчиках
        '''
        pass

    def closeEvent(self, event):
        '''
        Бокс для отлова случайного выхода
        '''
        reply = QMessageBox.question(self, 'Попытка выхода',
                                     "Вы действительно хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Base()
    sys.exit(app.exec_())

