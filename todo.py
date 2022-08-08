# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Notification import Item_From_TodoList_Added_In_Done_File
import time
from datetime import date
class Ui_To_Do_List(object):

        def grab_all(self):
                file=open('/home/atharva/Downloads/Jarvis/todo_store.txt','r')
                L = file.readlines()
                b = []
                for line in L:
                        length = len(line)
                        item = line[22:length-1]
                        b.append(item)
                for items in b:
                        self.listWidget.addItem(f"{items}\n")



        def add_item(self):
                item = self.lineEdit.text()
                clicked = self.listWidget.count()
                clicked1 = clicked+1
                self.listWidget.addItem(f"{clicked1}. {item}\n")
                self.lineEdit.setText("")
                t = time.strftime("%I:%M %p")
                current_date=date.today()
                file=open('/home/atharva/Downloads/Jarvis/todo_store.txt','a')
                file.write(f'{clicked1} {current_date} {t} {clicked1}.{item}\n')


        def delete_selected(self):
                clicked = self.listWidget.currentRow()
                clicked1 = clicked+1
                self.listWidget.takeItem(clicked)
                with open('/home/atharva/Downloads/Jarvis/todo_store.txt', 'r') as fr:
                        lines = fr.readlines()
                ptr = 1
                with open('/home/atharva/Downloads/Jarvis/todo_store.txt', 'w') as fw:
                        for line in lines:
                        
                                # we want to remove 5th line
                                if ptr != clicked1:
                                        fw.write(line)
                                        ptr += 1



        def clear_all(self):
                self.listWidget.clear()
                f = open("/home/atharva/Downloads/Jarvis/todo_store.txt", "r+") 
                f.seek(0) 
                f.truncate() 
        def Done(self):
                Item = self.listWidget.currentItem().text()
                clicked = self.listWidget.currentRow()
                clicked1 = clicked+1
                self.listWidget.takeItem(clicked)
                file=open('/home/atharva/Downloads/Jarvis/done.txt','a')
                t = time.strftime("%I:%M %p")
                current_date=date.today()
                file.write(f'{current_date} {t} {Item}\n')
                Item_From_TodoList_Added_In_Done_File(Item)
                file.close()
                with open('/home/atharva/Downloads/Jarvis/todo_store.txt', 'r') as fr:
                        lines = fr.readlines()
                ptr = 1
                with open('/home/atharva/Downloads/Jarvis/todo_store.txt', 'w') as fw:
                        for line in lines:
                                if ptr != clicked1:
                                        fw.write(line)
                                        ptr += 1


        def setupUi(self, To_Do_List):
                To_Do_List.setObjectName("To_Do_List")
                To_Do_List.resize(681, 683)
                self.centralwidget = QtWidgets.QWidget(To_Do_List)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 0, 801, 711))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("/home/atharva/Downloads/Jarvis/All GUI Requirements/Untitled design(1).png"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(120, 100, 461, 511))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.label_2.setFont(font)
                self.label_2.setText("")
                self.label_2.setTextFormat(QtCore.Qt.AutoText)
                self.label_2.setPixmap(QtGui.QPixmap("/home/atharva/Downloads/Jarvis/All GUI Requirements/white.jpg"))
                self.label_2.setScaledContents(True)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(120, 100, 461, 51))
                self.label_3.setStyleSheet("background-color: rgb(39, 108, 168);")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(130, 110, 111, 31))
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(510, 100, 91, 51))
                self.label_5.setObjectName("label_5")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(130, 190, 391, 51))
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("background-color: rgb(231, 231, 231);\n"
        "color: rgb(0, 0, 0);\n"
        "border-radius:5px;\n"
        "border-color: rgb(47, 117, 218);\n"
        "padding-left:10px;")
                self.lineEdit.setText("")
                self.lineEdit.setDragEnabled(False)
                self.lineEdit.setObjectName("lineEdit")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(526, 190, 41, 51))
                self.label_6.setStyleSheet("background-color: rgb(72, 93, 194);\n"
        "border-radius:none;")
                self.label_6.setObjectName("label_6")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(520, 190, 51, 51))
                self.pushButton.setStyleSheet("border-radius:none;")
                self.pushButton.setText("")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.add_item)
                self.listWidget = QtWidgets.QListWidget(self.centralwidget)
                self.listWidget.setGeometry(QtCore.QRect(140, 270, 411, 241))
                self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);")
                self.listWidget.setObjectName("listWidget")
                # self.listWidget.itemClicked.connect(self.Done)
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(150, 530, 81, 61))
                self.label_7.setStyleSheet("background-color: rgb(205, 17, 17);\n"
        "")
                self.label_7.setText("")
                self.label_7.setPixmap(QtGui.QPixmap("/home/atharva/Downloads/Jarvis/All GUI Requirements/bin.jpg"))
                self.label_7.setScaledContents(True)
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(440, 540, 111, 41))
                self.label_8.setStyleSheet("background-color: rgb(61, 157, 223);\n"
        "border-radius:none;")
                self.label_8.setObjectName("label_8")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(436, 540, 121, 41))
                self.pushButton_2.setStyleSheet("border-radius:none;")
                self.pushButton_2.setText("")
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(self.clear_all)
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_3.setGeometry(QtCore.QRect(150, 530, 81, 61))
                self.pushButton_3.setStyleSheet("border-radius:none;")
                self.pushButton_3.setText("")
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_3.clicked.connect(self.delete_selected)
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(290, 530, 81, 61))
                self.label_9.setStyleSheet("background-color: rgb(49, 124, 26);")
                self.label_9.setObjectName("label_9")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(296, 530, 71, 61))
                self.pushButton_4.setStyleSheet("border-radius:none;")
                self.pushButton_4.setText("")
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_4.clicked.connect(self.Done)
                To_Do_List.setCentralWidget(self.centralwidget)

                self.retranslateUi(To_Do_List)
                QtCore.QMetaObject.connectSlotsByName(To_Do_List)
                self.grab_all()
        def retranslateUi(self, To_Do_List):
                _translate = QtCore.QCoreApplication.translate
                To_Do_List.setWindowTitle(_translate("To_Do_List", "MainWindow"))
                self.label_3.setText(_translate("To_Do_List", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
                self.label_4.setText(_translate("To_Do_List", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Todo List</span></p></body></html>"))
                self.label_5.setText(_translate("To_Do_List", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">+</span></p></body></html>"))
                self.lineEdit.setPlaceholderText(_translate("To_Do_List", "Add You Todo"))
                self.label_6.setText(_translate("To_Do_List", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">✔</span></p></body></html>"))
                self.label_8.setText(_translate("To_Do_List", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Clear All</span></p></body></html>"))
                self.label_9.setText(_translate("To_Do_List", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Done</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    To_Do_List = QtWidgets.QMainWindow()
    ui = Ui_To_Do_List()
    ui.setupUi(To_Do_List)
    To_Do_List.show()
    sys.exit(app.exec_())
