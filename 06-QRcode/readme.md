### 目标
&emsp; 使用Python的第三方库- **MyQR** 生成普通二维码、带图片的艺术二维码(黑白与彩色)、动态二维码(黑白与彩色)

### 参考
&emsp; MyQR 的 github 中文介绍文档：https://github.com/sylnsfar/qrcode/blob/master/README-cn.md

### 安装
&emsp; 安装 MyQR 最简单粗暴的方法即通过 **pip(3)** 安装，它会自动安装所需的依赖包 (pillow, numpy, imageio), 如下：
```
pip(3) install myqr(or MyQR)
```
&emsp; 如果安装过程出现依赖错误,请移步至 https://pypi.org/project/MyQR 下载依赖库.    
<br/>

### 普通二维码
![普通二维码](https://github.com/sylnsfar/qrcode/blob/master/example/0.png)    
&emsp; 1. 命令行输入链接或者句子作为参数, 在当前目录下自动生成默认命名的png格式二维码. 示例：
```
myqr https://github.com/Northxw
```
&emsp; 2. 控制二维码的边长和纠错等级使用 -v 和 -l 参数.
+ **-v** 控制边长, 范围是1-40, 数字越大边长越大
+ **-l** 控制纠错等级, 范围是L、M、Q、H, 从左到右依次依次升高. 示例：
```
myqr https://github.com/Northxw -v 10 -l Q
```
&emsp; 3. 自定义文件名和输出位置.
+ **-n** 控制文件名, 格式可以是 .jpg， .png ，.bmp ，.gif
+ **-d** 输出位置
```
myqr https://github.com/Northxw -n northxw.jpg  -d .../paths/
```
&emsp; 4. 当然, 你还可以综合上述参数使用，如下:
```
myqr https://github.com/Northxw -v 5 -l H -n northxw.jpg  -d .
```
<br/>

### 艺术二维码
![艺术二维码](https://github.com/sylnsfar/qrcode/raw/master/example/2.png)   

&emsp; 1. 使用参数 **-p** 用来将QR 二维码图像与一张同目录下的图片相结合，产生一张**黑白**图片.
```
#1 -p
myqr https://github.com/Northxw -p northxw.jpg
```
<br/>

&emsp; 2. 使用参数 **-c** (color) 将产生的图片由黑白变为**彩色**.
```
#2 -c
myqr https://github.com/Northxw -p northxw.jpg -c
```
<br/>

&emsp; 3. 使用参数 **-con**, **-bri**
+ 参数-con 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
+ 参数 -bri 用来调节图片的亮度，其余用法和取值与 -con 相同。
```
#3 -con, -bri
myqr https://github.com -p github.jpg [-c] -con 1.5 -bri 1.6
```
<br>
&emsp; 4. 还可以使用上面介绍过的参数，如下:

```
myqr https://github.com/Northxw -p northxw.jpg -c -n northxw_c.png
```
<br/>

### 动态二维码
![动态二维码](https://github.com/sylnsfar/qrcode/raw/master/example/zootopia_qrcode.gif)
&emsp; 动态二维码与上述的带图片的二维码的生成方法没什么区别，你只要采用 .gif 格式的图片即可生成黑白或者彩色的动态二维码。但注意如果使用了 -n 参数自定义输出的文件名，切记其格式也必须是 .gif 格式。

```
myqr http://github.com/Northxw -p cs_2.gif -c -n love.gif
```
<br/>

### 作为文件导入

```
# 安装模块后
from MyQR import myqr
version, level, qr_name = myqr.run(
	words,
    version=1,
    level='H',
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd()
	)
```

### 说明
+ " 二维码的纠错等级 " 请参考：[二维码的纠错等级](https://blog.csdn.net/johnsuna/article/details/8864046?utm_source=blogxgwz0) 这篇博客做了比较详细的说明。此外，可以查看error_correction_level文件夹中的图片，做了对比.
+ " 作为文件导入 "的生成方式, 请查看文件夹file_import.

### 其他
&emsp; 图片的选择可以参考Github中给出的中文介绍。

### 总结
&emsp; MyQR库操作方便，功能强大。相信大家对qrcode库也有所了解，方法较多，但是操作冗杂，个人而言，还是比较使用MyQR库。
    当然，萝卜白菜，各有所爱，只要能完成目标任务即可。












