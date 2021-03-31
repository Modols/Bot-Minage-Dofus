from bot import Bot, posAmakna, posSadi

from PySide2 import QtWidgets, QtCore


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bot Dofus")
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.btn_startBot = QtWidgets.QPushButton("Start Bot")
        self.btn_stopBot = QtWidgets.QPushButton("Stop Bot")

        self.layout.addWidget(self.btn_startBot)
        self.layout.addWidget(self.btn_stopBot)

    def setup_connections(self):
        self.btn_startBot.clicked.connect(self.start_bot)
        self.btn_stopBot.clicked.connect(self.stop_bot)

    def start_bot(self):
        bot1 = Bot(posAmakna)
        bot1.start()
        print("Bot Started")

    def stop_bot(self):
        # self.bot1 = 0
        print("Bot Stopped")


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()
