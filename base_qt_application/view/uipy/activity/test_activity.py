# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_activity.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_test_content(object):
    def setupUi(self, test_content):
        test_content.setObjectName("test_content")
        test_content.resize(583, 324)
        self.test_main = QtWidgets.QVBoxLayout(test_content)
        self.test_main.setContentsMargins(5, 5, 5, 5)
        self.test_main.setSpacing(0)
        self.test_main.setObjectName("test_main")
        self.textBrowser = QtWidgets.QTextBrowser(test_content)
        self.textBrowser.setObjectName("textBrowser")
        self.test_main.addWidget(self.textBrowser)

        self.retranslateUi(test_content)
        QtCore.QMetaObject.connectSlotsByName(test_content)

    def retranslateUi(self, test_content):
        _translate = QtCore.QCoreApplication.translate
        test_content.setWindowTitle(_translate("test_content", "Form"))
        self.textBrowser.setHtml(_translate("test_content", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\">宫妆巧弄非凡类，诚然王母降瑶池</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test_content = QtWidgets.QWidget()
    ui = Ui_test_content()
    ui.setupUi(test_content)
    test_content.show()
    sys.exit(app.exec_())
