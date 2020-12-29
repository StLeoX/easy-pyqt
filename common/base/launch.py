# coding=utf-8
"""
    create by pymu
    on 2020/12/20
    at 0:50
    eq 启动类
"""
import ctypes
import sys

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QApplication

from common.base.activity import BaseActivity
from common.base.handle import ExceptionHandle
from common.loader.resource import ResourceLoader
from config.const import Config
from view.activity.activity_dialog_normal import NormalDialogActivity

# 放在py文件中，需要在窗口显示之前实例化
app = QApplication.instance() or QApplication(sys.argv)


class EasyQtInit:
    """默认的eq启动类"""

    def __init__(self, index_activity: BaseActivity = BaseActivity(), is_run_unique=True):
        """
        启动初始化，设置是否唯一启动

        :param index_activity: 启动的窗口
        :param is_run_unique: 是否需要唯一启动
        """
        self.localServer = QLocalServer()
        self.ex_handle = ExceptionHandle()
        self.index_activity = index_activity
        self.is_run_unique = is_run_unique
        self.socket = QLocalSocket()

    def run(self):
        """启动方法"""
        app.setStyleSheet(ResourceLoader().style_from("common.css"))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(Config.unique_name)
        self.socket.connectToServer(Config.app_name)
        if self.is_run_unique and self.socket.waitForConnected(500):
            NormalDialogActivity("已有实例在运行", title="重复运行").exec()
            app.quit()
        else:
            self.localServer.listen(Config.app_name)
            self.index_activity.show()
            sys.exit(app.exec_())
        self.localServer.close()
