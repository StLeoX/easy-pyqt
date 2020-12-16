![app icon](icon.png) QT

# 基本介绍
支持的版本: ![python 版本](python_version.svg)

# 项目结构
---
    -project                # 项目目录
        | -activity         # 顶级窗口
        | -service          # 服务层
        | -test             # 单元测试
        | -config           # 配置文件
            | setting.py    # 保存常用的目录路径及配置选项
        | -log              # 日志文件夹
        | -resource         # 静态资源，需要打包的资源文件也需要放置在此处
            | -img          # 图片资源
            | -qss          # 界面样式
        | -ui               # Qt designer 设计的ui文件
        | -uipy             # ui生成的模板
        | -frame            # 组合控件
        | -common           # 公共
            | -util         # 工具集
        | -main.py          # 启动入口
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
 