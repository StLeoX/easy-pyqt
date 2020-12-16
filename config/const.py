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


class Config:
    """
    属性项
    """
    app_name = "example app"

    person_sg = 0
    person_gb = 1

    # 唯一启动标识
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
