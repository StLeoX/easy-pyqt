# easy qt for python帮助手册
easy pyqt 集成大部分常见的开发组件及样式，能够通过极少的代码量即可生成完整功能的页面应用，
抛开繁琐的组件控件声明，信号槽定义，利用qt creator 即可快速的生成一个好看的qt 程序。
## 核心组件及功能
### 1.基本窗体 baseView
#### 介绍
默认的qt页面会调用系统的窗体样式，很多时候需要自定义一个无边框页面
#### 实现原理

#### 具备的功能

### 2.全局的异常拦截 ExceptionHandle
#### 介绍
在程序中运行中很多未知的异常不能完全被捕获，导致程序闪退缺不知原因，一般来说不应该对全部的运行方法进行 try
此时所以需要重写python的全局异常处理方法。
#### 实现原理
重写 sys的excepthook方法，
```python
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
    # 对异常的详细记录，写入日志
    self.logger.error("{}".format(msg))
    # 调用弹窗进行信息的简要提示
    error_dialog(self.exception_mapping(exc_type, exc_value))
```

#### 具备的功能