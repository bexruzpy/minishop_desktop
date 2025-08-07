from PyQt5.QtWidgets import QFrame, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class BaseFrame(QFrame):
    def __init__(self, path):
        super(QFrame, self).__init__()
        self.path = "designs/" + path
        loadUi(self.path, self)

class Product(QFrame):
    def __init__(self):
        super(Product, self).__init__()
        self.path = "designs/product.ui"
        loadUi(self.path, self)

class Group(QPushButton):
    def __init__(self, group_name):
        self.group_name = group_name
        self.text = group_name
        super(Group, self).__init__(text=group_name)
        self.setStyleSheet("""QPushButton{
            text-align: left;
            padding: 14px 16px;
            color: rgb(0, 0, 0);
            font-family: "Segoe UI Bold";
            background-color: rgba(0, 0, 0, 10);
            border:1px solid rgba(0, 0, 0, 20);
            font-size: 20px;
        }
        QPushButton:hover{
            background-color: rgba(0, 0, 0, 20);
            border:1px solid rgba(0, 0, 0, 30);
        }
        QPushButton:focus{
            background-color: rgba(0, 0, 0, 50);
            border:1px solid rgba(0, 0, 0, 60);
        }""")
        
