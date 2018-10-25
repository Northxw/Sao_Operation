### 目标
&emsp; 使用Appium, Charles分析京东App(获取节点ID)，并使用appium，mitmproxy的组件 mitmdump 实现对京东商品信息以及评论相关数据的爬取。
<br/>

### 思路
&emsp; 通过Charles抓包分析商品详情和商品评论的接口； 编写脚本 scripts 提取上述接口的数据，编写脚本 action 驱动App实现自动化； 将获取的数据存储至MongoDB    
<br/>

### 提示
&emsp; 测试期间应该注意的几个问题, 如下：
1. 驱动APP后, 首先会进入"京东隐私界面", 获取同意框的ID, Tap同意，如下：![京东隐私界面](https://github.com/Northxw/Sao_Operation/blob/master/05-JD/screenshot/%E4%BA%AC%E4%B8%9C%E9%9A%90%E7%A7%81%E6%94%BF%E7%AD%96%E7%95%8C%E9%9D%A2.png)    <br/>
2. 进入之后, 等待5秒+，会出现双11动画加载界面（非双11，双12期间应该不会出现类似界面），此时应该获取右上角" X "的节点ID或XPATH值，如图：![双11动画加载界面](https://github.com/Northxw/Sao_Operation/blob/master/05-JD/screenshot/%E5%8F%8C11%E5%8A%A8%E7%94%BB%E7%95%8C%E9%9D%A2.png)   <br/>
3. 进入商品详情页后, 上侧评论Tab栏并未加载, 测试如下：![tab_2](https://github.com/Northxw/Sao_Operation/blob/master/05-JD/screenshot/tab_2.png) 解决方案：通过模拟上滑, 至全部评论节点处，代码如下：
```
# 处理: 直接进入详情页无法查找到pd_tab3的节点,可通过上滑刷新到全部评论的位置,点击进入,效果相同;此时pa_tab3也会加载出来)
        # 向下滑动查找评论节点(测试发现,需要滑动屏幕三次)
        cnt = 1
        while True:
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            sleep(SCROLL_SLEEP_TIME)
            cnt = cnt + 1
            if cnt > 3:
                break
        # 滑动结束,延时等待
        sleep(25)
        # 判断节点是否出现,出现执行下一步,未出现继续下滑.
        if self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.productdetail:id/pd_comment_title'))):
            comments_tab_1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.productdetail:id/pd_comment_title')))
            comments_tab_1.click()
            # 点击进入评论详情页
        sleep(10)
```
4. 测试期间手机APP若存在更新行为，某些节点的ID或XPATH值会更改，亲测坑。     
<br/>

### 其他
&emsp; 淘宝、京东商品数据的Form表单以及请求参数有很多的加密参数，面对这些骚操作，使用Charles无法直接找到接口链接和参数。所以使用mitmproxy的组件mitmdump组件直接对接Python脚本并对请求的响应直接进行处理。   
&emsp; 相当于在请求和响应的必经之路上加了管道，当服务器响应后，返回响应，通过管道，此时在管道中获取响应，再原封不动的下发给App，处理完毕。    
<br/>

### 总结
&emsp; mitmdump很大程度上省去了请求参数构造，Form表单加密等工序，加上appium库实现App的动作模拟，几乎可以解决所有问题。但是还需要多加练习，加油。
