import sys
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QBrush, QPainter, QColor
from PyQt5.QtCore import Qt
from class_method import ConnectDB


class Base(QMainWindow, ConnectDB):

    def __init__(self):

        super().__init__()
        self.key_db = 1
        self.true_input = 0
        self.setWindowTitle('Тестирование знаний')
        self.setFixedSize(910, 600)
        self.general_window()
        self.center()

    def general_window(self):
        '''
        Создание меню, основных виджетов,
        кнопок и надписей
        '''
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
        self.one = ConnectDB.select_table(self, 'one_form', 'verbs_form', self.key_db)
        self.line_1 = QLabel(self.one, self)
        self.line_1.move(153, 149)
        self.line_1_2 = QLabel(self.one, self)
        self.line_1_2.move(153, 198)

        btn_2 = QLabel('Вторая ->', self)
        btn_2.move(260, 150)
        self.line_2 = QLineEdit(self)
        self.line_2.setMaxLength(14)
        self.line_2.move(350, 150)
        self.line_2_2 = QLabel(self)
        self.line_2_2.move(353, 198)

        btn_3 = QLabel('Третья ->', self)
        btn_3.move(460, 150)
        self.line_3 = QLineEdit(self)
        self.line_3.setMaxLength(14)
        self.line_3.move(550, 150)
        self.line_3_2 = QLabel(self)
        self.line_3_2.move(553, 198)

        btn_t = QLabel('Перевод ->', self)
        btn_t.move(655, 150)
        self.line_t = QLineEdit(self)
        self.line_t.setMaxLength(14)
        self.line_t.setFixedSize(110, 30)
        self.line_t.move(750, 150)

        self.line_t_2 = QLabel(self)
        self.line_t_2.move(753, 198)

        self.pix_map = QPixmap("images.jpeg")
        img = QLabel(self)
        img.setPixmap(self.pix_map)
        img.setGeometry(60, 270, 225, 225)
        lbl_img = QLabel('Это - Чак Паланик', self)
        lbl_img.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        lbl_img.adjustSize()
        lbl_img.move(60, 520)
        img.setStatusTip('Чак Паланик')

        self.max_val = ConnectDB.len_table(self, 'verbs_form')
        self.lbl_limit = QLabel(f'{self.key_db} / {self.max_val}', self)
        self.lbl_limit.setFont(QtGui.QFont('Times', 24, QtGui.QFont.Bold))
        self.lbl_limit.adjustSize()
        self.lbl_limit.move(410, 290)

        lbl_lim_set_stat = QLabel('Cтепень выполнения', self)
        lbl_lim_set_stat.setFont(QtGui.QFont('Times', 12, QtGui.QFont.Bold))
        lbl_lim_set_stat.adjustSize()
        lbl_lim_set_stat.move(350, 370)

        self.true_limit = QLabel('Правильных ответов:', self)
        self.true_limit.setFont(QtGui.QFont('Times', 14, QtGui.QFont.Bold))
        self.true_limit.adjustSize()
        self.true_limit.move(620, 280)
        self.true_limit_2 = QLabel(f'{self.true_input} из {self.max_val * 3}', self)
        self.true_limit_2.setFont(QtGui.QFont('Times', 14, QtGui.QFont.Bold))
        self.true_limit_2.adjustSize()
        self.true_limit_2.move(700, 320)


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
        btn_next.clicked.connect(self.check_input)
        btn_next.setGeometry(650, 440, 200, 25)

        self.show()

    def draw_lines(self, qp):
        '''
        Отрисовка дисплеев
        '''
        brush = QBrush(Qt.SolidPattern)
        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(QColor('white'))
        '''Окно лимита'''
        qp.drawRect(350, 270, 200, 80)
        qp.drawRect(374, 285, 150, 50)
        '''Первая'''
        qp.drawRect(150, 152, 100, 25)
        qp.drawRect(150, 200, 100, 25)
        '''Вторая'''
        qp.drawRect(350, 200, 100, 25)
        '''Третья'''
        qp.drawRect(550, 200, 100, 25)
        '''Перевод'''
        qp.drawRect(750, 200, 110, 25)

    def check_input(self):
        '''
        Проверка введённых значений
        '''
        input_2 = self.line_2.text()
        input_3 = self.line_3.text()
        input_t = self.line_t.text()
        two = ConnectDB.select_table(self, 'two_form', 'verbs_form', self.key_db)
        three = ConnectDB.select_table(self, 'three_form', 'verbs_form', self.key_db)
        trans = ConnectDB.select_table(self, 'translate', 'verbs_form', self.key_db)
        if input_2 == two:
            self.true_input += 1
        if input_3 == three:
            self.true_input += 1
        if input_t == trans:
            self.true_input += 1
        self.true_limit_2.setText(f'{self.true_input} из {self.max_val * 3}')
        self.next_value()

    def show_verbs(self):
        '''
        Вывод правильных значений в нижние табло
        '''
        self.doAction()
        two = ConnectDB.select_table(self, 'two_form', 'verbs_form', self.key_db)
        three = ConnectDB.select_table(self, 'three_form', 'verbs_form', self.key_db)
        trans = ConnectDB.select_table(self, 'translate', 'verbs_form', self.key_db)
        self.line_2_2.setText(two)
        self.line_3_2.setText(three)
        self.line_t_2.setText(trans)
        fixed_2 = self.line_2.text()
        fixed_3 = self.line_3.text()
        fixed_t = self.line_t.text()
        print(len(fixed_2), len(fixed_3), len(fixed_t))
        if len(fixed_2) == 0:
            self.line_2.setMaxLength(0)
        else:
            self.line_2.setReadOnly(True)
        if len(fixed_3) == 0:
            self.line_3.setMaxLength(0)
        else:
            self.line_3.setReadOnly(True)
        if len(fixed_t) == 0:
            self.line_t.setMaxLength(0)
        else:
            self.line_t.setReadOnly(True)

    def next_value(self):
        '''
        Следующее значение
        и обнуление подсказок
        '''
        str_empty = ''
        if self.key_db >= self.max_val:
            sys.exit(app.exec_())
        else:
            self.key_db += 1
            self.max_val = ConnectDB.len_table(self, 'verbs_form')
            self.one = ConnectDB.select_table(self, 'one_form', 'verbs_form', self.key_db)
            self.lbl_limit.setText(f'{self.key_db} / {self.max_val}')
            self.line_1.setText(self.one)
            self.line_1_2.setText(self.one)
            self.line_2.setReadOnly(False)
            self.line_3.setReadOnly(False)
            self.line_t.setReadOnly(False)
            self.line_2.setText(str_empty)
            self.line_3.setText(str_empty)
            self.line_t.setText(str_empty)
            self.line_2_2.setText(str_empty)
            self.line_3_2.setText(str_empty)
            self.line_t_2.setText(str_empty)
            self.line_2.setMaxLength(14)
            self.line_3.setMaxLength(14)
            self.line_t.setMaxLength(14)

    def center(self):
        '''
        Центрирование окна
        на запускаемом устройстве
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def change_title(self, state):
        '''
        Изменение названия окна
        '''
        if state == Qt.Checked:
            self.setWindowTitle('Галочку сними')
        else:
            self.setWindowTitle('Тестирование знаний')

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

    def paintEvent(self, e):
        '''
        Для отрисовки дисплея
        '''
        qp = QPainter()
        qp.begin(self)
        self.draw_lines(qp)
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

