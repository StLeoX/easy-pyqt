# coding=utf-8
"""
    create by pymu on 2020/10/23
    file: base_view.py
    页面及frame的约束类
"""

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle, QApplication

from common.loader.resource import ResourceLoader


class BaseView(QWidget):
    """
    类包含一个静态资源文件管理器
    """
    # 静态资源管理器
    resource: ResourceLoader = ResourceLoader()

    def set_signal(self) -> None:
        """信号设置"""
        ...

    def configure(self) -> None:
        """属性配置"""
        ...

    def procedure(self) -> None:
        """
        初始化流程, 比如setUi、place、configure、set_signal等
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

    def paintEvent(self, event):
        """
        重写paintEvent,
        如此在继承widget等控件之后依然可以通过调用qss样式文件进行样式重载
        """
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, QPainter(self), self)
        super(BaseView, self).paintEvent(event)
