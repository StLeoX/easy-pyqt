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
from view.dialog import error_dialog
from view.activity_frame_less_window_hint import FrameLessWindowHintActivity

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
            bar = FrameLessWindowHintActivity()
            bar.show()
            sys.exit(app.exec_())
    except Exception as e:
        Logger().error(f"程序崩溃, {e}")
        raise e
    finally:
        localServer.close()
