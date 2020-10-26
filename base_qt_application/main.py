# coding=utf-8
"""
    create by pymu on 2020/6/18
    package: .main.py
"""
import ctypes
import sys

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QApplication

from common.util.logger import Logger
from config.const import Config
from view.activity.dialog import error_dialog
from example.test_activity import TestActivity

if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(Config.unique_name)
    localServer = QLocalServer()
    try:
        app = QApplication(sys.argv)
        socket = QLocalSocket()
        socket.connectToServer(Config.app_name)
        if socket.waitForConnected(500):
            error_dialog("已有实例在运行")
            app.quit()
        else:
            localServer.listen(Config.app_name)
            bar = TestActivity()
            bar.show()
            sys.exit(app.exec_())
    except Exception as e:
        Logger().error(f"程序崩溃, {e}")
    finally:
        localServer.close()
