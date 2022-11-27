# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from tkinter import messagebox
import time,threading
T1 = time.perf_counter()
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_MainWindow(object):

    def clicktwo(self):
        c = QApplication.clipboard()
        if self.textEdit_2.toPlainText=="":
            messagebox.showerror("","错误，这是空的")
        else:


            c.setText(self.textEdit_2.toPlainText())

    def clickone(self):
        str1 = self.textEdit.toPlainText()
        if str1=="":

            messagebox.showerror("error","错误，不能为空")
        else:
            timeArray = time.localtime(float(str1))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            self.textEdit_2.setText(otherStyleTime)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(267, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setMidLineWidth(-4)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 267, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.clickone)
        self.pushButton_2.clicked.connect(self.clicktwo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "时间戳转换器"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "要转换的时间戳"))
        self.pushButton.setText(_translate("MainWindow", "转换"))
        self.pushButton_2.setText(_translate("MainWindow", "复制"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "转换的时间戳"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ChiCloud studio</span></p><p align=\"center\">驰云工作室</p><p align=\"center\"><a href=\"www.github.com/123ChiCloud\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p></body></html>"))

        self.ti()
    def ti(self):

        time.sleep(1)
        nowtime = time.time ( )
        print ( nowtime )

        self.textEdit.setText ( str ( nowtime ) )








import sys
def main():


    app = QtWidgets.QApplication ( sys.argv )


    MainWindows = QtWidgets.QMainWindow ( )

    ui = Ui_MainWindow ( )
    ui.setupUi ( MainWindows )

    MainWindows.show ( )


    sys.exit ( app.exec_ ( ) )


T2 =time.perf_counter()
def END():
    with open("log.txt","a") as f:
        str2=time.time()
        timeArray = time.localtime ( float ( str2 ) )
        otherStyleTime = time.strftime ( "%Y-%m-%d %H:%M:%S" , timeArray )
        log=(str(otherStyleTime)+'\n')
        f.write(log)
END()
main()
