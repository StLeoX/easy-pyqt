# coding=utf-8
"""
    create by pymu on 2020/10/23
    file: bar.py
"""

from view.base_view import BaseView
from view.uipy.frame.bar import Ui_base_bar


class BaseBar(BaseView, Ui_base_bar):

    def __init__(self):
        super().__init__()
        self.procedure()

    def procedure(self):
        self.setupUi(self)

    def set_signal(self):
        pass

    def configure(self):
        self.set_style(self.resource.style_from("bar.css"))
