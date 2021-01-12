# coding=utf-8
"""
    create by pymu on 2020/10/23
    package: .const.py
    project: base_qt_application

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
    app_name = "example app"

    person_sg = 0
    person_gb = 1

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

    # get shadow img path
    @property
    def shadow_path(self):
        """
        获取边框阴影的目录所在（此处已经指定了上级目录img所在）
        :return: shadow path
        """
        return self.link(self.img_path, "shadow")

    def get_shadow_path(self, name: str) -> str:
        """
        获取阴影
        :param name:
        :return:
        """
        return self.link(self.shadow_path, name)

    def get_user_desktop_path(self) -> str:
        """
        返回桌面
        :return:
        """
        return self.link(os.path.expanduser('~'), "Desktop")

    @property
    def oracle_path(self):
        """
        :return:
        """
        return self.link(self.resource_path, "oracle_client\\instantclient_19_3")



class WidgetProperty:
    """空间属性样式对应表 详细效果图请参阅：https://github.com/py-mu/easy-pyqt"""

    # 使用元组放置属性筛选描述
    btn_class_primary = ("原始按钮，不被注意的按钮如取消", ("property_name", "btn_class_primary"))  # note: 原始按钮
    btn_class_normal = ("常规按钮，容易被注意到且表示积极的按钮", ("property_name", "btn_class_normal"))  # note: 常规按钮()
    btn_class_warning = ("警告按钮，橙黄色带有冲击性的颜色，具有警告意味，但是无关紧要", ("property_name", "btn_class_warning"))  # note: 警告按钮()
    btn_class_danger = ("危险按钮，红色带有冲击性的颜色, 表示动作很危险， 具有强烈警告", ("property_name", "btn_class_danger"))  # note: 危险按钮()
    btn_class_disable = ("禁用按钮，通常用于表示，当前动作不可用", ("property_name", "btn_class_disable"))  # note: 禁用按钮()
    btn_class_success = ("成功按钮，通常用于表示，正确、可用", ("property_name", "btn_class_success"))  # note: 成功按钮()

    checkbox_class_normal = ("常用的复选框", ("property_name", "checkbox_class_normal"))  # note: 常用的复选框()
    checkbox_class_primary = ("原生的复选框", ("property_name", "checkbox_class_primary"))  # note: 原生的复选框()

    radio_btn_class_primary = ("原生的复选框", ("property_name", "radio_btn_class_primary"))  # note: 原生的单选框()
    radio_btn_class_normal = ("原生的复选框", ("property_name", "radio_btn_class_normal"))  # note: 原生的单选框()

    border_class_red = ("红色边框一般用于警示，输入错误", ("property_name", "border_class_red"))  # note: 红色边框()

    @staticmethod
    def get_style(name: str) -> Tuple[str, Tuple[str, str]]:
        """
        通过属性名筛选样式

        :param name: 属性名称
        :return: 如果有则返回，没有则返回默认的
        """
        default_property = "默认属性", ("property_name", "")
        if not name:
            return default_property
        if hasattr(WidgetProperty, str(name)):
            return getattr(WidgetProperty, str(name))
        return default_property
