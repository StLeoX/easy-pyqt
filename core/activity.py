# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .base_activity.py
    基本的窗体结构初始化
"""

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QDialog

from core.thread import FuncThread, ResponseData
from common.util.logger import Logger
from config.const import Config
from view.activity.dialog import WaitingDialog
from core.view import BaseView
from view.dialog import message_ok, error_dialog


class BaseActivity(QDialog, BaseView):
    def __init__(self, flags=None, *args, **kwargs):
        """
        自定义窗口，他具有以下属性或者功能：
            - 属性：logger    日志记录
            - 属性：resource  静态资源管理
            - 属性：waiting_dialog 弹出层
            - 属性：message_text 默认的消息提示
            - 属性：error_dialog_str 默认的错误提示
            - 属性：default_thread 通用线程
            - 属性：bar_normal 最大最小化按钮，由子类赋值
            - 属性：bar        标题栏，由子类赋值
            - 属性：exception_handle        异常捕获
            - 功能：拖动窗体，需把控件赋值给 bar 作为载体
            - 功能：无边框，实例化子类时，其边距应设置为5
            - 功能：最大最小化，需把控件赋值给 bar_normal 作为载体
            - 功能：窗体拉伸，需要设定 self.setMouseTracking(True)
            - 功能：文件拖拽，需要开启
            - 功能：键盘事件监听
        """
        super().__init__(flags, *args, **kwargs)
        # 默认的执行线程
        self.default_func: FuncThread = FuncThread()
        # 默认的遮罩层
        self.waiting_dialog: WaitingDialog = WaitingDialog()
        self.logger = Logger()
        self.config = Config()

    def configure(self):
        """
        如果有用到两个样式表，则需要把两个样式表,都添加，
        activity的配置方法，这里设置了基本的页面属性\n
        """
        self.resize(1047, 680)
        self.setWindowTitle("应用名称")
        self.setWindowIcon(self.resource.qt_icon_project_ico)

    def place(self):
        """test_layout = QtWidgets.QHBoxLayout(self)"""
        ...

    def set_signal(self):
        """
        设置信号，如果需要父类信号，那在重构的子类方法中:super(类名, self).set_signal()
        """
        # 执行失败时，通信频道移交给错误弹窗
        self.default_func.thread_error_signal.connect(self.error_dialog)
        self.default_func.thread_signal.connect(self.do_nothing)

    def do_nothing(self, *args, **kwargs):
        """
        链接到无执行的方法上，
        防止线程在错误的时间通信
        :param args: args
        :param kwargs: kwargs
        :return: none
        """
        ...

    def dragEnterEvent(self, event):
        """
        判断拖拽物体是否有路径，有时拖拽生效
        :param event:
        :return:
        """
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        """
        拖拽移动
        :param event:
        :return:
        """
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(Qt.CopyAction)
            except Exception as e:
                self.logger.error(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """
        如果需要监听文件拖拽则重构此方法
        获取拖拽文件
        :param event:
        :return:
        """
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.CopyAction)
                event.accept()
                links = []
                for url in event.mimeData().urls():
                    links.append(str(url.toLocalFile()))
                print(links)
            else:
                event.ignore()
        except Exception as e:
            raise e

    def error_dialog(self, response: ResponseData):
        """
        执行出错，弹窗提示，
        :param response:
        :return:
        """
        if str(response.data) == "list index out of range":
            info = "结果为空"
        elif isinstance(response.data, PermissionError):
            info = "无权访问"
        else:
            info = "操作失败: {}".format(response.data)
        self._error_dialog_str(info)

    @staticmethod
    def error_dialog_str(err_info: str):
        """
        错误, 内部使用
        :param err_info:
        :return:
        """
        error_dialog(err_info)

    @staticmethod
    def message_text(info):
        """
        通知
        :param info:
        :return:
        """
        message_ok(info)

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        """
        双击的坐标小于头部坐标是才最大化, 如果不需要这个功能，在继承子类时重构此方法即可
        :param e:
        :return:
        """
        if not self.bar or not self.bar_normal:
            return
        if e.pos().y() < self.bar.y() + self.bar.height():
            self.bar_normal.click()

    def keyPressEvent(self, a0: QtGui.QKeyEvent):
        """
        键盘监听事件
        :param a0:
        :return:
        """
        if a0.key() == Qt.Key_Escape:
            a0.ignore()
        else:
            a0.accept()
