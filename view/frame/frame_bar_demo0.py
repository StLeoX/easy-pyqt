# coding=utf-8
"""
    create by pymu
    on 2020/12/11
    at 20:18
    默认的标题栏样式1
"""
from common.base.view import BaseView
from view.ui.frame_bar import Ui_bar


class FrameBarDemo0(BaseView, Ui_bar):
    """
    标题栏 demo0
    """

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        self.procedure()

    def procedure(self) -> None:
        self.setupUi(self)
        super(FrameBarDemo0, self).procedure()

    def set_signal(self) -> None:
        pass

    def configure(self) -> None:
        super(FrameBarDemo0, self).configure()
        self.btn_bar_app_name.setText("默认标题栏一")
