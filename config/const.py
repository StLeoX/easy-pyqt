# coding=utf-8
"""
    create by pymu on 2020/10/23
    package: .const.py
    project: base_qt_application
    这里一般保存应用常使用的固定常量，如文件的相对路径
    常量集合
"""
import os

__class_path__ = os.path.abspath(os.path.dirname(__file__))
__root_path__ = os.path.abspath(os.path.join(__class_path__, os.path.pardir))

from typing import Tuple


class Config:
    """
    属性项
    """
    # 应用名称
    app_name = "example app"
    # 唯一启动标识 todo 获取设备号
    unique_name = "unique_6948510_u_8"

    @property
    def root_path(self) -> str:
        """
        项目根路径
        :return:
        """
        return __root_path__

    @property
    def resource_path(self):
        """
        资源文件夹
        :return:
        """
        return self.link(self.root_path, "resource", not_exists_create=True)

    @property
    def img_path(self):
        """
        img 文件夹
        :return:
        """
        return self.link(self.resource_path, "img", not_exists_create=True)

    @property
    def qss_path(self):
        """
        样式文件夹
        :return:
        """
        return self.link(self.resource_path, "qss", not_exists_create=True)

    @property
    def log_path(self):
        """
        log
        :return:
        """
        return self.link(self.root_path, "log", not_exists_create=True)

    @staticmethod
    def link(source: str, point: str, not_exists_create=False) -> str:
        """
        :param not_exists_create: 不存在创建
        :param source: 上级路径
        :param point: 连接路径
        :return:
        """
        return Config.path_exists(os.path.join(source, point)) if not_exists_create else os.path.join(source, point)

    @staticmethod
    def path_exists(path: str) -> str:
        """
        不存在则创建
        :param path:
        :return:
        """
        if not os.path.exists(path) and "." not in path:
            os.makedirs(path)
        return path

    def get_user_desktop_path(self) -> str:
        """
        返回桌面
        :return:
        """
        return self.link(os.path.expanduser('~'), "Desktop")


class WidgetProperty:
    """空间属性样式对应表 按照字母排序 详细效果图请参阅：https://py-mu.github.io/easy-pyqt/#/ui/readme"""

    # 容器
    box_class_primary = ("原始容器", ("box_class_primary", "true"))  # note: 原始容器

    # 使用元组放置属性筛选描述
    btn_class_primary = ("原始按钮，不被注意的按钮如取消", ("btn_class_primary", "true"))  # note: 原始按钮
    btn_class_normal = ("常规按钮，容易被注意到且表示积极的按钮", ("btn_class_normal", "true"))  # note: 常规按钮()
    btn_class_warning = ("警告按钮，橙黄色带有冲击性的颜色，具有警告意味，但是无关紧要", ("btn_class_warning", "true"))  # note: 警告按钮()
    btn_class_danger = ("危险按钮，红色带有冲击性的颜色, 表示动作很危险， 具有强烈警告", ("btn_class_danger", "true"))  # note: 危险按钮()
    btn_class_disable = ("禁用按钮，通常用于表示，当前动作不可用", ("btn_class_disable", "true"))  # note: 禁用按钮()
    btn_class_success = ("成功按钮，通常用于表示，正确、可用", ("btn_class_success", "true"))  # note: 成功按钮()

    # 复选框
    checkbox_class_normal = ("常用的复选框", ("checkbox_class_normal", "true"))  # note: 常用的复选框()
    checkbox_class_primary = ("原生的复选框", ("checkbox_class_primary", "true"))  # note: 原生的复选框()

    # 单选框
    radio_btn_class_primary = ("原生的复选框", ("radio_btn_class_primary", "true"))  # note: 原生的单选框()
    radio_btn_class_normal = ("原生的复选框", ("radio_btn_class_normal", "true"))  # note: 原生的单选框()

    # 其他
    border_class_red = ("红色边框一般用于警示，输入错误", ("border_class_red", "true"))  # note: 红色边框()

    @staticmethod
    def get_style(name: str, valid=True) -> Tuple[str, Tuple[str, str]]:
        """
        通过属性名筛选样式

        :param valid: 是否有效
        :param name: 属性名称
        :return: 如果有则返回，没有则返回默认的
        """
        the_property = "默认属性", ("property_name", "true")
        if not name:
            return the_property
        name = str(name)
        if hasattr(WidgetProperty, name):
            the_property = getattr(WidgetProperty, name)
            the_property = the_property[0], the_property[1][0], valid
        return the_property
