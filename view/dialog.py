# coding=utf-8
"""
    create by pymu on 2020/6/18
    package: .dialog.py
    常用弹窗集合
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QDialog, QHBoxLayout, QLabel

from common.loader.resource import ResourceLoader


def show_information_message_simple(text):
    """
    显示消息对话框(仅有确定)
    :param text: 内容
    :return:
    """
    message = QMessageBox(QMessageBox.Information, "消息提示框", text)
    message.addButton("确定", QMessageBox.YesRole)
    message.setWindowIcon(ResourceLoader().qt_icon_project_ico)
    message.exec_()


def show_warning_message(text):
    """
    显示警告对话框
    :param text: 内容
    :return:
    """
    message = QMessageBox(QMessageBox.Warning, "警告提示框", text)
    message.addButton("确定", QMessageBox.YesRole)
    message.addButton("取消", QMessageBox.NoRole)
    message.setWindowIcon(ResourceLoader().qt_icon_project_ico)
    message.exec_()


def show_critical_message(text):
    """
    显示错误对话框
    :param text: 内容
    :return:
    """
    message = QMessageBox(QMessageBox.Critical, "错误提示框", text)
    message.addButton("确定", QMessageBox.YesRole)
    message.setWindowIcon(ResourceLoader().qt_icon_project_ico)
    message.exec_()


def show_question_message(text):
    """
    显示问题对话框
    :param text: 内容
    :return:
    """
    message = QMessageBox(QMessageBox.Question, "确认提示框", text)
    qyes = message.addButton("确定", QMessageBox.YesRole)
    qno = message.addButton("取消", QMessageBox.NoRole)
    message.setWindowIcon(ResourceLoader().qt_icon_project_ico)
    return message, qyes, qno


def show_override_message(text):
    """
    显示问题对话框，用于询问是否追加/覆盖/取消?
    :param text: 内容
    :return:
    """
    message = QMessageBox(QMessageBox.Question, "确认提示框", text)
    qoverride = message.addButton("覆盖", QMessageBox.YesRole)
    qadd = message.addButton("追加", QMessageBox.YesRole)
    qcancel = message.addButton("取消", QMessageBox.NoRole)
    message.setWindowIcon(ResourceLoader().instance().qt_icon_project_ico)
    return message, qoverride, qadd, qcancel


def waiting_dialog(waiting_info: str = "加载中，请稍后") -> QDialog:
    """
    等待对话框
    使用方法：
    实例化弹出层之后
        # 在BaseActivity 中会初始化默认的拥塞弹窗
        self.waiting_dialog = waiting_dialog(waiting_info="显示文本信息")
        在需要执行的线程中进行拥塞UI
        如在修改数据线程：
        self.waiting_dialog
    :param waiting_info:
    :return:
    """
    div = QDialog(None, Qt.FramelessWindowHint)
    div.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.Tool |
                       Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint |
                       Qt.WindowMaximizeButtonHint)
    div.resize(240, 60)
    div.layout = QHBoxLayout(div)
    div.label = QLabel(waiting_info)
    div.label.setFont(ResourceLoader().qt_font_11)
    div.layout.addWidget(div.label, alignment=Qt.AlignCenter)
    return div


def waring_dialog(info):
    """
    警告
    :return:
    """
    message_box, btn_yes, _ = show_question_message(info)
    message_box.exec_()
    return message_box.clickedButton() == btn_yes


def message_ok(info):
    """
    一般通知弹窗。通常用作在线程执行结束后的通知
    :param info:
    :return:
    """
    show_information_message_simple(info)


def error_dialog(info):
    """
    操作失败
    :param info:
    :return:
    """
    message = QMessageBox(QMessageBox.Critical, "错误提示框", info)
    message.addButton("确定", QMessageBox.YesRole)
    message.setWindowIcon(ResourceLoader().qt_icon_project_ico)
    message.exec_()
