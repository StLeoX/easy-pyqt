# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from common.base.launch import EasyQtInit
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0
from view.ui.start_example_tab_bar import Ui_Form


class TestActivity(FrameLessWindowHintActivity, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置组件"""
        super(TestActivity, self).place()
        # 添加默认的标题栏0
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)

        # 放置组件区
        div = QWidget()
        self.setupUi(div)
        self.body_layout.addWidget(div)

        # 拉伸填充置顶
        self.body_layout.addStretch()

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(TestActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)


if __name__ == '__main__':
    # 启动类
    EasyQtInit(TestActivity()).run()
