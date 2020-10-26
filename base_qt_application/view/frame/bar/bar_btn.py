# coding=utf-8
"""
    create by pymu on 2020/10/23
    自定义标题栏中的最小/最大/关闭按钮
"""
from PyQt5.QtWidgets import QWidget

from view.base_view import BaseView
from view.uipy.frame.bar.bar_btn_normal_close_min import Ui_bar_btn_div


class BarBtnNormal(QWidget, Ui_bar_btn_div, BaseView):
    """
    标题栏，右侧的最大/最小/关闭按钮
    """

    def __init__(self):
        super().__init__()

    def set_signal(self):
        pass

    def configure(self):
        """
        配置
        :return:
        """
