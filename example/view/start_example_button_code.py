# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发按钮示例
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QPushButton, QWidget, QHBoxLayout

from common.base.button import BaseButton, QPushButtonToBaseButton
from common.base.launch import EasyQtInit
from common.base.layout import FlowLayout
from config.const import WidgetProperty
from view.activity.activity_dialog_normal import NormalDialogActivity
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0


# noinspection PyAttributeOutsideInit
class StartExampleButtonActivity(FrameLessWindowHintActivity):
    """在代码中添加button"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 按钮是否可用
        self.button5_enable = True
        self.procedure()

    def place(self):
        """放置按钮"""
        super(StartExampleButtonActivity, self).place()
        # 添加默认的标题栏0
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)
        g = QGroupBox()
        f_layout = FlowLayout(spacing=10)
        g.setLayout(f_layout)

        button1 = BaseButton("原始button")
        # 类似的set 推荐放在configure中配置更好管理哦（如果配置方法很长，应该做出分类，抽离出方法，如设置button一类， set_button_configure）
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
        # noinspection PyUnresolvedReferences
        button4.clicked.connect(self.unused_button5)
        button4.setProperty(*WidgetProperty.btn_class_danger[1])
        f_layout.addWidget(button4)

        self.button5 = BaseButton("禁用button")
        self.button5.setToolTip("按钮不可用(BaseButton)")
        # 这里提倡事件连接放在 set_signal 方法中统一配置，这样好管理哦。
        # noinspection PyUnresolvedReferences
        self.button5.clicked.connect(lambda: NormalDialogActivity(info="当前按钮是可用的").exec_())
        self.button5.setProperty(*WidgetProperty.btn_class_normal[1])
        self.button5.setDisabled(self.button5_enable)
        f_layout.addWidget(self.button5)

        button6 = BaseButton("带图标的button")
        button6.setToolTip("带图标的button(BaseButton)")
        button6.setProperty(*WidgetProperty.btn_class_normal[1])
        button6.setIcon(self.resource.awesome_font_icon("fa.eercast"))
        f_layout.addWidget(button6)

        button7 = BaseButton("可变图标的button")
        button7.setToolTip("可变图标的button(BaseButton)")
        button7.setProperty(*WidgetProperty.btn_class_normal[1])
        button7.setIcon(self.resource.awesome_font_icon("fa.frown-o"))
        button7.setListenHover(True)
        # noinspection PyUnresolvedReferences
        button7.hover_in.connect(lambda: button7.setIcon(self.resource.awesome_font_icon("fa.grav")))
        # noinspection PyUnresolvedReferences
        button7.hover_out.connect(lambda: button7.setIcon(self.resource.awesome_font_icon("fa.frown-o")))
        f_layout.addWidget(button7)

        self.button8 = QPushButton()
        self.button8.setIcon(self.resource.awesome_font_icon("fa.frown-o"))
        self.button8.setToolTip("ui加载的button， 然后升格为派生子类BaseButton， 也就是说我现在是BaseButton类型")
        f_layout.addWidget(self.button8)

        # button9 = QPushButton()
        # button9.setIcon(self.resource.awesome_font_icon("fa.upload", color="black"))
        # button9.setToolTip("图标按钮：上传")
        # f_layout.addWidget(button9)
        #
        # button10 = QPushButton()
        # button10.setIcon(self.resource.awesome_font_icon("fa.download", color="black"))
        # button10.setToolTip("图标按钮：上传")
        # f_layout.addWidget(button10)

        # button 组
        button_group = QWidget()
        button_group_layout = QHBoxLayout(button_group)
        button_group_layout.setContentsMargins(0, 0, 0, 0)
        button_group_layout.setSpacing(1)
        button11 = QPushButton()
        button11.setIcon(self.resource.awesome_font_icon("fa.chevron-left", color="black"))
        button11.setToolTip("快退")
        button_group_layout.addWidget(button11)

        button12 = QPushButton()
        button12.setIcon(self.resource.awesome_font_icon("fa.pause", color="black"))
        button12.setToolTip("暂停")
        button_group_layout.addWidget(button12)

        button13 = QPushButton()
        button13.setIcon(self.resource.awesome_font_icon("fa.chevron-right", color="black"))
        button13.setToolTip("快进")
        button_group_layout.addWidget(button13)

        f_layout.addWidget(button_group)

        self.body_layout.addWidget(g)
        # 拉伸填充置顶
        self.body_layout.addStretch()

    def unused_button5(self):
        """设置button5不可用于可用"""
        self.button5_enable = not self.button5_enable
        self.button5.setDisabled(self.button5_enable)

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(StartExampleButtonActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)
        self.bar.btn_bar_app_name.setText("button 实例")

        #  将button8 升格为派生子类 BaseButton 解锁更多新姿势。
        self.button8 = QPushButtonToBaseButton(self.button8)
        self.button8.setListenHover(True)
        self.button8.setProperty(*WidgetProperty.btn_class_danger[1])
        # noinspection PyUnresolvedReferences
        self.button8.hover_in.connect(lambda: self.button8.setIcon(self.resource.awesome_font_icon("fa.grav")))
        # noinspection PyUnresolvedReferences
        self.button8.hover_out.connect(lambda: self.button8.setIcon(self.resource.awesome_font_icon("fa.frown-o")))


if __name__ == '__main__':
    # 启动类
    EasyQtInit(StartExampleButtonActivity()).run()
