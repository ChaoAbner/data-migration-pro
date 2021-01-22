# 克隆项目

```git
git clone https://github.com/ChaoAbner/data-migration-pro.git
```

# 运⾏前置准备

mac系统请直接跳到第四步：安装依赖

## 1. 下载安装包

点击链接进⾏安装：Windows x86-64 executable installer

## 2. 安装

下载好安装包后，双击安装

具体操作参考：https://zhuanlan.zhihu.com/p/111168324

## 3. 测试

按下 win+R 打开运⾏窗⼝，输⼊**cmd**，回⻋，查看命令⾏窗⼝。

在命令⾏输⼊ **pip**，如果有以下的显示，说明正常。

![image-20201223174250774](http://img.fosuchao.com/image-20201223174250774.png)

## 4. 安装依赖

进⼊到脚本⽬录，即**data-migration-pro**

输⼊命令：**pip3 install -r requirements.txt --target=/Users/user/Library/Python/3.8/lib/python/site-packages**

没有pip需要先安装pip
mac安装命令：
**curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user
rm get-pip.py**



# 转**CSV**操作

## 1. **excel**⽂件准备

将整理好的excel⽂件，放在⽂件夹中，⽂件夹的名称重命名为：**newDataExcelList**

然后将⽂件夹放在桌⾯。

![image-20201223174344754](http://img.fosuchao.com/image-20201223174344754.png)

![image-20201223174414525](http://img.fosuchao.com/image-20201223174414525.png)

运⾏脚本

进⼊到脚本⽬录，即**data-migration-pro**

运⾏命令：**python data_tranfrom.py**

等待脚本运⾏完成，即可看到桌⾯上多了⼀个⽂件夹 **csvFile**

![image-20201223174437714](http://img.fosuchao.com/image-20201223174437714.png)

⾥⾯就是转好的csv⽂件。

![image-20201223174447731](http://img.fosuchao.com/image-20201223174447731.png)
