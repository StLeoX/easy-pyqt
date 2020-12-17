# coding=utf-8
"""
    create by pymu
    on 2020/12/11
    at 20:22
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton

from view.activity.activity_dialog_normal import NormalDialogActivity
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0


class TestActivity(FrameLessWindowHintActivity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置布局"""
        super(TestActivity, self).place()
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)
        button = QPushButton("测试")
        # noinspection PyUnresolvedReferences
        button.clicked.connect(self.test)
        self.body_layout.addWidget(button)

    def test(self):
        try:
            NormalDialogActivity().exec()
        except Exception as e:
            raise e

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(TestActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)
