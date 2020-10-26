# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .async_thread.py
    project: audit_tools
    异步线程
        通过设定外部方法执行，
        执行结束跟捕获异常时均会发出信号，返回ResponseData 应答
"""
import uuid

from PyQt5.QtCore import QThread, pyqtSignal

from common.util.logger import Logger


# noinspection PyBroadException
class ResponseData:
    """
        应答信号
    """
    # 执行成功
    SUCCESS_CODE = 0
    # 执行失败
    FAILED_CODE = 1

    code = 0
    id_ = None
    data = None

    def __init__(self, code=0):
        self.code = code


# noinspection PyBroadException,PyUnresolvedReferences
class FuncThread(QThread):
    """
    使用示例：
        # 在activity 类中声明一个func thread

        self.delete_file_func = FuncThread()

        # 为线程信号绑定槽

        self.delete_file_func.thread_signal.connect(....)    # 正常通信频道
        self.delete_file_func.thread_error_signal.connect(....)    # 异常通信频道

    """
    # 正常通信信号
    thread_signal = pyqtSignal(ResponseData)
    # 异常通信信号
    thread_error_signal = pyqtSignal(ResponseData)
    # 终止信号
    thread_finally_signal = pyqtSignal(ResponseData)
    # 是否在运行
    __is_working: bool = False

    def strike(self, response: ResponseData = None):
        """
        手动激发
        :param response:
        :return:
        """
        self.finally_signal.emit(response or ResponseData())

    @property
    def success_signal(self) -> pyqtSignal:
        """
        成功通信频道
        :return:
        """
        return self.thread_signal

    @property
    def failed_signal(self) -> pyqtSignal:
        """
        失败通信频道
        :return:
        """
        return self.thread_error_signal

    @property
    def finally_signal(self):
        return self.thread_finally_signal

    @property
    def working(self) -> bool:
        """
        是否在运行
        :return:
        """
        return self.__is_working

    def __init__(self):
        super().__init__()
        self.func = None
        self._id = uuid.uuid4()
        self.func_args = []
        self.func_kwargs = {}
        self.logger = Logger()
        self.success_signal.connect(lambda: None)
        self.failed_signal.connect(lambda: None)

    def set_func(self, func, _id=None, *args, **kwargs):
        """
        设置执行线程， 新建以一个通信对象之后，需要调用此方法设置执行方法之后才能开启
        通信执行线程
        :param _id: 线程通信鉴权
        :param func: 设置执行方法
        :param args:  设置执行参数
        :param kwargs: 设置执行参数（键值对）
        :return:  None
        """
        self.func = func
        self._id = _id
        self.func_args = args
        self.func_kwargs = kwargs
        self.logger.info("设置线程 func={}  arg={}  kwargs={}".format(func.__name__, args, kwargs))

    def quit_(self):
        """
        中断任务
        :return:
        """
        self.__is_working = False
        self.terminate()

    def run(self):
        """
        执行线程：
        在 start() 后启动
        其中有返回的结果，及执行异常时的通信
        """
        self.__is_working = True
        response = ResponseData(ResponseData.SUCCESS_CODE)
        response.id_ = self._id
        if self.func is None:
            self.logger.warning("没有设置线程方法，却要执行")
            return
        try:
            result = self.func(*self.func_args, **self.func_kwargs)
            response.data = result
            self.thread_signal.emit(response)
        except Exception as e:
            response.code = ResponseData.FAILED_CODE
            response.data = e
            self.thread_error_signal.emit(response)
            self.logger.error("执行失败 func={}  arg={}  kwargs={}, error={}".format(self.func.__name__,
                                                                                 self.func_args,
                                                                                 self.func_kwargs,
                                                                                 e))
        finally:
            self.finally_signal.emit(response)
            self.__is_working = False
