# coding=utf-8
"""
    create by pymu on 2020/10/23
"""
from view.activity.base_activity import BaseActivity
from view.frame.bar.bar import BaseBar
from view.uipy.activity.test_activity import Ui_test_content


class TestActivity(BaseActivity, Ui_test_content):
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
        self.configure()
        self.place()

    def place(self):
        """
        对页面进行微调
        :return:
        """
        self.bar = BaseBar()
        self.test_main.insertWidget(0, self.bar)

    def configure(self):
        """
        页面配置
        :return:
        """
        BaseActivity.configure(self)
