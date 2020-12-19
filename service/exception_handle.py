# coding=utf-8
"""
    create by pymu
    on 2020/12/15
    at 10:13
    全局异常处理
"""
import sys
import threading
import traceback

from common.util.logger import Logger
from view.activity.activity_dialog_normal import NormalDialogActivity


class ExceptionHandle:
    _instance_lock = threading.Lock()
    is_init = False

    def __init__(self):
        """
        全局异常处理，包含属性：
            - logger：日志
            - exception：异常回溯
            - exception_mapping：异常转换成中文
        """
        if self.is_init:
            return
        else:
            self.is_init = not self.is_init
        self.is_mapping = True
        self.logger = Logger()
        sys.excepthook = self.exception

    def __new__(cls, *args, **kwargs):
        """
        实现单例
        """
        if not hasattr(ExceptionHandle, "_instance"):
            with ExceptionHandle._instance_lock:
                if not hasattr(ExceptionHandle, "_instance"):
                    ExceptionHandle._instance = object.__new__(cls)
        return ExceptionHandle._instance

    def exception(self, exc_type: type, exc_value: BaseException, tb: traceback):
        """
        分为两个部分：
            - 日志记录：写到日志文件中
            - 弹窗提示，除了日志无感记录之外，出现未记录的异常应该提示给用户
        :param exc_type:
        :param exc_value:
        :param tb:
        :return:
        """
        msg = ' Traceback (most recent call last):\n'
        while tb:
            filename = tb.tb_frame.f_code.co_filename
            name = tb.tb_frame.f_code.co_name
            lineno = tb.tb_lineno
            msg += '   File "%.500s", line %d, in %.500s\n' % (filename, lineno, name)
            tb = tb.tb_next

        msg += ' %s: %s\n' % (exc_type.__name__, exc_value)
        self.logger.error("{}".format(msg))
        NormalDialogActivity(info=self.exception_mapping(exc_type, exc_value), title="操作异常").exec()

    def exception_mapping(self, exception_type: type, exc_value: BaseException):
        """
        异常映射,()
        :return:
        """
        if not self.is_mapping:
            return str(exception_type)
        if isinstance(exception_type, ZeroDivisionError):
            msg = "Python 解释器请求退出"
        elif isinstance(exception_type, KeyboardInterrupt):
            msg = "用户执行中断"
        elif isinstance(exception_type, StopIteration):
            msg = "迭代器没有更多的值"
        elif isinstance(exception_type, GeneratorExit):
            msg = "生成器(generator)发生异常来通知退出"
        else:
            msg = f"未知异常类型:{exception_type.__name__}"
        return f"{msg} {exc_value}"
