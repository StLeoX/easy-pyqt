# coding=utf-8
"""
    create by pymu
    on 2020/12/16
    at 10:01
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel

from view.base_view import BaseView
from view.uipy.dialog_info_waring_error import Ui_Form


class WaitingDialog(QDialog, BaseView):
    def __init__(self, show_info="加载中请稍后"):
        """
        等待对话框
        使用方法：
        实例化弹出层之后
            - # 在BaseActivity 中会初始化默认的拥塞弹窗
            - self.waiting_dialog = waiting_dialog(waiting_info="显示文本信息")
            - 在需要执行的线程中进行拥塞UI
            - 如在修改数据线程：
            - self.waiting_dialog
        :param show_info: 默认显示的文本
        :return:QDialog
        """
        super().__init__()
        self.show_info = show_info
        self.procedure()

    def place(self) -> None:
        layout = QHBoxLayout(self)
        label = QLabel(self.show_info)
        label.setFont(self.resource.qt_font_11)
        layout.addWidget(label, alignment=Qt.AlignCenter)

    def configure(self) -> None:
        super(WaitingDialog, self).configure()
        self.set_style("common.css")
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.Tool |
                            Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint |
                            Qt.WindowMaximizeButtonHint)
        self.resize(240, 60)


class NormalDialogFrame(BaseView, Ui_Form):
    """
    一般的弹窗样式，具体的配件需要模板生成，
    如果调用的弹窗有其他的功能或者组件
    请新建一个弹窗类
    """

    def __init__(self, flags=None, *args, **kwargs):
        """一般弹窗, 继承自无边框窗体"""
        super().__init__(flags, *args, **kwargs)
        self.procedure()

    def place(self):
        super(NormalDialogFrame, self).place()
        self.setupUi(self)

    def configure(self) -> None:
        super(NormalDialogFrame, self).configure()
