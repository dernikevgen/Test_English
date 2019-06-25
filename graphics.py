import sys
from random import shuffle
from PyQt5.QtCore import QBasicTimer, QSize
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QBrush, QPainter, QColor, QImage, QPalette
from PyQt5.QtCore import Qt
from class_method import ConnectDB


class Base(QMainWindow, ConnectDB):

    def __init__(self):

        super().__init__()
        self.key_db = 0
        self.true_input = 0
        self.max_val = ConnectDB.len_table(self, 'verbs_form')
        self.value_list = [i for i in range(1, self.max_val+1)]
        shuffle(self.value_list)
        self.setWindowTitle('Тестирование знаний')
        self.setFixedSize(910, 600)
        self.center()
        self.general_window()

    def general_window(self):
        '''
        Creating menus, basic widgets,
        buttons and labels
        '''
        menubar = self.menuBar()
        opt_ns_Menu = menubar.addMenu('&Опции')
        self.get_Action = QAction('&Начать', self)
        self.get_Action.setShortcut('Ctrl+r')
        exit_Action = QAction('&Выход', self)
        exit_Action.setShortcut('Ctrl+Q')
        self.get_Action.triggered.connect(self.start_program)
        exit_Action.triggered.connect(self.close)
        opt_ns_Menu.addAction(self.get_Action)
        opt_ns_Menu.addAction(exit_Action)

        try_Menu = menubar.addMenu('&Учебник')
        try_Action = QAction('&Правила к заданиям', self)
        try_Menu.addAction(try_Action)

        dop_Menu = menubar.addMenu('&Дополнительно')
        to_addAction_1 = QAction('&О разработчиках', self)
        to_addAction_1.triggered.connect(self.info)
        to_addAction_2 = QAction('&Почему Паланик?', self)
        to_addAction_1.triggered.connect(self.info)
        to_addAction_2.triggered.connect(self.button_palanuk)
        dop_Menu.addAction(to_addAction_1)
        dop_Menu.addAction(to_addAction_2)

        self.setStatusTip('Строка состояния')
        self.get_Action.setStatusTip('Начать тест')
        exit_Action.setStatusTip('Выход из программы')
        try_Action.setStatusTip('Необходимый атрибут')
        to_addAction_1.setStatusTip('Важная информация')
        to_addAction_2.setStatusTip('Причём тут Чак Паланик?')
        '''
        Window space
        '''
        back_map = QImage("image_back2.jpg")
        back_map_2 = back_map.scaled(QSize(450, 300))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(back_map_2))
        self.setPalette(palette)

        cb = QCheckBox('Поставь галочку', self)
        cb.move(60, 100)
        cb.adjustSize()
        cb.stateChanged.connect(self.change_title)

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
        self.line_1 = QLabel(self)
        self.line_1.move(153, 149)
        self.line_1_2 = QLabel(self)
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

        pix_map = QPixmap("images.jpeg")
        img = QLabel(self)
        img.setPixmap(pix_map)
        img.setGeometry(60, 270, 225, 225)
        lbl_img = QLabel('Это - Чак Паланик', self)
        lbl_img.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        lbl_img.adjustSize()
        lbl_img.move(60, 520)
        img.setStatusTip('Чак Паланик')

        self.choice_verbs()
        self.lbl_limit = QLabel(f'{self.key_db} / {self.max_val}', self)
        self.lbl_limit.setFont(QtGui.QFont('Times', 24, QtGui.QFont.Bold))
        self.lbl_limit.adjustSize()
        self.lbl_limit.move(410, 290)
        self.lbl_lim_set_stat = QLabel('Cтaрт: Ctrl+r', self)
        self.lbl_lim_set_stat.setFont(QtGui.QFont
                                      ('Times', 12, QtGui.QFont.Bold))
        self.lbl_lim_set_stat.adjustSize()
        self.lbl_lim_set_stat.move(380, 370)

        self.true_limit = QLabel('Правильных ответов:', self)
        self.true_limit.setFont(QtGui.QFont('Times', 14, QtGui.QFont.Bold))
        self.true_limit.adjustSize()
        self.true_limit.move(620, 280)
        self.true_limit_2 = QLabel(f'{self.true_input} из'
                                   f' {self.max_val * 3}', self)
        self.true_limit_2.setFont(QtGui.QFont
                                  ('Times', 14, QtGui.QFont.Bold))
        self.true_limit_2.adjustSize()
        self.true_limit_2.move(700, 320)

        self.btn_assert = QPushButton('Проверить', self)
        self.btn_assert.resize(self.btn_assert.sizeHint())
        self.btn_assert.clicked.connect(self.show_verbs)
        self.btn_assert.setGeometry(350, 440, 200, 25)
        self.btn_assert.blockSignals(True)

        lbl_assert = QLabel('Если вы не заполнили пропуски,\n'
                            'то при нажатии этой клавиши\n'
                            'вы не сможете записать ответ.', self)
        lbl_assert.adjustSize()
        lbl_assert.move(350, 480)

        self.btn_next = QPushButton('Далее', self)
        self.btn_next.resize(self.btn_assert.sizeHint())
        self.btn_next.setFocus()
        self.btn_next.setAutoDefault(True)
        self.btn_next.clicked.connect(self.check_input)
        self.btn_next.setGeometry(650, 440, 200, 25)
        self.btn_next.blockSignals(True)
        self.lbl_next = QLabel(self)
        self.lbl_next.move(730, 480)

        self.show()

    def draw_lines(self, qp):
        '''
        Paint displays
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

    def start_program(self):
        '''Start program'''
        self.choice_verbs()
        self.line_1.setText(self.one)
        self.line_1_2.setText(self.one)
        self.lbl_lim_set_stat.setText('Cтепень выполнения')
        self.lbl_lim_set_stat.adjustSize()
        self.lbl_lim_set_stat.move(350, 370)
        self.btn_assert.blockSignals(False)
        self.btn_next.blockSignals(False)
        self.insert_empty_str()

    def choice_verbs(self):
        '''
        Choise value from db
        '''
        self.one = ConnectDB.select_table(self,
                                          'one_form',
                                          'verbs_form',
                                          self.value_list[self.key_db])
        self.two = ConnectDB.select_table(self,
                                          'two_form',
                                          'verbs_form',
                                          self.value_list[self.key_db])
        self.three = ConnectDB.select_table(self,
                                            'three_form',
                                            'verbs_form',
                                            self.value_list[self.key_db])
        self.trans = ConnectDB.select_table(self,
                                            'translate',
                                            'verbs_form',
                                            self.value_list[self.key_db])
        self.max_val = ConnectDB.len_table(self, 'verbs_form')

    def check_input(self):
        '''
        Check input values
        '''
        self.choice_verbs()
        input_2 = self.line_2.text().lower()
        input_3 = self.line_3.text().lower()
        input_t = self.line_t.text().lower()
        if input_2 == self.two:
            self.true_input += 1
        if input_3 == self.three:
            self.true_input += 1
        if input_t == self.trans:
            self.true_input += 1
        self.true_limit_2.setText(f'{self.true_input} из'
                                  f' {self.max_val * 3}')
        self.next_value()

    def show_verbs(self):
        '''
        Print true value in down display
        '''
        self.choice_verbs()
        self.line_2_2.setText(self.two)
        self.line_3_2.setText(self.three)
        self.line_t_2.setText(self.trans)
        self.lbl_next.setText('(Enter)')
        self.btn_next.setFocus()
        if len(self.line_2.text()) == 0:
            self.line_2.setMaxLength(0)
        else:
            self.line_2.setReadOnly(True)
            if self.line_2.text().lower() != self.two:
                self.line_2.setStyleSheet("color: red;")
            else:
                self.line_2.setStyleSheet("color: green;")

        if len(self.line_3.text()) == 0:
            self.line_3.setMaxLength(0)
        else:
            self.line_3.setReadOnly(True)
            if self.line_3.text().lower() != self.three:
                self.line_3.setStyleSheet("color: red;")
            else:
                self.line_3.setStyleSheet("color: green;")

        if len(self.line_t.text()) == 0:
            self.line_t.setMaxLength(0)
        else:
            self.line_t.setReadOnly(True)
            if self.line_t.text().lower() != self.trans:
                self.line_t.setStyleSheet("color: red;")
            else:
                self.line_t.setStyleSheet("color: green;")

    def insert_empty_str(self):
        '''
        Dont't repeat
        '''
        self.str_empty = ''
        self.line_2.setText(self.str_empty)
        self.line_3.setText(self.str_empty)
        self.line_t.setText(self.str_empty)
        self.line_2_2.setText(self.str_empty)
        self.line_3_2.setText(self.str_empty)
        self.line_t_2.setText(self.str_empty)

    def next_value(self):
        '''
        Next value and
        clear 'true values'
        '''
        if self.key_db == len(self.value_list)-1:
            self.show_verbs()
            self.btn_assert.disconnect()
            self.btn_next.disconnect()
            self.get_Action.disconnect()
            self.doAction()
            self.lbl_limit.setFont(QtGui.QFont
                                   ('Times', 16, QtGui.QFont.Bold))
            self.lbl_limit.setText(f'{self.true_input} /'
                                   f' {self.max_val * 3}')
            self.lbl_lim_set_stat.setText('Правильных ответов')
            self.true_limit.move(660, 280)
            self.true_limit.setText('Тест завершён')
            self.true_limit_2.setText('ctr + Q')
            self.lbl_next.setText(self.str_empty)
        else:
            self.key_db += 1
            self.choice_verbs()
            self.btn_next.setFocus()
            self.lbl_limit.setText(f'{self.key_db} /'
                                   f' {self.max_val}')
            self.line_1.setText(self.one)
            self.line_1_2.setText(self.one)
            self.line_2.setReadOnly(False)
            self.line_3.setReadOnly(False)
            self.line_t.setReadOnly(False)
            self.insert_empty_str()
            self.lbl_next.setText(self.str_empty)
            self.line_2.setStyleSheet("color: black;")
            self.line_3.setStyleSheet("color: black;")
            self.line_t.setStyleSheet("color: black;")

    def info(self):
        '''
        info of PyQt developers
        '''
        QMessageBox.aboutQt(self)

    def button_palanuk(self):
        '''
        Info for smail
        '''
        win_palanuk = QWidget(self, Qt.Window)
        win_palanuk.setWindowModality(Qt.WindowModal)
        win_palanuk.setFixedSize(600, 600)
        win_palanuk.move(
            QApplication.desktop().screen().rect().center() - win_palanuk.rect().center()
        )
        win_palanuk.show()
        back_map = QImage("images.jpeg")
        back_map_2 = back_map.scaled(QSize(600, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(back_map_2))
        win_palanuk.setPalette(palette)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Галочку сними')
        else:
            self.setWindowTitle('Тестирование знаний')

    def timerEvent(self, e):
        '''
        For statusbar
        '''
        if self.step >= 100:
            self.timer.stop()
            return

        self.step = self.step + 25
        self.pbar.setValue(self.step)

    def doAction(self):
        '''
        Start statusbar
        '''

        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)

    def paintEvent(self, e):
        '''
        Paint display
        '''
        qp = QPainter()
        qp.begin(self)
        self.draw_lines(qp)
        qp.end()

    def closeEvent(self, event):
        '''
        Try / except on quit
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

