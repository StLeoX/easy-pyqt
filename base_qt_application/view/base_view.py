# coding=utf-8
"""
    create by pymu on 2020/10/23
    file: base_view.py
    页面及frame的约束类
"""
import abc

from PyQt5.QtWidgets import QWidget

from common.loader.resource import ResourceLoader


class BaseView(QWidget):
    """
    类包含一个静态资源文件管理器
    """
    # 静态资源管理器
    resource: ResourceLoader = ResourceLoader()

    @abc.abstractmethod
    def set_signal(self):
        """信号设置"""
        ...

    @abc.abstractmethod
    def configure(self):
        """属性配置"""
        ...

    def procedure(self):
        """
        初始化流程, 比如setUi、place、configure、set_signal等
        :return:
        """
        ...

    def place(self):
        """
        页面微布局,并不是所有的页面都是由Qt designer 设计而来的
        还有部分组件需要加载到页面，约定在这里编写，方便管理哦
        :return:
        """
        ...

    def set_style(self, *files: str, use_old_style: bool = False):
        """
        设置样式，可以传入多个文件名，后面声明的样式会覆盖前面声明的样式
        :param use_old_style: 是否使用原来控件上的样式？
        :param files:  样式列表, 相对qss的路径， 如qss/index.css -> index.css
        :return:
        """
        old_style = ""
        if use_old_style:
            old_style = self.styleSheet() or ""
        self.setStyleSheet(old_style + self.resource.style_from(*files))
