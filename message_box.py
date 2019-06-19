import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QAction, QMessageBox, QApplication, QDesktopWidget
import graphics

class StartProject(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('Тестирование знаний')
        self.setFixedSize(910, 600)
        self.general_window()
        self.center()

    def general_window(self):
        '''
        Создание меню, основных виджетов,
        кнопок и надписей
        '''

        menubar = self.menuBar()
        opt_ns_Menu = menubar.addMenu('&Опции')
        get_Action = QAction('&Начать', self)
        get_Action.setShortcut('Ctrl+r')
        get_Action.triggered.connect(self.start_test)
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

        self.show()

    def start_test(self, event):
        reply = QMessageBox.question(self, 'Вопрос',
                                     "Начать тест сейчас?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            event.ignore()


    def center(self):
        '''
        Центрирование окна
        на запускаемом устройстве
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
    ex = StartProject()
    sys.exit(app.exec_())

