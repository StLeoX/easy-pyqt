![app icon](resource/img/icon.png) 


*简单开发你的qt应用，答应我，别再熬夜了，好吗？👀✨*
---

# 基本介绍

easy qt for python 致力于样式跟界面布局之上，作为开发人员的你只需专注于业务逻辑即可。

- 👉国内玩家请访问[码云](https://gitee.com/pymu/easy-pyqt)🚩👈

- 👉点击[easy your qt](doc/help/)查看我们是如何制作eq框架的。👈

- 👉点击[qesy pyqt 使用教程](doc/start/)查看，如何使用eq框架快速开发一个pyqt应用程序。👈

- 👉点击[qesy pyqt todo清单](doc/todo/)查看待实现的清单列表。👈

- 👉点击[qesy pyqt 设计风格](doc/ui_designer/)查看eq的设计思路。👈

- 👉点击[组件列表](doc/frame_list/)查看已实现的组件，从中选择你喜欢的组件进行开发吧。👈

- 👉点击[QT样式指南](doc/style/)。👈

- 👉点击[qt测试](https://github.com/PyQt5/PyQt) 大佬的测试样例，能解决大部分功能问题。👈

- 👉点击[打包教程](doc/package/) python应用打包详解。👈


# 项目结构
---
    -project                # 项目目录
        | -view             # 视图
            | -activity     # 顶级窗口
            | -frame        # 组合控件
            | -ui           # Qt designer 设计的ui文件
            | -uipy         # ui生成的模板
        | -service          # 服务层
        | -example          # 测试样例
        | -config           # 配置文件
            | setting.py    # 保存常用的目录路径及配置选项
        | -log              # 日志文件夹
        | -resource         # 静态资源，需要打包的资源文件也需要放置在此处
            | -img          # 图片资源
            | -qss          # 界面样式
        | -common           # 公共
            | -util         # 工具集
        | -requirement.txt  # 依赖列表
        | -README           # 辅助说明

# 快速开始

- 安装必要的模块包
```shell script
# 在激活的虚拟环境下（如果有）
pip install -r requirement.txt
```

- 运行
```shell script
python main.py
```

# 界面设计
！需要使用Qt creator 图形界面设计工具，不到不得已尽量不要手写页面

流程如下：
- 1、设计好ui文件，统一放置在ui文件夹下，如果数量太多，可新建子文件夹
- 2、通过命令 pyuic5 -x <ui文件> -o uipy/<py模板>, 统一转换到uipy文件夹下，
     如果对应的有文件夹，那uipy也应存在，需要注意，生成之后不可以修改此文件，要修改只能从ui图形设计修改，再转换而至
     pyside2-uic mainwindow.ui > ui_mainwindow.py
- 3、如果设计的ui模板属于frame组件级别的，在frame包新建一个类文件，通过集成及修改
      如果是activity级别，那就在activity包下集成修改。
> 很好，现在来说一下，以上都是废话，在这里只需遵循一个原则：第一、是确保组件是可复用的，第二、uipy（ui转来的py）仅是可读的。
> 其他的无所谓啦


# 打包
! 需安装 pyinstaller

打包命令列表

|option| description|for example|
|:----:| :---------:|--------|
|-i    |指定图标文件  | -i icon.ico
|-w    |无cmd打包    | -w[F] #通常与F使用
|-F    |打包为一个EXE | -Fw #打包为一个无cmd的EXE
|-c    |使用cmd win系统有效 | -c 
|-n    |程序名       | -n 审计助手  
|-add-data    |添加resource       | --add-data="resource;resource"

```shell script
pyinstaller -w main.py -i icon.ico --add-data="resource;resource" -n 工具名称
# 或者
build.bat
```

# 注意事项
1. 打包缺少模块 pkg_resources.py2_warn
```shell script
--hidden-import=pkg_resources.py2_warn
```
 