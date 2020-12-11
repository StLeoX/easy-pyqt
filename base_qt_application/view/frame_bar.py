# coding=utf-8
"""
    create by pymu on 2020/10/23
    file: bar.py
"""
from PyQt5.QtCore import Qt

from view.base_view import BaseView
from view.uipy.frame.bar import Ui_base_bar


class BaseBar(BaseView, Ui_base_bar):

    def __init__(self, flags=None):
        """自定义标题栏， 注意这是一个组件"""
        super().__init__(flags)
        # 自定义组件，在顶级容器设置qss样式失效问题
        # 在继承的子类中调用一下方法
        self.setAttribute(Qt.WA_StyledBackground)
        self.procedure()

    def procedure(self):
        """初始化流程"""
        self.setupUi(self)
        self.configure()

    def set_signal(self):
        """信号设定"""
        ...

    def configure(self):
        """自定义标题栏配置"""
        self.app_name.setText("简单的页面")
        self.set_style("bar.css")
        self.app_logo.setIcon(self.resource.qt_icon_project_png)
