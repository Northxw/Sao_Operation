### 目标
&emsp; 通过 Appium Server 实现在线安装、本地安装(提前下载apk文件)手机应用。本次在线安装的示例软件是TIM，以及本地安装的软件墨迹天气。

### 思路
&emsp; 运行Appium(自动监听4723端口), 通过Python编写的脚本向端口对应的服务接口发送操作指令, 实现在线或本地安装App。   
&emsp; 首先，编写爬虫脚本抓取"2345安卓应用"商城的手机应用下载链接（这里将脚本封装为类，方便扩展）。获取链接的代码如下：

```
def get(self, url):
        """
        获取下载详情页中Apk的下载链接
        :param url: 下载详情页的URL
        :return: apk的下载URL
        """
        apk_downlaod_url = ''
        response = urllib.request.urlopen(url)  # 发送请求,返回结果
        doc = pq(response.read())
        href = doc('.apk_info_box .dl_area .btn_trig #quickDown').items()
        for _ in href:
            apk_downlaod_url = _.attr('href')
            break
        return apk_downlaod_url
```   
&emsp; 然后，在Install_online.py中引用返回的链接。这里最重要的是配置启动安装的参数,分别是：paltformName，deviceName, app。配置代码如下：

```
def __init__(self, server=SERVER, app_value=APP_VALUE, platformname=PLANTFORM, devicename=DEVIDE_NAME):
        """
        初始化信息
        :param server: Appium Server
        :param app_value: Apk 文件的下载链接
        """
        self.server = server
        self.app_value = app_value
        self.platformname = platformname
        self.devicename = devicename
```
&emsp; 配置参数以及其他信息都单独保存为config.py文件，方便扩展（比如修改设备名称或者设备类型等）。   
&emsp; 最后，运行主程序 Install_online.py 文件就会完成在线安装App。本地安装更加简单，不再做说明。  

### 注意事项
&emsp; 接下来对测试安装过程中要注意的问题做一下简单总结：
+ 选择2345安卓市场下载的原因是：APK文件的下载链接方便查找。当然，也可以选择百度软件助手。不建议将"安智市场"作为爬取目标, 各种反爬，太烦人。
+ 本地安装手机应用的APK文件尽量放在项目路径下，方便检索。
+ 若之前使用Appium桌面版软件对手机软件做测试，要插拔重连安卓机，否则代码run之后可能没有响应。
+ 若安装的APP已经存在本地，相当于更新操作。并会自动更新软件的数据。
+ 安装APP的过程中需要手动确定安装（获取权限），至于怎么实现跳过该步骤，无法替您解答（可自行百度）。
+ "2345安卓市场"的软件搜索详情页的URL对keyword为中文的字符做了特殊处理。所以, 本次实践的在线安装以TIM为例来演示。
+ 注意安卓手机与PC机链接正常，测试方法在上一篇中有讲到，[...传送门！...](https://github.com/Northxw/Sao_Operation/blob/master/02-Open_WeChat/readme.md)

### 总结
&emsp; 本次实践中走了很多弯路, 盲目分析爬取请求，导致最后获取不到想要的数据。具体思路有点模糊。希望自己以后可以注意这方面。