# coding=utf-8
"""
    create by pymu
    on 2020/12/10
    at 17:17
    无边框窗口阴影、拉伸、拖动
"""
from typing import Tuple

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsDropShadowEffect

from view.base_activity import BaseActivity
from view.base_view import BaseView


class FrameLessWindowHintActivity(BaseActivity):
    body_widget: QWidget = None  # 页面上的主要容器，控件应该放在这个里面
    body_layout: QHBoxLayout = None
    bar_normal: QWidget = None  # 自定义标题栏的最大化最小化及关闭按钮
    bar_close: QWidget = None
    bar_mini: QWidget = None
    bar: BaseView = None  # 顶部标题栏
    border: int = 5  # 窗口拉伸边界

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

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

    def set_signal(self):
        super(FrameLessWindowHintActivity, self).set_signal()
        if self.bar_normal:
            self.bar_normal.clicked.connect(self.change_normal)
        if self.bar_close:
            self.bar_close.clicked.connect(self.accept)
        if self.bar_mini:
            self.bar_mini.clicked.connect(self.showMinimized)

    def configure(self):
        super(FrameLessWindowHintActivity, self).configure()
        self.setMouseTracking(True)
        self.setObjectName("main_window")
        self.body_widget.setMouseTracking(True)
        self.setWindowIcon(self.resource.qt_icon_project_png)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.set_default_window_shadow()
        if self.bar_normal:
            self.bar_normal.setFont(self.button_font)
            self.bar_normal.setText(b'\xef\x80\xb1'.decode("utf-8"))
        if self.bar_mini:
            self.bar_mini.setFont(self.button_font)
            self.bar_mini.setText(b"\xef\x80\xb0".decode("utf-8"))
        if self.bar_close:
            self.bar_close.setFont(self.button_font)
            self.bar_close.setText(b"\xef\x81\xb2".decode("utf-8"))

    def set_default_window_shadow(self):
        """设置默认阴影"""
        self.set_window_shadow(self.get_default_effect_shadow(), self.body_widget)

    def get_default_effect_shadow(self) -> QGraphicsDropShadowEffect:
        """获取一个默认的阴影对象"""
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 0)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(Qt.darkGray)  # 阴影颜色
        return effect_shadow

    @staticmethod
    def set_window_shadow(shadow: QGraphicsDropShadowEffect, widget: QWidget):
        """给控件设置阴影"""
        widget.setGraphicsEffect(shadow)

    def change_normal(self):
        """
        切换到恢复窗口大小按钮,
        :return:
        """
        if not hasattr(self, "bar_normal"):
            return
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.showMaximized()  # 先实现窗口最大化
        self.bar_normal.setFont(self.button_font)
        self.bar_normal.setText(b'\xef\x80\xb2'.decode("utf-8"))
        self.bar_normal.setToolTip("恢复")  # 更改按钮提示
        self.bar_normal.disconnect()  # 断开原本的信号槽连接
        self.bar_normal.clicked.connect(self.change_max)  # 重新连接信号和槽

    def change_max(self):
        """
        切换到最大化按钮
        :return:
        """
        if not hasattr(self, "bar_normal"):
            return
        self.layout().setContentsMargins(*[self.border for _ in range(4)])
        self.showNormal()
        self.bar_normal.setFont(self.button_font)
        self.bar_normal.setText(b'\xef\x80\xb1'.decode("utf-8"))
        self.bar_normal.setToolTip("最大化")
        self.bar_normal.disconnect()  # 关闭信号与原始槽连接
        self.bar_normal.clicked.connect(self.change_normal)

    def place(self):
        """
        创建一个无边框的窗体，附带界面阴影窗口拉伸
        """
        super(FrameLessWindowHintActivity, self).place()
        main_layout = QHBoxLayout(self)
        self.body_widget = QWidget()
        self.body_layout = QHBoxLayout(self.body_widget)
        main_layout.addWidget(self.body_widget)

    def event_flag(self, event: QtGui.QMouseEvent) -> Tuple[bool, bool, bool, bool]:
        """判断鼠标是否移动到边界"""
        top = self.border < event.pos().y() < self.border + 10
        bottom = self.border + self.body_widget.height() < event.pos().y() < self.height()
        left = self.border < event.pos().x() < self.border + 10
        right = self.border + self.body_widget.width() < event.pos().x() < self.width()
        return top, bottom, left, right

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """重构鼠标点击事件"""
        super(FrameLessWindowHintActivity, self).mousePressEvent(event)
        if not self.body_widget:
            return super(FrameLessWindowHintActivity, self).mousePressEvent(event)
        top, bottom, left, right = self.event_flag(event)
        # 左键事件
        if event.button() == Qt.LeftButton:
            self.EventFlags.event_position_mouse = event.globalPos() - self.pos()
            if top and left and self.EventFlags.event_switch_border_top_left:
                self.EventFlags.event_flag_border_top_left = True
            elif top and right and self.EventFlags.event_switch_border_top_right:
                self.EventFlags.event_flag_border_top_right = True
            elif bottom and left and self.EventFlags.event_switch_border_bottom_left:
                self.EventFlags.event_flag_border_bottom_left = True
            elif bottom and right and self.EventFlags.event_switch_border_bottom_right:
                self.EventFlags.event_flag_border_bottom_right = True
            elif top and self.EventFlags.event_switch_border_top:
                self.EventFlags.event_flag_border_top = True
            elif bottom and self.EventFlags.event_switch_border_bottom:
                self.EventFlags.event_flag_border_bottom = True
            elif left and self.EventFlags.event_switch_border_left:
                self.EventFlags.event_flag_border_left = True
            elif right and self.EventFlags.event_switch_border_right:
                self.EventFlags.event_flag_border_right = True
            elif self.bar and self.body_widget and event.y() < self.bar.height() \
                    + self.body_widget.layout().getContentsMargins()[1]:
                self.EventFlags.event_flag_bar_move = True
                self.EventFlags.event_position_mouse = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标移动事件"""
        super(FrameLessWindowHintActivity, self).mouseMoveEvent(event)
        if self.body_widget:
            top, bottom, left, right = self.event_flag(event)
            if top and left and self.EventFlags.event_switch_border_top_left:
                self.setCursor(Qt.SizeFDiagCursor)
            elif bottom and right and self.EventFlags.event_switch_border_bottom_right:
                self.setCursor(Qt.SizeFDiagCursor)
            elif top and right and self.EventFlags.event_switch_border_top_right:
                self.setCursor(Qt.SizeBDiagCursor)
            elif bottom and left and self.EventFlags.event_switch_border_bottom_left:
                self.setCursor(Qt.SizeBDiagCursor)
            elif top and self.EventFlags.event_switch_border_top:
                self.setCursor(Qt.SizeVerCursor)
            elif bottom and self.EventFlags.event_switch_border_bottom:
                self.setCursor(Qt.SizeVerCursor)
            elif left and self.EventFlags.event_switch_border_left:
                self.setCursor(Qt.SizeHorCursor)
            elif right and self.EventFlags.event_switch_border_right:
                self.setCursor(Qt.SizeHorCursor)
            elif Qt.LeftButton and self.EventFlags.event_flag_bar_move:
                self.move(event.globalPos() - self.EventFlags.event_position_mouse)
            else:
                self.setCursor(Qt.ArrowCursor)
            # 窗口拉伸
            if self.EventFlags.event_flag_border_top_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y() + event.pos().y(),
                                 self.width() - event.pos().x(), self.height() - event.pos().y())
            elif self.EventFlags.event_flag_border_bottom_right:
                self.resize(event.pos().x(), event.pos().y())

            elif self.EventFlags.event_flag_border_bottom_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y(),
                                 self.width() - event.pos().x(), event.pos().y())

            elif self.EventFlags.event_flag_border_top_right:
                self.setGeometry(self.geometry().x(), self.geometry().y() + event.pos().y(),
                                 event.pos().x(), self.height() - event.pos().y())
            elif self.EventFlags.event_flag_border_right:
                self.resize(event.pos().x(), self.height())
            elif self.EventFlags.event_flag_border_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y(),
                                 self.width() - event.pos().x(), self.height())
            elif self.EventFlags.event_flag_border_bottom:
                self.resize(self.width(), event.pos().y())
            elif self.EventFlags.event_flag_border_top:
                self.setGeometry(self.geometry().x(), self.geometry().y() + event.pos().y(),
                                 self.width(), self.height() - event.pos().y())

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标释放事件"""
        super(FrameLessWindowHintActivity, self).mouseReleaseEvent(event)
        self.EventFlags.event_flag_bar_move = False
        self.EventFlags.event_flag_border_left = False
        self.EventFlags.event_flag_border_right = False
        self.EventFlags.event_flag_border_top = False
        self.EventFlags.event_flag_border_bottom = False
        self.EventFlags.event_flag_border_top_left = False
        self.EventFlags.event_flag_border_top_right = False
        self.EventFlags.event_flag_border_bottom_left = False
        self.EventFlags.event_flag_border_bottom_right = False
