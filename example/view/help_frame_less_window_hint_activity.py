# coding=utf-8
"""
    create by pymu
    on 2020/12/18
    at 11:26
    如何开发自定义边框窗口代码
"""

import sys
from typing import Tuple

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QHBoxLayout, QGraphicsDropShadowEffect, QPushButton

from common.base.base_view import BaseView


class BaseActivity(QDialog):
    body_widget: QWidget = None  # 页面上的主要容器，控件应该放在这个里面
    body_layout: QHBoxLayout = None
    bar_normal: QPushButton = None  # 自定义标题栏的最大化最小化及关闭按钮
    bar_close: QPushButton = None
    bar_mini: QPushButton = None
    bar: BaseView = None  # 顶部标题栏
    border_width: int = 5  # 窗口拉伸边界

    class EventFlags:
        """扳机状态，用于判定鼠标事件是否触发"""
        event_flag_bar_move = False
        event_flag_border_left = False
        event_flag_border_right = False
        event_flag_border_top = False
        event_flag_border_bottom = False
        event_flag_border_top_left = False
        event_flag_border_top_right = False
        event_flag_border_bottom_left = False
        event_flag_border_bottom_right = False

        # 不得已以为拉伸闪烁问题
        # 只能设定固定方向的拉伸能够使用
        # 当然全部打开也是可以的，只是存在闪烁问题
        # PC端的应用大部分存在这个问题，所以用也可以
        event_switch_border_left = False
        event_switch_border_right = True
        event_switch_border_top = False
        event_switch_border_bottom = True
        event_switch_border_top_left = False
        event_switch_border_top_right = False
        event_switch_border_bottom_left = False
        event_switch_border_bottom_right = True

        event_position_mouse: QPoint = None

        def __init__(self):
            """进行实例化，不同页面窗体，不同的开关及状态"""

    def __init__(self):
        super().__init__()
        self.event_flags = self.EventFlags()
        self.place()
        self.configure()
        self.set_signal()

    def set_signal(self):
        """页面信号"""

    def place(self):
        """页面布局"""
        self.body_widget = QWidget()
        layout = QHBoxLayout(self)
        layout.addWidget(self.body_widget)

    def configure(self):
        """页面配置"""
        self.resize(300, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.body_widget.setStyleSheet("background: #fff")
        self.bar = self.body_widget
        effect_shadow = QGraphicsDropShadowEffect()
        effect_shadow.setOffset(0, 0)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(Qt.darkGray)  # 阴影颜色
        self.body_widget.setGraphicsEffect(effect_shadow)
        self.body_widget.setMouseTracking(True)
        self.setMouseTracking(True)

    def event_flag(self, event: QtGui.QMouseEvent) -> Tuple[bool, bool, bool, bool]:
        """判断鼠标是否移动到边界"""
        top = self.border_width < event.pos().y() < self.border_width + 10
        bottom = self.border_width + self.body_widget.height() < event.pos().y() < self.height()
        left = self.border_width < event.pos().x() < self.border_width + 10
        right = self.border_width + self.body_widget.width() < event.pos().x() < self.width()
        return top, bottom, left, right

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """重构鼠标点击事件"""
        if not self.body_widget:
            return super(BaseActivity, self).mousePressEvent(event)
        top, bottom, left, right = self.event_flag(event)
        body_widget_margins = 0 if not self.body_widget.layout() else self.body_widget.layout().getContentsMargins()[1] * 2
        body_widget_spacing = 0 if not self.body_widget.layout() else self.body_widget.layout().spacing()
        # 左键事件
        if event.button() == Qt.LeftButton:
            self.event_flags.event_position_mouse = event.globalPos() - self.pos()
            if top and left and self.event_flags.event_switch_border_top_left:
                self.event_flags.event_flag_border_top_left = True
            elif top and right and self.event_flags.event_switch_border_top_right:
                self.event_flags.event_flag_border_top_right = True
            elif bottom and left and self.event_flags.event_switch_border_bottom_left:
                self.event_flags.event_flag_border_bottom_left = True
            elif bottom and right and self.event_flags.event_switch_border_bottom_right:
                self.event_flags.event_flag_border_bottom_right = True
            elif top and self.event_flags.event_switch_border_top:
                self.event_flags.event_flag_border_top = True
            elif bottom and self.event_flags.event_switch_border_bottom:
                self.event_flags.event_flag_border_bottom = True
            elif left and self.event_flags.event_switch_border_left:
                self.event_flags.event_flag_border_left = True
            elif right and self.event_flags.event_switch_border_right:
                self.event_flags.event_flag_border_right = True
            elif self.bar and self.body_widget and event.y() < self.bar.height() + self.border_width \
                    + body_widget_margins + body_widget_spacing:
                self.event_flags.event_flag_bar_move = True
                self.event_flags.event_position_mouse = event.globalPos() - self.pos()
        return super(BaseActivity, self).mousePressEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标移动事件"""
        super(BaseActivity, self).mouseMoveEvent(event)
        if self.body_widget:
            top, bottom, left, right = self.event_flag(event)
            if top and left and self.event_flags.event_switch_border_top_left:
                self.setCursor(Qt.SizeFDiagCursor)
            elif bottom and right and self.event_flags.event_switch_border_bottom_right:
                self.setCursor(Qt.SizeFDiagCursor)
            elif top and right and self.event_flags.event_switch_border_top_right:
                self.setCursor(Qt.SizeBDiagCursor)
            elif bottom and left and self.event_flags.event_switch_border_bottom_left:
                self.setCursor(Qt.SizeBDiagCursor)
            elif top and self.event_flags.event_switch_border_top:
                self.setCursor(Qt.SizeVerCursor)
            elif bottom and self.event_flags.event_switch_border_bottom:
                self.setCursor(Qt.SizeVerCursor)
            elif left and self.event_flags.event_switch_border_left:
                self.setCursor(Qt.SizeHorCursor)
            elif right and self.event_flags.event_switch_border_right:
                self.setCursor(Qt.SizeHorCursor)
            elif Qt.LeftButton and self.event_flags.event_flag_bar_move:
                self.move(event.globalPos() - self.event_flags.event_position_mouse)
            else:
                self.setCursor(Qt.ArrowCursor)
            # 窗口拉伸
            if self.event_flags.event_flag_border_top_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y() + event.pos().y(),
                                 self.width() - event.pos().x(), self.height() - event.pos().y())
            elif self.event_flags.event_flag_border_bottom_right:
                self.resize(event.pos().x(), event.pos().y())

            elif self.event_flags.event_flag_border_bottom_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y(),
                                 self.width() - event.pos().x(), event.pos().y())

            elif self.event_flags.event_flag_border_top_right:
                self.setGeometry(self.geometry().x(), self.geometry().y() + event.pos().y(),
                                 event.pos().x(), self.height() - event.pos().y())
            elif self.event_flags.event_flag_border_right:
                self.resize(event.pos().x(), self.height())
            elif self.event_flags.event_flag_border_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y(),
                                 self.width() - event.pos().x(), self.height())
            elif self.event_flags.event_flag_border_bottom:
                self.resize(self.width(), event.pos().y())
            elif self.event_flags.event_flag_border_top:
                self.setGeometry(self.geometry().x(), self.geometry().y() + event.pos().y(),
                                 self.width(), self.height() - event.pos().y())

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标释放事件"""
        super(BaseActivity, self).mouseReleaseEvent(event)
        self.event_flags.event_flag_bar_move = False
        self.event_flags.event_flag_border_left = False
        self.event_flags.event_flag_border_right = False
        self.event_flags.event_flag_border_top = False
        self.event_flags.event_flag_border_bottom = False
        self.event_flags.event_flag_border_top_left = False
        self.event_flags.event_flag_border_top_right = False
        self.event_flags.event_flag_border_bottom_left = False
        self.event_flags.event_flag_border_bottom_right = False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BaseActivity()
    window.show()
    sys.exit(app.exec_())
