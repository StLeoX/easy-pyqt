# coding=utf-8
"""
    create by pymu
    on 2020/12/15
    at 10:13
    全局拦截
"""
import sys
import threading
import traceback
from typing import Any, Dict, Optional

from common.util.logger import Logger
from view.activity.activity_dialog_normal import NormalDialogActivity


class ExceptionHandle:
    _instance_lock = threading.Lock()
    is_init = False

    class ExceptionOperational:
        """异常操作类型"""
        LEVEL_DEBUG = 0
        LEVEL_INFO = 1
        LEVEL_WARNING = 2
        LEVEL_ERROR = 2

        # 异常描述
        description = "未知异常"
        # 是否弹窗通知
        is_show_dialog = False
        # 回调方法
        callback: Any = None
        # 异常等级
        exception_level: int = 0
        # 是否做日志记录，默认为记录在日志中
        is_log_it = True
        dialog_title = "程序异常"

        def __init__(self, description="未知异常", is_show_dialog=True, dialog_title="程序异常",
                     callback=None, exception_level=LEVEL_ERROR, is_log_it=True):
            """
            初始化有一个异常操作类型,在异常触发时调用
            :param description: 异常描述
            :param is_show_dialog: 是否显示弹窗
            :param dialog_title: 弹窗的标题
            :param callback: 回调，即触发该异常时进行回调
            :param exception_level: 异常等级，根据等级显示弹窗的等级
            :param is_log_it: 是否做日志记录， 默认是
            """
            self.description = description
            self.is_show_dialog = is_show_dialog
            self.callback = callback
            self.exception_level = exception_level
            self.is_log_it = is_log_it
            self.dialog_title = dialog_title

    # 异常映射类型(可以重构)
    # 因为全局异常类是属于一个全局单例对象
    # 所以可以声明为类属性，不必声明在对象属性中
    # 同时在不同的场景下可以通过修改类属性而修改异常操作类型
    mapping_dict: Dict[str, ExceptionOperational] = {
        "ZeroDivisionError": ExceptionOperational("除零异常"),
        "RecursionError": ExceptionOperational("超出最大递归深度"),
        "SystemExit": ExceptionOperational("解释器请求退出"),
        "KeyboardInterrupt": ExceptionOperational("用户中断执行"),
        "StopIteration": ExceptionOperational("迭代器没有更多的值"),
        "GeneratorExit": ExceptionOperational("生成器(generator)发生异常通知退出"),
        "ArithmeticError": ExceptionOperational("数值计算错误"),
        "FloatingPointError": ExceptionOperational("浮点数值计算错误"),
        "OverflowError": ExceptionOperational("数值运算超出最大限制"),
        "AssertionError": ExceptionOperational("断言语句失败"),
        "AttributeError": ExceptionOperational("对象没有这个属性"),
        "EOFError": ExceptionOperational("没有内建输入,到达EOF 标记"),
        "EnvironmentError": ExceptionOperational("操作系统错误"),
        "IOError": ExceptionOperational("输入/输出操作失败"),
        "OSError": ExceptionOperational("操作系统错误"),
        "WindowsError": ExceptionOperational("系统调用失败"),
        "ImportError": ExceptionOperational("导入模块/对象失败"),
        "LookupError": ExceptionOperational("无效数据查询"),
        "IndexError": ExceptionOperational("序列中没有此索引(index)"),
        "KeyError": ExceptionOperational("映射中没有这个键"),
        "MemoryError": ExceptionOperational(" 内存溢出错误", is_show_dialog=False),
        "NameError": ExceptionOperational("未声明/初始化对象"),
        "UnboundLocalError": ExceptionOperational("访问未初始化的本地变量"),
        "ReferenceError": ExceptionOperational("弱引用(Weak reference)试图访问已经垃圾回收了的对象"),
        "RuntimeError": ExceptionOperational("运行时错误"),
        "NotImplementedError": ExceptionOperational("调用未实现的方法"),
        "SyntaxError": ExceptionOperational("python语法错误"),
        "IndentationError": ExceptionOperational("python缩进错误"),
        "TabError": ExceptionOperational("python缩进空格混用错误"),
        "SystemError": ExceptionOperational("解释器系统错误"),
        "TypeError": ExceptionOperational("类型无效"),
        "ValueError": ExceptionOperational("值无效"),
        "FileNotFoundError": ExceptionOperational("找不到路径"),
        "PermissionError": ExceptionOperational("无操作权限"),
        "UnicodeError": ExceptionOperational("Unicode编码异常"),
        "UnicodeDecodeError": ExceptionOperational("Unicode解码异常"),
        "UnicodeEncodeError": ExceptionOperational("Unicode编码异常"),
        "UnicodeTranslateError": ExceptionOperational("Unicode编码转换异常"),
        "Warning": ExceptionOperational("警告", is_show_dialog=False, exception_level=ExceptionOperational.LEVEL_WARNING),
        "DeprecationWarning": ExceptionOperational("调用过时方法或者类", is_show_dialog=False,
                                                   exception_level=ExceptionOperational.LEVEL_WARNING),
        "FutureWarning": ExceptionOperational("关于构造将来语义会有改变的警告", is_show_dialog=False,
                                              exception_level=ExceptionOperational.LEVEL_WARNING),
        "OverflowWarning": ExceptionOperational("关于自动提升为长整型(long)的警告", is_show_dialog=False,
                                                exception_level=ExceptionOperational.LEVEL_WARNING),
        "PendingDeprecationWarning": ExceptionOperational("关于特性将会被废弃的警告", is_show_dialog=False,
                                                          exception_level=ExceptionOperational.LEVEL_WARNING),
        "RuntimeWarning": ExceptionOperational("可疑的运行时行为(runtime behavior)的警告", is_show_dialog=False,
                                               exception_level=ExceptionOperational.LEVEL_WARNING),
        "SyntaxWarning": ExceptionOperational("可疑的语法的警告", is_show_dialog=False,
                                              exception_level=ExceptionOperational.LEVEL_WARNING),
        "UserWarning": ExceptionOperational("用户代码生成的警告", is_show_dialog=False,
                                            exception_level=ExceptionOperational.LEVEL_WARNING),
    }

    def __init__(self, is_mapping=True):
        """
        全局异常处理，包含属性：
            - logger：日志
            - exception：异常回溯
            - exception_mapping：异常转换成中文
        :param is_mapping: 是否映射成中文
        """
        if self.is_init:
            return
        else:
            self.is_init = not self.is_init
        self.is_mapping = is_mapping
        self.logger = Logger()
        sys.excepthook = self.exception

    @staticmethod
    def instance():
        """获取实例"""
        instance: Optional[ExceptionHandle] = getattr(ExceptionHandle, "_instance")
        return instance or ExceptionHandle()

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
        todo 异常回调
        分为两个部分：
            - 日志记录：写到日志文件中
            - 弹窗提示，除了日志无感记录之外，出现未记录的异常应该提示给用户
        :param exc_type: 异常对象
        :param exc_value: 异常信息
        :param tb: 栈回溯
        """
        ex_operational = self.mapping_dict.get(exc_type.__name__, self.ExceptionOperational())
        if ex_operational.is_log_it:
            msg = ' Traceback (most recent call last):\n'
            while tb:
                filename = tb.tb_frame.f_code.co_filename
                name = tb.tb_frame.f_code.co_name
                lineno = tb.tb_lineno
                msg += '   File "%.500s", line %d, in %.500s\n' % (filename, lineno, name)
                tb = tb.tb_next
            msg += ' %s: %s\n' % (exc_type.__name__, exc_value)
            self.logger.error("{}".format(msg))
        if ex_operational.is_show_dialog:
            if ex_operational.exception_level == self.ExceptionOperational.LEVEL_ERROR:
                NormalDialogActivity(
                    info=f"{ex_operational.description if self.is_mapping else exc_type.__name__} {exc_value}",
                    title=ex_operational.dialog_title).exec()
