# coding=utf-8
"""
    create by pymu
    on 2020/12/16
    at 11:19
     一般弹窗
"""
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.activity.dialog import NormalDialogFrame


class NormalDialogActivity(FrameLessWindowHintActivity):

    def __init__(self):
        """一般弹窗, 继承自无边框窗体"""
        super().__init__()
        self.procedure()

    def place(self):
        super(NormalDialogActivity, self).place()
        window_ui = NormalDialogFrame()
        self.bar = window_ui.bar
        self.bar_close = window_ui.btn_bar_close
        self.body_layout.addWidget(window_ui)


    def configure(self):
        super(NormalDialogActivity, self).configure()
        self.resize(300, 200)
