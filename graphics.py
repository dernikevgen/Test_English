import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QDesktopWidget, QGridLayout, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton, QWidget, QLineEdit, QFileDialog, QSizePolicy
from PyQt5.QtGui import QColor


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Определяем QWidget
        widget = QWidget(self)
        self.setCentralWidget(widget)
        self.textEdit = QTextEdit()
        self.statusBar()

        get_Action = QAction('&Начать', self)
        get_Action.setShortcut('Ctrl+r')

        exit_Action = QAction('&Выход', self)
        exit_Action.setShortcut('Ctrl+Q')
        exit_Action.triggered.connect(self.close)

        menubar = self.menuBar()
        opt_ns_Menu = menubar.addMenu('&Опции')
        opt_ns_Menu.addAction(get_Action)
        opt_ns_Menu.addAction(exit_Action)

        try_Action = QAction('&Статистика', self)
        try_Menu = menubar.addMenu('&Попытки')
        try_Menu.addAction(try_Action)

        to_addAction = QAction('&О разработчика', self)
        dop_Menu = menubar.addMenu('&Дополнительно')
        dop_Menu.addAction(to_addAction)

        get_Action.setStatusTip('Начать тест')
        exit_Action.setStatusTip('Выход из программы')
        try_Action.setStatusTip('Предыдущие попытки')
        to_addAction.setStatusTip('Важная информация')

        grid = QGridLayout(widget)
        self.btn_1 = QPushButton('Первая', self)
        self.btn_1.move(50, 150)
        self.le = QLineEdit(self)
        self.le.setText(str('be'))

        self.le.move(150, 150)
        self.le = QLineEdit(self)
        self.le.setText(str('be'))
        self.le.move(150, 200)

        self.btn_2 = QPushButton('Вторая', self)
        self.btn_2.move(250, 150)
        self.le = QLineEdit(self)
        self.le.move(350, 150)
        self.le = QLineEdit(self)
        self.le.move(350, 200)

        self.btn_3 = QPushButton('Третья', self)
        self.btn_3.move(450, 150)
        self.le = QLineEdit(self)
        self.le.move(550, 150)
        self.le = QLineEdit(self)
        self.le.move(550, 200)

        self.btn_4 = QPushButton('Перевод', self)
        self.btn_4.move(650, 150)
        self.le = QLineEdit(self)
        self.le.move(750, 150)
        self.le = QLineEdit(self)
        self.le.move(750, 200)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn_1)
        hbox.addWidget(self.btn_2)
        hbox.addWidget(self.btn_3)
        hbox.addWidget(self.btn_4)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.resize(900, 600)
        self.center()
        self.setWindowTitle('НУ ЧЁ НАРОД ПОГНАЛИ ?')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Попытка выхода', "Вы действительно хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())