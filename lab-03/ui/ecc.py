from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_Header = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Header.setGeometry(QtCore.QRect(200, 50, 161, 51))
        self.lbl_Header.setObjectName("lbl_Header")
        self.btn_gen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen.setGeometry(QtCore.QRect(320, 60, 75, 23))
        self.btn_gen.setObjectName("btn_gen")
        self.lbl_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info.setGeometry(QtCore.QRect(50, 120, 61, 16))
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_sig = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sig.setGeometry(QtCore.QRect(50, 220, 47, 13))
        self.lbl_sig.setObjectName("lbl_sig")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(50, 320, 75, 23))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(250, 310, 75, 23))
        self.btn_verify.setObjectName("btn_verify")
        self.txt_info_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info_text.setGeometry(QtCore.QRect(150, 110, 351, 71))
        self.txt_info_text.setObjectName("txt_info_text")
        self.txt_signature_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature_text.setGeometry(QtCore.QRect(150, 200, 351, 71))
        self.txt_signature_text.setObjectName("txt_signature_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_Header.setText(_translate("MainWindow", "ECC CIPHER"))
        self.btn_gen.setText(_translate("MainWindow", "Generate Key"))
        self.lbl_info.setText(_translate("MainWindow", "Information"))
        self.lbl_sig.setText(_translate("MainWindow", "Signature")) 
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
