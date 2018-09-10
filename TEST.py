# class MyThread(threading.Thread):
#     def __init__(self, window, *args, **kwargs):
#         super(MyThread, self).__init__(*args, **kwargs)
#         self.daemon = True
#         self.window = window
#     def run(self):
#         sleep(4)
#         self.window.add_user.emit("hanmeimei")
# class Window(QWidget):
#     addbtn = pyqtSignal()
#     add_user = pyqtSignal(str)
#     def __init__(self, *args, **kwargs):
#         super(Window, self).__init__(*args, **kwargs)
#         self.setGeometry(0, 0, 500, 300)
#         self.add_user.connect(self.add_contact)
#         thread = MyThread(self)
#         self.contacts = QListWidget(self)
#         self.contacts.setGeometry(10, 10, 100, 300)
#         self.contacts.addItems(("bob", "jim", "lilei"))
#         thread.start()
#     def add_contact(self, username):
#         self.contacts.addItem(username)

from PyQt5.QtWidgets import QWidget,QListWidget,QApplication
import threading,sys
from PyQt5.QtCore import pyqtSignal

class Mythread(threading.Thread):
    def __init__(self,window):
        super(Mythread,self).__init__()
        self.daemon = True
        self.window = window

    def run(self):
        self.window.singnal.emit()


class Win(QWidget):
    singnal = pyqtSignal()
    def __init__(self):
        super(Win,self).__init__()
        thread = Mythread(self)
        thread.start()
        self.contacts = QListWidget(self)
        self.contacts = QListWidget(self)
        self.contacts.setGeometry(10, 10, 100, 300)
        self.contacts.addItems(("bob", "jim", "lilei"))
        self.singnal.connect(self.add_user())
        self.show()

    def add_user(self, username):
        self.contacts.addItem(username)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())







