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
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout

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
        return super(BaseButton, self).mousePressEvent(event)

    # noinspection PyUnresolvedReferences
    def eventFilter(self, widget: QObject, event: QEvent) -> bool:
        """事件过滤器"""
        if widget == self and self.hover_listen_able:
            if event.type() == QEvent.Enter:
                self.hover_in.emit()
            elif event.type() == QEvent.Leave:
                self.hover_out.emit()
        return super(BaseButton, self).eventFilter(widget, event)

    def setProperty(self, name: str, value: typing.Any) -> bool:
        """在属性发生变化时刷新样式"""
        if not self.property_name:
            self.property_name = value
        result = super(BaseButton, self).setProperty(name, value)
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
    """
    将父类升格到派生子类BaseButton, 通过反射注入的方式会存在很多问题，
    使用对象实例化把主要的数据拷贝给新对象
    注意：在父类上绑定的操作都将会会失效（替换控件的方法也可能会出现问题）
    """
    parent_div: QWidget = button.parent()
    parent_layout = parent_div.layout()
    if not parent_div or not parent_layout:
        raise ValueError("没有找到 button 的父级容器或布局")
    new_button = BaseButton()
    new_button.setObjectName(button.objectName())
    new_button.setEnabled(button.isEnabled())
    new_button.setToolTip(button.toolTip())
    new_button.setIcon(button.icon())
    new_button.setText(button.text())
    new_button.setMouseTracking(button.hasMouseTracking())
    new_button.setCursor(button.cursor())
    index = parent_layout.indexOf(button)
    if isinstance(parent_layout, QHBoxLayout) or isinstance(parent_layout, QVBoxLayout):
        alignment = parent_layout.itemAt(index).alignment()
        parent_layout.insertWidget(index, new_button, alignment=alignment)
        parent_layout.removeWidget(button)
    elif isinstance(parent_layout, QGridLayout):
        pos = parent_layout.getItemPosition(index)
        parent_layout.addWidget(new_button, pos[0], pos[1])
    else:
        items = [parent_layout.itemAt(i).widget() for i in range(parent_layout.count())]
        for i in items:
            parent_layout.removeWidget(i)
        items.remove(button)
        items.insert(index, new_button)
        for i in items:
            parent_layout.addWidget(i)
    return new_button
