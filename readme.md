*简单开发你的qt应用，答应我，别再熬夜了，好吗？👀✨*
---

# 基本介绍

easy qt for python（eq） 致力于样式跟界面布局之上，力达能够做出一个快速开发的组件框架，作为开发人员的你只需专注于业务逻辑以及如何调用即可。

📝  [点击此处查看文档](https://py-mu.github.io/easy-pyqt)

# 项目结构
    -project                # 项目目录
        | -view             # 视图
            | -activity     # 顶级窗口
            | -frame        # 组合控件
            | -ui           # Qt designer 设计的ui文件 & ui生成的模板
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
