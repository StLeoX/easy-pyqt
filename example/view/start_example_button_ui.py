# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：使用qt designer ui模板生成的button
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from core.button import QPushButtonToBaseButton
from core.launch import EasyQtInit
from config.const import WidgetProperty
from view.activity.activity_dialog_normal import NormalDialogActivity
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0
from view.ui.start_example_button import Ui_Form


# noinspection PyAttributeOutsideInit
class StartExampleButtonUIActivity(FrameLessWindowHintActivity, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        super(StartExampleButtonUIActivity, self).place()
        # 添加默认的标题栏0
        self.bar: FrameBarDemo0 = FrameBarDemo0(self)
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)
        content = QWidget()
        self.setupUi(content)
        self.body_layout.addWidget(content)
        # 拉伸填充置顶
        self.body_layout.addStretch()

    # noinspection PyUnresolvedReferences
    def set_signal(self):
        super(StartExampleButtonUIActivity, self).set_signal()
        self.pushButton_8.hover_in.connect(lambda: self.pushButton_8.setIcon(self.resource.awesome_font_icon("fa.grav")))
        self.pushButton_8.hover_out.connect(lambda: self.pushButton_8.setIcon(self.resource.awesome_font_icon("fa.frown-o")))
        self.pushButton_5.clicked.connect(lambda: NormalDialogActivity(info="当前按钮是可用的").exec_())


    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(StartExampleButtonUIActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)
        self.bar.btn_bar_app_name.setText("button 实例")

        self.set_button_configure()

    def set_button_configure(self):
        """button配置"""
        self.pushButton.setText("原始按钮")
        self.pushButton.setToolTip("这是默认的按钮样式， 常用于表示取消、关闭之类不引起关注的按钮，与积极按钮生成对比效果更佳")

        self.pushButton_2.setText("积极按钮")
        self.pushButton_2.setToolTip("通常用于表示积极动作的按钮，比如确认、登录、注册、")
        self.pushButton_2.setProperty(*WidgetProperty.btn_class_normal[1])

        self.pushButton_3.setText("警告按钮")
        self.pushButton_3.setToolTip("橙黄色表示警示，用于表示操作处于危险的边缘，也用于表示异常的状态")
        self.pushButton_3.setProperty(*WidgetProperty.btn_class_warning[1])

        self.pushButton_4.setText("危险按钮")
        self.pushButton_4.setToolTip("红色警告，表示事件的严重性，常用于删除、销毁等动作")
        self.pushButton_4.setProperty(*WidgetProperty.btn_class_danger[1])

        self.pushButton_5.setText("禁止按钮")
        self.pushButton_5.setToolTip("禁止操作，表示当前按钮不可用, 如果需要添加鼠标样式，"
                                     "需要把QPushButton升格为BaseButton子类, 当前还是可以点击的，现在只是切换了样式")
        self.pushButton_5.setProperty(*WidgetProperty.btn_class_disable[1])

        self.pushButton_6.setText("带图标的按钮")
        self.pushButton_6.setIcon(self.resource.qt_icon_project_png)
        self.pushButton_6.setToolTip("给按钮添加图标")

        # button 升格为BaseButton 子类
        self.pushButton_7 = QPushButtonToBaseButton(self.pushButton_7)
        self.pushButton_7.setText("被禁用的子类按钮")
        self.pushButton_7.setIcon(self.resource.awesome_font_icon("fa.frown-o", color="red"))
        self.pushButton_7.setEnabled(False)

        self.pushButton_8.setText("可变图标的子类按钮")
        self.pushButton_8.setIcon(self.resource.awesome_font_icon("fa.frown-o"))
        self.pushButton_8 = QPushButtonToBaseButton(self.pushButton_8)
        self.pushButton_8.setProperty(*WidgetProperty.btn_class_normal[1])
        self.pushButton_8.setListenHover(True)

        self.pushButton_9.setText("鼠标来在这里一下😶")
        self.pushButton_9.setToolTip("<p>其实没那么丑, 只是布局的原因，被拉伸了</p>"
                                     "<p>具体效果可以在流式布局中查看<span style='color:blue'>StartExampleButtonActivity</span></p>")


if __name__ == '__main__':
    # 启动类
    EasyQtInit(StartExampleButtonUIActivity()).run()
