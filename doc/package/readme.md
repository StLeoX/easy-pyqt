# 打包

## 1、 pyinstaller 打包
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

### 注意事项
1. 打包缺少模块 pkg_resources.py2_warn
```shell script
--hidden-import=pkg_resources.py2_warn
```
 
## 2、