# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def loginCheck(self):
        self.rstWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog()
        self.setupUi(self.rstWindow)
        self.rstWindow.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 332)
        self.user_name = QtWidgets.QLabel(Dialog)
        self.user_name.setGeometry(QtCore.QRect(50, 60, 101, 31))
        self.user_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_name.setObjectName("user_name")
        self.pswd = QtWidgets.QLabel(Dialog)
        self.pswd.setGeometry(QtCore.QRect(50, 90, 101, 31))
        self.pswd.setObjectName("pswd")
        self.uname = QtWidgets.QLineEdit(Dialog)
        self.uname.setGeometry(QtCore.QRect(180, 70, 141, 20))
        self.uname.setObjectName("uname")
        self.passwrd = QtWidgets.QLineEdit(Dialog)
        self.passwrd.setGeometry(QtCore.QRect(180, 100, 141, 20))
        self.passwrd.setObjectName("passwrd")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.loginCheck)
        self.rst_btn = QtWidgets.QPushButton(Dialog)
        self.rst_btn.setGeometry(QtCore.QRect(230, 200, 75, 23))
        self.rst_btn.setObjectName("rst_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.user_name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Username</span></p></body></html>"))
        self.pswd.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.rst_btn.setText(_translate("Dialog", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

