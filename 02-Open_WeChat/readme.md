#### 目标
&emsp; 使用Appium软件, Selenium 和 appium 第三方库实现自动化登录 Android 手机的微信App

#### 准备工作
&emsp; ! ! ! 首先下载安装并配置Java环境（谷歌或百度教程）， 然后依次执行以下步骤：
+ 第一步：正确安装 Appium 软件, Windows系统可以在 https://github.com/appium/appium-desktop/release  下载最新桌面版（默认安装即可）.
+ 第二步：因为要使用安卓手机做App抓取，还需要下载配置 Android SDK. 可以直接下载 [Android Studio](https://developer.android.com/studio/index.html?hl=zh-cn)( 默认安装即可 ), 然后下载 Android SDK（方法可自行百度）
+ 第三步：将SDK以及SDK文件夹下的 tools 和 platform-tools 文件夹添加到系统PATH中.      

&emsp; 此外，还可以通过nodejs安装appium.  [runoob教程](http://www.runoob.com/nodejs/noedejs-install-setup.html), 注意下载最新的node版本.

#### Appium启动App的方式
&emsp; Appium启动App有两种方式，具体操作可以谷歌或百度，方式如下：
+ Appium内置的驱动器打开App
+ Python程序实现

#### 提示
&emsp; 操作过程中可能出现的错误我列举几点：
+ 安卓手机与PC端连接异常（记得打开手机的开发者模式）
+ 错误反馈中包含 "Can't not found Java..."，没有Java环境，所以一定要提前配置好Java环境
+ 设置的启动参数有误

&emsp; 最后的重要提示: <font color="#dd0000">提前退出微信登录，并且一定要保持手机处于解锁常亮状态！</font><br/>

#### 其他
&emsp; 程序的可扩展性很高，例如短信验证码登录，设置更加具体的异常处理模块等等