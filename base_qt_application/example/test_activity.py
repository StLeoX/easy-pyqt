# coding=utf-8
"""
    create by pymu
    on 2020/12/11
    at 20:22
"""
from PyQt5.QtCore import Qt

from view.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame_bar_demo0 import FrameBarDemo0


class TestActivity(FrameLessWindowHintActivity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置布局"""
        super(TestActivity, self).place()
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)

    def configure(self):
        """配置页面及控件属性"""
        super(TestActivity, self).configure()
        self.bar.btn_bar_close.setIcon(self.resource.awesome_font_icon("fa.close", color="red"))
        self.bar.btn_bar_normal.setIcon(self.resource.awesome_font_icon("fa.window-maximize", color="red"))
        self.bar.btn_bar_min.setIcon(self.resource.awesome_font_icon("fa.window-minimize", color="red"))
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)
        self.bar.btn_bar_app_name.setText("测试窗口")
        self.bar.setMouseTracking(True)
        self.bar.set_style("bar.css")
