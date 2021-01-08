# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：提示窗
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QToolTip

from core.launch import EasyQtInit
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0


class TestActivity(FrameLessWindowHintActivity):
    """更多详细用法 请参阅：https://doc-snapshots.qt.io/qt5-5.15/qtooltip.html"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置组件"""
        super(TestActivity, self).place()
        # 添加默认的标题栏0
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)

        button = QPushButton("手动激发tip")
        button.setToolTip("这是一个提示窗")
        # noinspection PyUnresolvedReferences
        button.clicked.connect(self.show_tool_tip)
        button.setFixedWidth(170)
        self.body_layout.addWidget(button)

        button1 = QPushButton("HTML 格式的tip")
        button1.setFixedWidth(170)
        button1.setToolTip(
            "<p>正如在java中存在很多工具类，jar包，在python中也存在标准库，标准库是一组模块，如collections模块，其包含的OrderedDict可以记录键值对的添加顺序</p>")
        self.body_layout.addWidget(button1)

        # 拉伸填充置顶
        self.body_layout.addStretch()

    def show_tool_tip(self):
        """手动激发提示框"""
        QToolTip.showText(self.pos(), '这是一个被signal激发的tips哦')

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
