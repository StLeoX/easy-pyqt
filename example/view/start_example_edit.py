# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：输入框
"""
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator, QFontMetrics, QFont
from PyQt5.QtWidgets import QLineEdit, QTextEdit

from common.base.highlight import EditHighLighter
from common.base.launch import EasyQtInit
from config.const import WidgetProperty
from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.frame.frame_bar_demo0 import FrameBarDemo0


# noinspection PyAttributeOutsideInit
class TestActivity(FrameLessWindowHintActivity):
    """入框样式"""

    # ip校验
    ipValidator = QRegExpValidator(QRegExp('^((2[0-4]\d|25[0-5]|\d?\d|1\d{2})\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'))

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
        # 设置清空按钮
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("只有输入123才可以通过")
        self.line_edit.setClearButtonEnabled(True)
        self.body_layout.addWidget(self.line_edit)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText("只能输入ip")
        self.line_edit1.setValidator(self.ipValidator)
        self.line_edit1.setClearButtonEnabled(True)
        self.body_layout.addWidget(self.line_edit1)

        pass_wd = QLineEdit()
        pass_wd.setPlaceholderText("请输入密码")
        pass_wd.setEchoMode(QLineEdit.Password)
        pass_wd.setClearButtonEnabled(True)
        self.body_layout.addWidget(pass_wd)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("长文本输入框")
        self.body_layout.addWidget(self.text_edit)

        # 拉伸填充置顶
        self.body_layout.addStretch()

    # noinspection PyUnresolvedReferences
    def set_signal(self):
        super(TestActivity, self).set_signal()
        self.line_edit.editingFinished.connect(self.check_input)

    def check_input(self):
        """检查输入是否正确"""
        text = self.line_edit.text()
        if text != '123':
            self.line_edit.setProperty(*WidgetProperty.border_class_red[1])
            self.line_edit.style().polish(self.line_edit)
        else:
            self.line_edit.setProperty(*WidgetProperty.btn_class_primary[1])
            self.line_edit.style().polish(self.line_edit)

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        self.bar_close = self.bar.btn_bar_close
        self.bar_mini = self.bar.btn_bar_min
        self.bar_normal = self.bar.btn_bar_normal
        super(TestActivity, self).configure()
        self.bar.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)
        # EditHighLighter(self.text_edit)
        self.high_lighter = EditHighLighter(self.text_edit)
        self.high_lighter.set_tab_size()
        # self.high_lighter.key_word = EditHighLighter.SQL_KEY
        # self.high_lighter.builtins = EditHighLighter.SQL_BUILTINS
        # self.high_lighter.constants = EditHighLighter.SQL_CONSTANTS


if __name__ == '__main__':
    # 启动类
    EasyQtInit(TestActivity()).run()
