# coding=utf-8
"""
    create by pymu
    on 2020/12/30
    at 8:47
"""
import typing

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal, QEvent, QObject
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton

from common.decorator.hook import set_instance_method
from config.const import WidgetProperty


class BaseButton(QPushButton):
    """
    button 子类, 重构鼠标事件，在设置disable之后的鼠标游标，
    此类仅是简单子类，如有功能冲突，请使用QPushButton
    """
    # 鼠标经过事件, 需要设置可监听才可用
    hover_in: pyqtSignal = pyqtSignal()
    hover_out: pyqtSignal = pyqtSignal()

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        self.disable = False
        self.hover_listen_able = False
        self.property_name = ""

    def setListenHover(self, able: bool):
        """是否监听鼠标经过事件"""
        self.hover_listen_able = able
        if able:
            self.installEventFilter(self)
        else:
            self.removeEventFilter(self)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """重构点击事件"""
        if self.disable:
            return
        return QPushButton.mousePressEvent(self, event)

    # noinspection PyUnresolvedReferences
    def eventFilter(self, widget: QObject, event: QEvent) -> bool:
        """事件过滤器"""
        if widget == self and self.hover_listen_able:
            if event.type() == QEvent.Enter:
                self.hover_in.emit()
            elif event.type() == QEvent.Leave:
                self.hover_out.emit()
        return QPushButton.eventFilter(self, widget, event)

    def setProperty(self, name: str, value: typing.Any) -> bool:
        """在属性发生变化时刷新样式"""
        if not self.property_name:
            self.property_name = value
        result = QPushButton.setProperty(self, name, value)
        self.style().polish(self)
        return result

    def setDisabled(self, disable: bool) -> None:
        """
        设置按钮无用, 当且仅当设置状态与当前状态不一致时才会改变
        样式应该设置无效之前设定
        """
        if disable and not self.disable:
            self.property_name = self.property("property_name")
            self.setCursor(QCursor(Qt.ForbiddenCursor))
            self.setProperty(*WidgetProperty.btn_class_disable[1])
        else:
            self.setProperty(*WidgetProperty.get_style(self.property_name)[1])
            self.unsetCursor()
        self.disable = disable

    def setEnabled(self, able: bool) -> None:
        """翻转之后便是disable"""
        self.setDisabled(not able)


def QPushButtonToBaseButton(button: QPushButton) -> BaseButton:
    """转换到BaseButton"""
    button.disable = False
    button.hover_listen_able = False
    button.setMouseTracking(True)
    button.property_name = ""
    # button_son = BaseButton()
    # setattr(QPushButton, "hover_in", button_son.hover_in)
    # setattr(QPushButton, "hover_out", button_son.hover_out)
    setattr(QPushButton, "hover_in", pyqtSignal())
    setattr(QPushButton, "hover_out", pyqtSignal())
    button.set_instance_method = set_instance_method
    button.set_instance_method(button, BaseButton.setEnabled)
    button.set_instance_method(button, BaseButton.setDisabled)
    button.set_instance_method(button, BaseButton.setProperty)
    button.set_instance_method(button, BaseButton.mousePressEvent)
    button.set_instance_method(button, BaseButton.eventFilter)
    button.set_instance_method(button, BaseButton.setListenHover)
    print(button.__dir__)
    return button
