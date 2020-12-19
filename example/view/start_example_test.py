# coding=utf-8
"""
    create by pymu
    on 2020/12/18
    at 17:14
    使用eq 开发一个测试页面代码
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton

from common.base.eq_init import EasyQtInit
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0


class TestActivity(FrameLessWindowHintActivity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置布局"""
        super(TestActivity, self).place()
        # 添加默认的标题栏0
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)
        button = QPushButton("点击按钮")
        button.clicked.connect(self.test_click)
        self.body_layout.addWidget(button, alignment=Qt.AlignTop)

    def test_click(self):
        """测试点击事件"""
        raise ValueError("不应该传入没有定义的值")

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(TestActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)


if __name__ == '__main__':
    EasyQtInit(TestActivity()).run()
