# coding=utf-8
"""
    create by pymu
    on 2020/12/16
    at 11:19
     一般弹窗
"""
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from view.activity.activity_frame_less_window_hint import FrameLessWindowHintActivity
from view.uipy.dialog_info_waring_error import Ui_Form


class NormalDialogActivity(FrameLessWindowHintActivity, Ui_Form):

    def __init__(self):
        """一般弹窗, 继承自无边框窗体"""
        super().__init__()
        self.procedure()

    def place(self):
        """需要在父类界面渲染之前重构窗体"""
        main_layout = QHBoxLayout(self)
        self.body_widget = QWidget()
        self.setupUi(self.body_widget)
        main_layout.addWidget(self.body_widget)
        self.body_layout = self.body_widget.layout()
        super(NormalDialogActivity, self).place()

    def configure(self):
        self.bar_close = self.btn_bar_close
        super(NormalDialogActivity, self).configure()
        self.resize(300, 200)
        self.set_style("dialog_normal.css")
        self.btn_bar_app_logo.setIcon(self.resource.qt_icon_project_png)
        self.btn_bar_title.setText("操作异常")
        self.btn_dialog_yes.setText("确认")
        self.btn_dialog_no.setHidden(True)
        self.EventFlags.event_switch_border_bottom = False
        self.EventFlags.event_switch_border_right = False
        self.EventFlags.event_switch_border_bottom_right = False
