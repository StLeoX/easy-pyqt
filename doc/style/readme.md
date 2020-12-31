# QT 样式设计指南

参考Qt官网样式设计指南：
- [Qt 样式表示例](https://doc.qt.io/qt-5/stylesheet-examples.html)
- [Qt 样式表参考](https://doc.qt.io/qt-5/stylesheet-reference.html)

## 一、基本元素

### 1、QPushButton 按钮

### 2、QLineEdit 输入框

### 3、QToolTip 提示框



## 二、自定义主题

### 1.切换主题配色
复制[eq样式表](../../resource/qss/common.css)文件，重命名为你的项目基本样式。编辑复制的样式文件在以下找到配色变量
：
```css
DEFINED_VALUE{
    --basic-color: #fdfdfd; /*基本色*/
    --basic-color-sub: #d0d2d4;/*基本 辅助色 */
    --basic-color-sub-border: darkgray;/*基本 辅助边框色 */
    --basic-color-sub-outline: gray;/*基本 辅助边框色 */
    --accent-color: #6096ba;/*辅助色*/
    --accent-color-light: #6096ba;/*辅助亮色*/
    --basi-border-radius: 2px;/*默认的倒角*/
    --basi-pdding-sieze-5: 5px;/*默认的边距*/
}
```
根据项目需要修改为自己的配色。

### 2.如何使用变量？

与CSS用法一致，唯一两点：var(--accent-color-light);中间不能有空格，且必须以分号结尾；

### 3.如何变更样式（规范约束）

如需覆盖主题样式，只需新增样式文件，如bar.css,对需要覆盖的控件进行样式编辑
调用self.set_style("bar.css")方法（继承base view）对象可用。
或者：
```python
app = QApplication.instance() or QApplication(sys.argv)
app.setStyleSheet(ResourceLoader().style_from("common.css", "bar.css"))
```
