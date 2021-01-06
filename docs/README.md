<div style="text-align: center;">✨👀简单开发你的qt应用，答应我，别再熬夜了，好吗？👀✨</div>

---

# EQ简介

easy qt for python（EQ） 致力于样式跟界面布局之上，力达能够做出一个快速开发的组件框架，作为开发人员的你只需专注于业务逻辑。

> EQ 由qt萌新在项目中，总结而出的代码聚合，可能在开发思想上与qt背道而驰，非我离经叛道，而是实在不能明了为什么使用qt还要重复的对控件进行样式修改，重复的布局、重复的样式，重复的Ctrl C + V，
>也许在大多的开发人员中看来原生的样式就已经足够，但是还是想做一些自己的改变，不管是功能上还是页面布局上总是有太多的相似，这个算是一种尝试，使用QT designer设计模板之后
>无需多大改动，就能得到风格统一的样式，（此才是强迫症患者的福音？）如此即可不再重复的setObjectName、setStyleSheet，我切换主题就可改变风格、岂不美哉？
>但是理想很美好，现实却是略显骨感，有很多是我不能理解的，或者说是没有意识到的东西，所以在代码上、思路上、优化上有很多让人啼笑皆非的错误，也请诸位前辈不吝指正。

与此同时，如果你也想跟我完善这个项目，但是又不知道该做什么时，请访问📃[qesy pyqt todo清单](todo/readme.md)查看待实现的清单列表。

- 👉国内玩家请访问[码云](https://gitee.com/pymu/easy-pyqt)🚩

- 👉点击[easy your qt](help/readme.md)查看我们是如何制作eq框架的。

- 👉点击[qesy pyqt 使用教程](doc/start/)查看，如何使用eq框架快速开发一个pyqt应用程序。

- 👉点击[qesy pyqt todo清单](doc/todo/)查看待实现的清单列表。

- 👉点击[UI设计指南](doc/ui/)查看eq的风格设计思路，提供应用样式模板可选解决方案。

- 👉点击[组件列表](doc/frame/)查看已实现的组件，从中选择你喜欢的组件进行开发吧。

- 👉点击[Qss样式指南](doc/style/)。

- 👉点击[qt测试](https://github.com/PyQt5/PyQt) 大佬的测试样例，能解决大部分功能问题。

- 👉点击[打包教程](doc/package/) python应用打包详解。

- 👉点击[疑难解答](doc/package/) 查看在开发中的常见问题（持续收录）。



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
