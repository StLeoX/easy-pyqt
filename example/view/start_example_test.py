# coding=utf-8
"""
    create by pymu
    on 2020/12/18
    at 17:14
    使用eq 开发一个测试页面代码
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QPushButton, QLineEdit

from core.button import BaseButton, QPushButtonToBaseButton
from core.launch import EasyQtInit
from core.layout import FlowLayout
from config.const import WidgetProperty
from view.activity.activity_dialog_normal import NormalDialogActivity
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0


class TestActivity(FrameLessWindowHintActivity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_a = True
        self.procedure()

    def place(self):
        """放置布局"""
        super(TestActivity, self).place()
        # 添加默认的标题栏0
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)
        g = QGroupBox()
        f_layout = FlowLayout(spacing=10)
        g.setLayout(f_layout)

        # comBox = QComboBox()
        # comBox.setView(QListView())
        # comBox.addItems(
        #     ['Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', 'Java', 'C#', 'PHP', ])
        # f_layout.addWidget(comBox)

        button1 = BaseButton("原始button")
        button1.setToolTip("常用于表示不引人注意的动作")
        f_layout.addWidget(button1)

        button2 = BaseButton("积极button")
        button2.setToolTip("常用于表示积极的动作")
        button2.setProperty(*WidgetProperty.btn_class_normal[1])
        f_layout.addWidget(button2)

        button3 = BaseButton("警告button")
        button3.setToolTip("橙黄色带有冲击性的颜色")
        button3.setProperty(*WidgetProperty.btn_class_warning[1])
        f_layout.addWidget(button3)

        button4 = BaseButton("危险button")
        button4.setToolTip("带有冲击性的颜色")
        button4.clicked.connect(self.unused_button5)
        button4.setProperty(*WidgetProperty.btn_class_danger[1])
        f_layout.addWidget(button4)

        self.button5 = BaseButton("禁用button")
        self.button5.setToolTip("按钮不可用")
        self.button5.clicked.connect(lambda: NormalDialogActivity(info="当前按钮是可用的").exec_())
        self.button5.setProperty(*WidgetProperty.btn_class_normal[1])
        self.button5.setDisabled(self.is_a)
        f_layout.addWidget(self.button5)

        button6 = BaseButton("带图标的button")
        button6.setToolTip("带图标的button")
        button6.setProperty(*WidgetProperty.btn_class_normal[1])
        button6.setIcon(self.resource.awesome_font_icon("fa.eercast"))
        f_layout.addWidget(button6)

        button7 = BaseButton("可变图标的button")
        button7.setToolTip("可变图标的button")
        button7.setProperty(*WidgetProperty.btn_class_normal[1])
        button7.setIcon(self.resource.awesome_font_icon("fa.frown-o"))
        button7.setListenHover(True)
        button7.hover_in.connect(lambda: button7.setIcon(self.resource.awesome_font_icon("fa.grav")))
        button7.hover_out.connect(lambda: button7.setIcon(self.resource.awesome_font_icon("fa.frown-o")))
        f_layout.addWidget(button7)

        # todo 父类转子类
        self.button8 = QPushButton()
        self.button8.setIcon(self.resource.awesome_font_icon("fa.frown-o"))
        self.button8.setToolTip("ui加载的button， 然后升格为派生子类BaseButton， 也就是说我现在是BaseButton类型")
        f_layout.addWidget(self.button8)

        # todo 父类转子类
        button9 = QPushButton()
        button9.setToolTip("ui加载的button")

        line_edit = QLineEdit("这是一个输入框")
        f_layout.addWidget(line_edit)

        line_edit1 = QLineEdit()
        line_edit1.setPlaceholderText("提示输入文本")
        f_layout.addWidget(line_edit1)

        # 验证失败的
        line_edit2 = QLineEdit()
        line_edit2.setEchoMode(QLineEdit.Password)
        line_edit2.setPlaceholderText("输入一些文本看看")
        f_layout.addWidget(line_edit2)

        # 验证失败的
        line_edit3 = QLineEdit()
        line_edit3.setPlaceholderText("假设这是你输入错误的文本")
        line_edit3.setProperty(*WidgetProperty.border_class_red[1])
        # line_edit3.setProperty("property_name", "border_class_blue")
        f_layout.addWidget(line_edit3)

        self.body_layout.addWidget(g)
        # 拉伸填充置顶
        self.body_layout.addStretch()

    def unused_button5(self):
        """设置button5不可用于可用"""
        self.is_a = not self.is_a
        self.button5.setDisabled(self.is_a)

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(TestActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)
        self.button8 = QPushButtonToBaseButton(self.button8)
        self.button8.setListenHover(True)
        # self.button8.setDisabled(True)
        self.button8.setProperty(*WidgetProperty.btn_class_normal[1])
        self.button8.hover_in.connect(lambda: self.button8.setIcon(self.resource.awesome_font_icon("fa.grav")))
        self.button8.hover_out.connect(lambda: self.button8.setIcon(self.resource.awesome_font_icon("fa.frown-o")))


if __name__ == '__main__':
    EasyQtInit(TestActivity()).run()
