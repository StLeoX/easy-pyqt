# coding=utf-8
"""
    create by pymu
    on 2020/12/18
    at 17:14
    使用eq 开发一个测试页面代码
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QGroupBox

from common.base.launch import EasyQtInit
from common.base.layout import FlowLayout
from config.const import WidgetProperty
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0


class TestActivity(FrameLessWindowHintActivity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()
        self.is_a = True

    def place(self):
        """放置布局"""
        super(TestActivity, self).place()
        # 添加默认的标题栏0
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)
        g = QGroupBox()
        f_layout = FlowLayout()
        g.setLayout(f_layout)

        # comBox = QComboBox()
        # comBox.setView(QListView())
        # comBox.addItems(
        #     ['Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', ])
        # f_layout.addWidget(comBox)

        button1 = QPushButton("原始button")
        button1.setToolTip("常用于表示不引人注意的动作")
        f_layout.addWidget(button1)

        button2 = QPushButton("积极button")
        button2.setToolTip("常用于表示积极的动作")
        button2.setProperty(*WidgetProperty.btn_class_normal[1])
        f_layout.addWidget(button2)

        button3 = QPushButton("警告button")
        button3.setToolTip("橙黄色带有冲击性的颜色")
        button3.setProperty(*WidgetProperty.btn_class_warning[1])
        f_layout.addWidget(button3)

        button4 = QPushButton("危险button")
        button4.setToolTip("带有冲击性的颜色")
        button4.setProperty(*WidgetProperty.btn_class_danger[1])
        f_layout.addWidget(button4)

        button5 = QPushButton("禁用button")
        button5.setToolTip("按钮不可用")
        button5.setDisabled(True)
        button5.setProperty(*WidgetProperty.btn_class_disable[1])
        f_layout.addWidget(button5)

        self.body_layout.addWidget(g)
        self.body_layout.addStretch()

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(TestActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)


if __name__ == '__main__':
    EasyQtInit(TestActivity()).run()
