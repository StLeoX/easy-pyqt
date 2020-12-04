# coding=utf-8
"""
    create by pymu on 2020/10/23
"""
from view.activity.base_activity import BaseActivity
from view.frame.bar.bar import BaseBar
from view.uipy.frame.test import Ui_Form


class TestActivity(BaseActivity, Ui_Form):
    """
    测试页面
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def procedure(self):
        """
        实例化流程
        :return:
        """
        self.setupUi(self)
        self.place()
        self.configure()
        self.set_signal()

    def place(self):
        """
        对页面进行微调, 引发图形变换的跟bar没有关系，就是不能在主空间下直接使用控件
        :return:
        """
        self.bar = BaseBar()
        self.verticalLayout_2.insertWidget(0, self.bar)

    def configure(self):
        """
        页面配置
        :return:
        """
        BaseActivity.configure(self)
        self.bar_mini = self.bar.bar_btn_min
        self.bar_close = self.bar.bar_btn_close
        self.bar_normal = self.bar.bar_btn_normal
