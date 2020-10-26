# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .base_activity.py
    project:
"""

from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt, QRect
from PyQt5.QtGui import QPainter, QPixmap, QPainterPath, QBrush, QMouseEvent
from PyQt5.QtWidgets import QDialog, QWidget

from common.util.async_thread import FuncThread, ResponseData
from common.util.logger import Logger
from config.const import Config
from view.activity.dialog import waiting_dialog, message_ok, error_dialog
from view.base_view import BaseView


class BaseActivity(QDialog, BaseView):
    # 自定义标题栏的最大化最小化
    bar_normal = None

    # 自定义标题栏组件
    bar = None

    # 窗口拖动位置列表
    _right_rect = []
    _bottom_rect = []
    _corner_rect = []

    # 拖拽flag
    move_DragPosition = None

    # 窗口拉伸鼠标可以检测的宽度
    _padding = 5
    # 阴影宽度
    SHADOW_WIDTH = 5
    # 扳机默认值
    _move_drag = False
    _corner_drag = False
    _bottom_drag = False
    _right_drag = False

    #
    #

    def __init__(self, flags=None, *args, **kwargs):
        """
        自定义窗口，*他具有以下属性或者功能*：
            - 属性：logger    日志记录
            - 属性：resource  静态资源管理
            - 属性：waiting_dialog 弹出层
            - 属性：message_text 默认的消息提示
            - 属性：error_dialog_str 默认的错误提示
            - 属性：default_thread 通用线程
            - 属性：bar_normal 最大最小化按钮，由子类赋值
            - 属性：bar        标题栏，由子类赋值
            - 功能：拖动窗体，需把控件赋值给 bar 作为载体
            - 功能：无边框，实例化子类时，其边距应设置为5
            - 功能：最大最小化，需把控件赋值给 bar_normal 作为载体
            - 功能：窗体拉伸，需要设定 self.setMouseTracking(True)
            - 功能：文件拖拽，需要开启
        """
        super().__init__(flags, *args, **kwargs)
        self.default_func: FuncThread = FuncThread()  # 默认的执行线程
        self.waiting_dialog = waiting_dialog()  # 默认的遮罩层
        self.logger = Logger()
        self.config = Config()

    def configure(self):
        """
        如果有用到两个样式表，则需要把两个样式表,都添加，
        activity的配置方法，这里设置了基本的页面属性\n
        如果需要父类的方法，则需要在重构的子类方法之中添加：\n
        >>> BaseActivity.configure(self)

        :return: None
        """
        self.resize(1047, 680)
        self.setWindowTitle("应用名称")
        self.set_style("common.css")
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint |
            Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint |
            Qt.WindowMaximizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(self.resource.qt_icon_project_ico)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def place(self):
        """
            test_layout = QtWidgets.QHBoxLayout(self)
        """
        ...

    def set_signal(self):
        """
        设置信号，如果需要父类信号，那在重构的子类方法中\n：
        >>> BaseActivity.set_signal(self)

        :return: None
        """
        if self.bar_normal:
            self.bar_normal.clicked.connect(lambda: BaseActivity.change_normal(self))
            # 执行失败时，通信频道移交给错误弹窗
        self.default_func.thread_error_signal.connect(self.error_dialog)
        self.default_func.thread_signal.connect(self.do_nothing)

    def do_nothing(self, *args, **kwargs):
        """
        链接到无执行的方法上，
        防止线程在错误的时间通信
        :param args: args
        :param kwargs: kwargs
        :return: none
        """
        ...

    def resizeEvent(self, _event):
        """
        自定义窗口调整大小事件
        采用三个列表生成式生成三个列表, 用以保存一个鼠标可以拖动的范围
        :param _event:
        :return:
        """
        if not self.bar:
            return
        # 获取右侧边界
        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(self.bar.height(), self.height() + self._padding)]
        # 下边界
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() + self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]
        # 右下边界
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                             for y in range(self.height() - self._padding, self.height() + 1)]

    @staticmethod
    def change_normal(self: QWidget):
        """
        切换到恢复窗口大小按钮,
        链接的方法为：
        >>> lambda: BaseActivity.change_normal(self)
        :return:
        """
        if not hasattr(self, "bar_normal"):
            return
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.showMaximized()  # 先实现窗口最大化
        self.bar_normal.setText(b'\xef\x80\xb2'.decode("utf-8"))
        self.bar_normal.setToolTip("恢复")  # 更改按钮提示
        self.bar_normal.disconnect()  # 断开原本的信号槽连接
        self.bar_normal.clicked.connect(lambda: BaseActivity.change_max(self))  # 重新连接信号和槽

    @staticmethod
    def change_max(self: QWidget):
        """
        切换到最大化按钮
        :return:
        """
        if not hasattr(self, "bar_normal"):
            return
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.showNormal()
        self.bar_normal.setText(b'\xef\x80\xb1'.decode("utf-8"))
        self.bar_normal.setToolTip("最大化")
        # 关闭信号与原始槽连接
        self.bar_normal.disconnect()
        self.bar_normal.clicked.connect(lambda: BaseActivity.change_normal(self))

    def mousePressEvent(self, event):
        """
        重构鼠标点击事件
        :param event:
        :return:
        """
        if not self.bar:
            return
        if (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            self._bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < self.bar.height()):
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, _):
        """
        判断鼠标位置 是否移动到了 指定的范围内
        以便更换鼠标样式
        :param _:
        :return:
        """
        if _.pos() in self._corner_rect:
            self.setCursor(Qt.SizeFDiagCursor)
        elif _.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)
        elif _.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

        if Qt.LeftButton and self._right_drag:
            self.resize(_.pos().x(), self.height())
            _.accept()
        elif Qt.LeftButton and self._bottom_drag:
            self.resize(self.width(), _.pos().y())
            _.accept()
        elif Qt.LeftButton and self._corner_drag:
            self.resize(_.pos().x(), _.pos().y())
            _.accept()
        elif Qt.LeftButton and self._move_drag:
            self.move(_.globalPos() - self.move_DragPosition)
            _.accept()

    def mouseReleaseEvent(self, _):
        """
        鼠标释放后，各扳机复位
        :param _:
        :return:
        """
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def dragEnterEvent(self, event):
        """
        判断拖拽物体是否有路径，有时拖拽生效
        :param event:
        :return:
        """
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        """
        拖拽移动
        :param event:
        :return:
        """
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(Qt.CopyAction)
            except Exception as e:
                self.logger.error(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """
        如果需要监听文件拖拽则重构此方法
        获取拖拽文件
        :param event:
        :return:
        """
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.CopyAction)
                event.accept()
                links = []
                for url in event.mimeData().urls():
                    links.append(str(url.toLocalFile()))
                print(links)
            else:
                event.ignore()
        except Exception as e:
            raise e

    def error_dialog(self, response: ResponseData):
        """
        执行出错，弹窗提示，
        :param response:
        :return:
        """
        if str(response.data) == "list index out of range":
            info = "结果为空"
        elif isinstance(response.data, PermissionError):
            info = "无权访问"
        else:
            info = "操作失败: {}".format(response.data)
        self._error_dialog_str(info)

    @staticmethod
    def error_dialog_str(err_info: str):
        """
        错误, 内部使用
        :param err_info:
        :return:
        """
        error_dialog(err_info)

    @staticmethod
    def message_text(info):
        """
        通知
        :param info:
        :return:
        """
        message_ok(info)

    def draw_shadow(self, painter):
        """
        绘制边框阴影
        :param painter:
        :return:
        """
        # 绘制左上角、左下角、右上角、右下角、上、下、左、右边框
        pix_maps = list()
        pix_maps.append(str(self.config.get_shadow_path("left_top.png")))
        pix_maps.append(str(self.config.get_shadow_path("left_bottom.png")))
        pix_maps.append(str(self.config.get_shadow_path("right_top.png")))
        pix_maps.append(str(self.config.get_shadow_path("right_bottom.png")))
        pix_maps.append(str(self.config.get_shadow_path("top_mid.png")))
        pix_maps.append(str(self.config.get_shadow_path("bottom_mid.png")))
        pix_maps.append(str(self.config.get_shadow_path("left_mid.png")))
        pix_maps.append(str(self.config.get_shadow_path("right_mid.png")))
        # 左上角
        painter.drawPixmap(0, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(pix_maps[0]))
        # 右上角
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(pix_maps[2]))
        # 左下角
        painter.drawPixmap(0, self.height() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(pix_maps[1]))
        # 右下角
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH, QPixmap(pix_maps[3]))
        # 左
        painter.drawPixmap(0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(pix_maps[6]).scaled(self.SHADOW_WIDTH,
                                                       self.height() - 2 * self.SHADOW_WIDTH))
        # 右
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(pix_maps[7]).scaled(self.SHADOW_WIDTH,
                                                       self.height() - 2 * self.SHADOW_WIDTH))
        # 上
        painter.drawPixmap(self.SHADOW_WIDTH, 0, self.width() - 2 * self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(pix_maps[4]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                       self.SHADOW_WIDTH))
        # 下
        painter.drawPixmap(self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH, self.width() - 2 * self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH, QPixmap(pix_maps[5]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                                          self.SHADOW_WIDTH))

    def paintEvent(self, event):
        """
        重新渲染
        :param event:
        :return:
        """
        painter = QPainter(self)
        self.draw_shadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(QRect(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width() - 2 * self.SHADOW_WIDTH,
                               self.height() - 2 * self.SHADOW_WIDTH))
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        painter.setPen(Qt.gray)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillPath(path, QBrush(Qt.white))
        # 起点 x， 起点 y， 终点 x， 终点 y，
        # 左右
        painter.drawLine(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH)
        painter.drawLine(self.width() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width() - self.SHADOW_WIDTH,
                         self.height() - self.SHADOW_WIDTH)
        # 上下
        painter.drawLine(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width() - self.SHADOW_WIDTH, self.SHADOW_WIDTH)
        painter.drawLine(self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH, self.width() - self.SHADOW_WIDTH,
                         self.height() - self.SHADOW_WIDTH)

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        """
        双击的坐标小于头部坐标是才最大化, 如果不需要这个功能，在继承子类时重构此方法即可
        :param e:
        :return:
        """
        if not self.bar or not self.bar_normal:
            return
        if e.pos().y() < self.bar.y() + self.bar.height():
            self.bar_normal.click()

    def keyPressEvent(self, a0: QtGui.QKeyEvent):
        """
        键盘监听事件
        :param a0:
        :return:
        """
        if a0.key() == Qt.Key_Escape:
            a0.ignore()
        else:
            a0.accept()
