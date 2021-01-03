# coding=utf-8
"""
    create by pymu on 2020/10/23
    file: base_view.py
    页面及frame的约束类
"""
from typing import Union

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QGradient
from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle, QApplication, QGraphicsDropShadowEffect

from common.loader.resource import ResourceLoader


class BaseView(QWidget):
    """
    类包含一个静态资源文件管理器
    """
    # 静态资源管理器
    resource: ResourceLoader = ResourceLoader()

    def set_signal(self) -> None:
        """信号设置, 信号放在此处定义，方便管理哦，如此在后期调试就不用在各处翻找事件及信号"""
        ...

    def configure(self) -> None:
        """属性配置，同上统一配置方便管理"""
        ...

    def procedure(self) -> None:
        """
        初始化流程, 比如setUi、place、configure、set_signal等，
        注意先后顺序，place放置结束之后、进行页面配置（样式、属性等）、连接信号。
        """
        self.place()
        self.configure()
        self.set_signal()

    def place(self) -> None:
        """
        页面微布局,并不是所有的页面都是由Qt designer 设计而来的
        还有部分组件需要加载到页面，约定在这里编写，方便管理哦
        """
        ...

    def set_style(self, *files: str, use_old_style: bool = True) -> None:
        """
        设置样式（窗口级别），可以传入多个文件名，后面声明的样式会覆盖前面声明的样式
        :param use_old_style: 是否使用原来控件上的样式？
        :param files:  样式列表, 相对qss的路径， 如qss/index.css -> index.css
        """
        old_style = self.styleSheet() if use_old_style else ""
        self.setStyleSheet(old_style + self.resource.style_from(*files))

    def set_template(self, css_name: str):
        """
        设置主题(应用级别), 如果给窗口设置了样式set_style，那这个主题将不会生效，
        按照样式优先级应该是宽泛的优先于具体的。
        :param css_name: 样式名字
        """
        app: QApplication = QApplication.instance()
        app.setStyleSheet(self.resource.style_from(css_name))

    def get_effect_shadow(self, offset=(0, 0), radius=10,
                          color: Union[QColor, Qt.GlobalColor, QGradient] = Qt.darkGray) -> QGraphicsDropShadowEffect:
        """
        获取一个默认的阴影对象， 偏移0、半径10、颜色深灰色

        :param offset: 偏移（x， y）
        :param radius: 半径；默认10
        :param color: 颜色
        """
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(*offset)  # 偏移
        effect_shadow.setBlurRadius(radius)  # 阴影半径
        effect_shadow.setColor(color)  # 阴影颜色
        return effect_shadow

    @staticmethod
    def set_widget_shadow(shadow: QGraphicsDropShadowEffect, widget: QWidget):
        """给控件设置阴影"""
        widget.setGraphicsEffect(shadow)

    def paintEvent(self, event):
        """
        重写paintEvent,
        如此在继承widget等控件之后依然可以通过调用qss样式文件进行样式重载
        """
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, QPainter(self), self)
        super(BaseView, self).paintEvent(event)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        """解决最小化之后页面假死问题，此处参阅：https://blog.csdn.net/qq_40194498/article/details/109511055"""
        if not self.isMinimized():
            self.setAttribute(Qt.WA_Mapped)
        super(BaseView, self).showEvent(event)
