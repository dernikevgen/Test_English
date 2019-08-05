import sys
from random import shuffle
from PyQt5.QtCore import QBasicTimer, QSize, QUrl
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QBrush, QPainter, QColor, QImage, QPalette
from PyQt5.QtCore import Qt
from connect_api import ConnectDjangoApi


class Base(QMainWindow, ConnectDjangoApi):

    def __init__(self):

        super().__init__()
        self.key_db = self.true_input = self.id = 0
        self.setWindowTitle('Тестирование знаний')
        self.setFixedSize(910, 600)
        self.center()
        self.general_window()

    def pre_start_program(self):

        self.value_list = ConnectDjangoApi.value_list(self)
        self.verbs_dict = ConnectDjangoApi.value_dict(self)
        self.max_flags = ConnectDjangoApi.count_input(self)
        self.max_val = len(self.value_list) // 4
        self.print_key = [i for i in range(1, len(self.value_list) + 1)]
        self.print_one_key = [i for i in range(1, len(self.value_list) + 1, 4)]
        shuffle(self.print_one_key)
        self.input_conteiner = {i: i for i in self.print_one_key}
        self.container = self.verbs_dict.copy()
        self.flag_back_btn_activate = False

    def general_window(self):
        '''
        Assert of Web-connection
        '''
        try:
            self.pre_start_program()
        except:
            self.message_box()
        '''
        Creating menu, basic widgets,
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
        try_Action.triggered.connect(self.buttom_browser)
        try_Menu.addAction(try_Action)

        dop_Menu = menubar.addMenu('&Дополнительно')
        to_addAction_1 = QAction('&О разработчиках', self)
        to_addAction_2 = QAction('&Почему Паланик?', self)
        info_PyQt5 = lambda: QMessageBox.aboutQt(self)
        to_addAction_1.triggered.connect(info_PyQt5)
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
        self.image_background(self, 450, 300,)
        back_map = QImage("image_back22.jpg")
        back_map_2 = back_map.scaled(QSize(450, 300))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(back_map_2))
        self.setPalette(palette)

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
        self.line_1.move(153, 151)
        self.line_1_2 = QLabel(self)
        self.line_1_2.move(153, 200)

        btn_2 = QLabel('Вторая ->', self)
        btn_2.move(260, 150)
        self.line_2 = QLineEdit(self)
        self.line_2.setMaxLength(14)
        self.line_2.setFixedSize(108, 33)
        self.line_2.move(350, 150)
        self.line_2_2 = QLabel(self)
        self.line_2_2.move(353, 200)

        btn_3 = QLabel('Третья ->', self)
        btn_3.move(460, 150)
        self.line_3 = QLineEdit(self)
        self.line_3.setMaxLength(14)
        self.line_3.setFixedSize(108, 33)
        self.line_3.move(540, 150)
        self.line_3_2 = QLabel(self)
        self.line_3_2.move(543, 200)

        btn_t = QLabel('Перевод ->', self)
        btn_t.move(655, 150)
        self.line_t = QLineEdit(self)
        self.line_t.setMaxLength(14)
        self.line_t.setFixedSize(108, 33)
        self.line_t.move(750, 150)
        self.line_t_2 = QLabel(self)
        self.line_t_2.move(753, 200)

        self.draw_fonts(self.line_1_2, self.line_1,
                        self.line_2, self.line_2_2,
                        self.line_3, self.line_3_2,
                        self.line_t, self.line_t_2,)

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
        self.lbl_limit = QLabel(self)
        self.lbl_limit.setFont(QtGui.QFont('Times', 20, QtGui.QFont.Bold))
        self.lbl_limit.move(400, 295)
        self.lbl_lim_set_stat = QLabel('Cтaрт: Ctrl+r', self)
        self.lbl_lim_set_stat.setFont(QtGui.QFont
                                      ('Times', 12, QtGui.QFont.Bold))
        self.lbl_lim_set_stat.adjustSize()
        self.lbl_lim_set_stat.move(380, 370)

        self.true_limit = QLabel('Правильных ответов:', self)
        self.true_limit.setFont(QtGui.QFont('Times', 14, QtGui.QFont.Bold))
        self.true_limit.adjustSize()
        self.true_limit.move(620, 280)
        self.true_limit_2 = QLabel(self)
        self.true_limit_2.setFont(QtGui.QFont
                                  ('Times', 18, QtGui.QFont.Bold))
        self.true_limit_2.adjustSize()
        self.true_limit_2.move(700, 320)

        self.btn_back = QPushButton('Назад', self)
        self.btn_back.resize(self.btn_back.sizeHint())
        self.btn_back.clicked.connect(self.back_value)
        self.btn_back.setGeometry(350, 440, 200, 25)
        self.btn_back.blockSignals(True)

        self.btn_assert = QPushButton('Проверить', self)
        self.btn_assert.resize(self.btn_assert.sizeHint())
        self.btn_assert.clicked.connect(self.show_verbs)
        self.btn_assert.setGeometry(490, 480, 200, 25)
        self.btn_assert.blockSignals(True)

        lbl_assert = QLabel('Если вы не заполнили пропуски,\n'
                            'то при нажатии этих клавиш\n'
                            'вы не сможете изменить ответ.', self)
        lbl_assert.adjustSize()
        lbl_assert.move(490, 510)

        self.btn_next = QPushButton('Далее', self)
        self.btn_next.resize(self.btn_assert.sizeHint())
        self.btn_next.setFocus()
        self.btn_next.setAutoDefault(True)
        self.btn_next.clicked.connect(self.next_value)
        self.btn_next.setGeometry(650, 440, 200, 25)
        self.btn_next.blockSignals(True)
        self.lbl_next = QLabel(self)
        self.lbl_next.move(730, 480)

        self.show()

    def draw_fonts(self, *args):
        '''
        Dont't repeat
        '''
        for i in args:
            i.setFont(QtGui.QFont
                      ('Arial', 13, QtGui.QFont.Light))

    def draw_lines(self, qp):
        '''
        Paint displays
        '''
        brush = QBrush(Qt.SolidPattern)
        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(QColor('white'))
        '''Окно лимита'''
        qp.drawRect(350, 270, 200, 80)
        '''Первая'''
        qp.drawRect(150, 152, 105, 30)
        qp.drawRect(150, 200, 105, 30)
        '''Вторая'''
        qp.drawRect(350, 200, 105, 30)
        '''Третья'''
        qp.drawRect(540, 200, 105, 30)
        '''Перевод'''
        qp.drawRect(750, 200, 105, 30)

    def image_background(self, windget, x, y, image="image_back22.jpg"):
        '''
        Don't repeat
        '''
        back_map = QImage(image)
        back_map_2 = back_map.scaled(QSize(x, y))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(back_map_2))
        windget.setPalette(palette)

    def message_box(self):
        '''
        Warning message of notConnection
        '''
        hello = QDialog(self)
        hello.setWindowTitle('Внимание')
        hello.setWindowModality(Qt.WindowModal)
        hello.setFixedSize(500, 200)
        lable_help = QLabel('Приложению необходим доступ в интернет', hello)
        lable_help.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        lable_help.move(50, 60)
        thanks = QPushButton('Хорошо, спасибо', hello)
        thanks.resize(thanks.sizeHint())
        thanks.adjustSize()
        thanks.setGeometry(150, 120, 200, 30)
        thanks.clicked.connect(hello.close)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        hello.exec()

    def start_program(self):
        '''
        Start program
        '''
        try:
            self.pre_start_program()
        except:
            self.message_box()
            sys.exit(app.exec_())
        self.key_db = self.true_input = self.id = self.step = 0
        for i in self.container:
            self.container[i] = 0
        for i in self.input_conteiner:
            self.input_conteiner[i] = []
        self.pbar.setValue(self.step)
        self.btn_assert.blockSignals(False)
        self.btn_next.blockSignals(False)
        self.btn_back.blockSignals(False)
        self.choice_verbs()
        self.line_1.setText(self.one)
        self.line_1_2.setText(self.one)
        self.line_2.setReadOnly(False)
        self.line_3.setReadOnly(False)
        self.line_t.setReadOnly(False)
        self.clear_widget()
        self.lbl_lim_set_stat.setText('Cтепень выполнения')
        self.true_limit.setText('Правильных ответов')
        self.true_limit_2.setText(f'{self.true_input} из'
                                  f' {self.max_flags}')
        self.lbl_limit.setText(f'{self.id+1} / {self.max_val}')
        self.true_limit.adjustSize()
        self.true_limit_2.adjustSize()
        self.lbl_lim_set_stat.adjustSize()
        self.true_limit.move(620, 280)
        self.lbl_lim_set_stat.move(350, 370)

    def choice_verbs(self):
        '''
        Choise value from db
        self.one - primary list[0](conditionally),
        two,three,trans - [1],[2],[3] etc..
        "self.repeat" - this helper variable
        '''
        self.repeat = self.print_one_key[self.key_db]
        self.one = self.verbs_dict[self.repeat]
        self.two = self.verbs_dict[self.repeat + 1]
        self.three = self.verbs_dict[self.repeat + 2]
        self.trans = self.verbs_dict[self.repeat + 3]

    def check_input(self):
        '''
        Check input text, and draw
        true-progress counter
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

    def color_windgets(self, line, verbs):
        '''
        Don't repeat,
        colorama for true/false askers
        '''
        if line.text().lower() != verbs:
            line.setStyleSheet("color: red;")
        else:
            line.setStyleSheet("color: green;")

    def show_verbs(self):
        '''
        Print true value in down display,
        and block signal for
        cheating prevention
        '''
        self.choice_verbs()
        self.lbl_next.setText('(Enter)')
        self.btn_next.setFocus()
        if len(self.line_2.text()) != 0:
            self.line_2.setReadOnly(True)
            self.line_2_2.setText(self.two)
            self.color_windgets(self.line_2, self.two)
        if len(self.line_3.text()) != 0:
            self.line_3.setReadOnly(True)
            self.line_3_2.setText(self.three)
            self.color_windgets(self.line_3, self.three)
        if len(self.line_t.text()) != 0:
            self.line_t.setReadOnly(True)
            self.line_t_2.setText(self.trans)
            self.color_windgets(self.line_t, self.trans)

    def clear_widget(self, flag=True):
        '''
        Clear of all widgets
        to default standart,
        with two branching.
        '''
        if flag == True:
            self.line_2.clear()
            self.line_3.clear()
            self.line_t.clear()
        self.line_2_2.clear()
        self.line_3_2.clear()
        self.line_t_2.clear()
        self.line_2.setStyleSheet("color: black;")
        self.line_3.setStyleSheet("color: black;")
        self.line_t.setStyleSheet("color: black;")

    def fragment_clear_windget(self):
        '''
        Fragmented clear and
        filling out widget
        '''
        v_two = self.container[self.repeat + 1]
        v_three = self.container[self.repeat + 2]
        v_trans = self.container[self.repeat + 3]
        self.line_2_2.clear()
        self.line_3_2.clear()
        self.line_t_2.clear()
        if v_two != 0:
            self.line_2.setText(v_two)
            self.line_2.setReadOnly(True)
        else:
            self.line_2.clear()
            self.line_2.setReadOnly(False)
        if v_three != 0:
            self.line_3.setText(v_three)
            self.line_3.setReadOnly(True)
        else:
            self.line_3.clear()
            self.line_3.setReadOnly(False)
        if v_trans != 0:
            self.line_t.setText(v_trans)
            self.line_t.setReadOnly(True)
        else:
            self.line_t.clear()
            self.line_3.setReadOnly(False)
        self.clear_widget(flag=False)

    def back_value(self):
        '''
        Draw previously entered values,
        calculate counter "progress bar"
        '''
        self.id -= 1
        if self.id < 0:
            self.id += 1
            self.btn_back.blockSignals(True)
            self.lbl_limit.setText(f'{self.id + 1} /'
                                   f' {self.max_val}')
            return
        self.key_db -= 1
        self.flag_back_btn_activate = True
        self.choice_verbs()
        self.line_1.setText(self.one)
        self.line_1_2.setText(self.one)
        if self.container[self.repeat + 1] != 0:
            self.line_2.setText(str(self.container[self.repeat + 1]))
            self.line_2.setReadOnly(True)
        if self.container[self.repeat + 2] != 0:
            self.line_3.setText(str(self.container[self.repeat + 2]))
            self.line_3.setReadOnly(True)
        if self.container[self.repeat + 3] != 0:
            self.line_t.setText(str(self.container[self.repeat + 3]))
            self.line_t.setReadOnly(True)
        self.lbl_limit.setText(f'{self.id + 1} /'
                               f' {self.max_val}')

    def mechanick_next(self):
        '''
        Function collections entered values
        in conteiner, changes counters.
        Checks widget fullness,
        if YES - draw corresponding values,
        if NO - clear all.
        '''
        self.container[self.repeat] = self.one
        if len(self.line_2.text()) != 0:
            self.container[self.repeat + 1] = str(self.line_2.text())
            self.input_conteiner[self.repeat].append('0')
        if len(self.line_3.text()) != 0:
            self.container[self.repeat + 2] = str(self.line_3.text())
            self.input_conteiner[self.repeat].append('0')
        if len(self.line_t.text()) != 0:
            self.container[self.repeat + 3] = str(self.line_t.text())
            self.input_conteiner[self.repeat].append('0')
        self.key_db += 1
        self.id += 1
        self.choice_verbs()
        self.btn_next.setFocus()
        self.lbl_limit.setText(f'{self.id + 1} /'
                               f' {self.max_val}')
        self.line_1.setText(self.one)
        self.line_1_2.setText(self.one)
        self.line_2.setReadOnly(False)
        self.line_3.setReadOnly(False)
        self.line_t.setReadOnly(False)
        self.btn_back.blockSignals(False)
        if len(self.input_conteiner[self.print_one_key[self.key_db - 1]]) != 0:
            self.fragment_clear_windget()
        else:
            self.clear_widget()
        self.lbl_next.clear()

    def next_value(self):
        '''
        Next value and
        clear 'true values'
        '''
        if self.id == self.max_val - 1:
            self.check_input()
            self.lbl_limit.setText(f'{self.id + 1} /'
                                   f' {self.max_val}')
            self.btn_assert.blockSignals(True)
            self.btn_next.blockSignals(True)
            self.btn_back.blockSignals(True)
            self.get_Action.blockSignals(True)
            self.line_2.setReadOnly(True)
            self.line_3.setReadOnly(True)
            self.line_t.setReadOnly(True)
            self.doAction()
        else:
            if self.flag_back_btn_activate == True:
                self.mechanick_next()
                self.flag_back_btn_activate = False
            else:
                self.check_input()
                self.mechanick_next()

    def button_palanuk(self):
        '''
        Info for smail
        '''
        win_palanuk = QWidget(self, Qt.Window)
        win_palanuk.setWindowModality(Qt.WindowModal)
        win_palanuk.setWindowTitle('Чак Паланик')
        win_palanuk.setFixedSize(600, 600)
        win_palanuk.move(
            QApplication.desktop().screen().rect().center()
            - win_palanuk.rect().center()
        )
        win_palanuk.show()
        self.image_background(win_palanuk, 600, 600, "images.jpeg")
        because = QPushButton('Потому что', win_palanuk)
        because.resize(self.btn_assert.sizeHint())
        because.adjustSize()
        because.setGeometry(350, 500, 200, 50)
        because.clicked.connect(win_palanuk.close)
        because.show()

    def buttom_browser(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def timerEvent(self, e):
        '''
        For statusbar
        '''
        if self.step >= 100:
            self.timer.stop()
            self.show_verbs()
            self.lbl_limit.setFont(QtGui.QFont
                                   ('Times', 20, QtGui.QFont.Bold))
            self.lbl_limit.setText(f'{self.true_input} /'
                                   f' {self.max_val * 3}')
            self.lbl_limit.move(410, 295)
            self.lbl_lim_set_stat.setText('Правильных ответов')
            self.true_limit.move(660, 280)
            self.true_limit.setText('Тест завершён')
            self.true_limit_2.setText('ctr + Q')
            self.true_limit.adjustSize()
            self.true_limit_2.adjustSize()
            self.lbl_next.clear()
            return
        self.step += 25
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
        if self.id == self.max_val-1:
            reply = QMessageBox.question(self, 'Попытка выхода',
                                         "Выйти - 'Yes', попробовать снова - 'Retry'",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Retry,
                                         QMessageBox.Retry)
        else:
            reply = QMessageBox.question(self, 'Попытка выхода',
                                         "Вы действительно хотите выйти?",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        elif reply == QMessageBox.Retry:
            event.ignore()
            self.start_program()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Base()
    sys.exit(app.exec_())

