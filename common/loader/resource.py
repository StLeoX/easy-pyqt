# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .loader.py
    project:
    静态资源加载， 避免重复进行实例化
"""
import threading

import qtawesome
from PyQt5 import QtGui
from PyQt5.QtGui import qGray, qRgba, qAlpha

from common.decorator.lazy_property import Lazy
from config import const


class ResourceLoader:
    """
    静态资源加载器，可以使用 lazy 加载图像
    实现单例模式
    """

    # 单例添加线程锁
    _instance_lock = threading.Lock()
    img_path = const.Config().img_path

    def __new__(cls, *args, **kwargs):
        """
        实现单例
        :param args:
        :param kwargs:
        """
        if not hasattr(ResourceLoader, "_instance"):
            with ResourceLoader._instance_lock:
                if not hasattr(ResourceLoader, "_instance"):
                    ResourceLoader._instance = object.__new__(cls)
        return ResourceLoader._instance

    def render_icon(self, name: str, convert=False) -> QtGui.QIcon:
        """
        渲染 icon 对象
        :param convert: 是否需要灰度转换
        :param name: 文件名
        :return:
        """
        path = const.Config.link(self.img_path, name)
        return self.__render_icon_by_path(path) \
            if not convert else self.__render_icon_by_path_convert(path)

    @staticmethod
    def __render_icon_by_path(path: str) -> QtGui.QIcon:
        """
        通过路径渲染出一个icon图像
        :param path: 图像地址
        :return: QtGui.QIcon
        """
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.On)
        return icon

    @staticmethod
    def __render_icon_by_path_convert(path: str) -> QtGui.QIcon:
        """
        返回灰度icon
        :param path:
        :return:
        """
        icon = QtGui.QIcon()
        image = QtGui.QPixmap(path).toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = image.pixel(x, y)
                gray = qGray(color)
                image.setPixel(x, y, qRgba(gray, gray, gray, qAlpha(color)))
        icon.addPixmap(QtGui.QPixmap.fromImage(image), QtGui.QIcon.Normal, QtGui.QIcon.On)
        return icon

    @staticmethod
    def make_font(size: int, weight: int = 2, family: str = "微软雅黑") -> QtGui.QFont:
        """
        创建一个字体，如此不必重复的
        实例化-设置-调用
        :param size: 大小
        :param weight: 权重
        :param family: 字体族
        :return:
        """
        font = QtGui.QFont()
        font.setWeight(weight)
        font.setFamily(family)
        font.setPointSize(size)
        return font

    @staticmethod
    def style_from(*css_name: str) -> str:
        """
        获取qss文件夹下的样式加载到容器中,
        样式优先级是由调用先后决定，
        即 先使用表[程序声明] < 后使用
        :param css_name: css 文件名, 可以是多个的
        :return: str 样式字符串
        """
        style_str = ""
        for file_name in css_name:
            with open(const.Config.link(
                    const.Config().qss_path,
                    file_name),
                    encoding="utf-8") as f:
                style_str += f.read()
        return style_str

    @staticmethod
    def awesome_font_icon(font_str: str, color="white") -> QtGui.QIcon:
        """
        字体图标,临时使用，
        重复调用建议使用方法生成
        :param color: 显示的颜色，是一个颜色描述单词，
        或者十六进制色，如 '#666' default ’white‘
        :param font_str 图标标识 如：'fa5.file-excel'
        :return:
        """
        return qtawesome.icon(font_str, color=color)

    # --------------------------------
    # |    以下是常用的图片/字体对象     |
    # ________________________________

    @Lazy
    def qt_icon_project_ico(self):
        """
        项目图标-icon
        :return:
        """
        return self.render_icon("icon.ico")

    @Lazy
    def qt_icon_project_png(self) -> QtGui.QIcon:
        """
        程序图标-png
        :return:
        """
        return self.render_icon("icon.png")

    @Lazy
    def qt_font_10(self) -> QtGui.QFont:
        """
        微软雅黑 10
        :return:
        """
        return self.make_font(10)

    @Lazy
    def qt_font_11(self) -> QtGui.QFont:
        """
        微软雅黑 11
        :return:
        """
        return self.make_font(11)

    @Lazy
    def qt_font_17(self) -> QtGui.QFont:
        """
        微软雅黑 17
        :return:
        """
        return self.make_font(17)
