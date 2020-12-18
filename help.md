#easy qt for python
本教程意在介绍我们如何制作组件及如何利用组件快速开发。
## 一、 基本窗口
### 1.1 新建一个窗口
- 新建一个空项目
- 新建一个main.py文件，作为程序的主入口
- 在文件中输入：
```python
import sys
from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    window.show()
    sys.exit(app.exec_())
```
- 运行代码，就可以出现下面的界面。
![我的第一个qt窗口]()

>ps: 但是我们很多时候并不是都满意系统自带的窗口样式，于是乎。

### 1.2窗口无边框
在以上代码的基础上设定窗口属性为无边框:
```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())
```
显示的效果如下：
![无边框qt窗口]()

>ps: 好像跟我们想的有一点不一样，没有边框了，分不清界面，而且不能拖动，不能拉伸，于是乎。

###1.3 窗口阴影
有三个方案：
1. 通过重写paint给窗口绘制一个阴影效果
2. 给窗口的所有边界添加一个阴影图片，通过图片拉伸达到看起来是阴影的效果。
3. 窗口嵌套，用最顶层的窗口作为显示阴影的容器
> 考虑性能、代码侵入性，可扩展，此处采用3。

实现原理：
- 给最顶层窗体设置~~~①背景透明~~~；②无边框;③窗口大小
- 添加容器，用于放置其他组件，并设置其背景颜色
```python
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QWidget,QHBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    # 设定顶层窗口无边框 
    window.setWindowFlags(Qt.FramelessWindowHint)
    # 添加背景透明属性 
    # window.setAttribute(Qt.WA_TranslucentBackground)
    # 先设置顶层窗口为红色，用于比对
    window.setStyleSheet("background: red")
    window.resize(300, 200)
    widget = QWidget()
    widget.setStyleSheet("background: #fff")
    layout = QHBoxLayout(window)
    layout.addWidget(widget)
    window.show()
    sys.exit(app.exec_())
```
此时，起到的效果，应该是这样的：
![边框颜色]()
- 给主要容器widget添加阴影，同时给顶层窗口设置背景透明
```python

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QHBoxLayout, QGraphicsDropShadowEffect

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    # 设定顶层窗口无边框
    window.setWindowFlags(Qt.FramelessWindowHint)
    # 添加背景透明属性
    window.setAttribute(Qt.WA_TranslucentBackground)
    widget = QWidget()
    effect_shadow = QGraphicsDropShadowEffect()
    effect_shadow.setOffset(0, 0)  # 偏移
    effect_shadow.setBlurRadius(10)  # 阴影半径
    effect_shadow.setColor(Qt.darkGray)  # 阴影颜色
    widget.setGraphicsEffect(effect_shadow)
    widget.setStyleSheet("background: #fff")
    layout = QHBoxLayout(window)
    layout.addWidget(widget)
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())
```
最终的效果图应该是这样的：
![无边框阴影]()
> 看起来是有点感觉，但是不能拖动，不能拉伸，突然觉得系统的边框也不是那么难看（没办法，自己选的嘛偶像， 好在实现起来也不难），于是乎。

### 1.4 窗口拖动
写到此处，会发现代码量在增加，不能再写在方法中，如此不利于重构聚合，所以需要新建一个class，而窗口拖动也恰好需要重写在QWidget下的三个方法：
mousePassEvent（鼠标点击事件）、mouseMoveEvent（鼠标移动事件）、mouseReleaseEvent（鼠标释放事件）。
重新先思考，窗口拖动的流程：鼠标按下->鼠标移动->鼠标释放。
- 新建类，继承Dialog（为什么选择dialog？）
> 为什么选择继承QDialog而不是更上的QWidget？其实两者都差不多。我更乐意用继承QWidget作为组件的父类，QDialog作为页面级别的父类。

main.py
```python

```

