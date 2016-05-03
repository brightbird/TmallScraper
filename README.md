# TmallScraper
===
===
## Project Document
 * Project Name: TmallScraper
 * Version: 5.1.1
 * Author：Guo Zhang
 * Contributor: Xingjian Lin
 * Data: 2016-05-03
 * Python version: 2.7.9 
 * Description: This is a Tmall scraper for China's Prices Project
  
---  
## Project Structure
===
  * tmallScraper.py (Main function)
    * scraperThreadPool (a thread pool for a scraper)
      * catPara.py (deal with parameters to the scraper function)
    * tmallCategoryScraper.py (a category scraper)
      * getParameter.py (unparse parameters for a URL)
      * createFile.py (create a file name for a page)
      * unparseURL.py (create URL for requests)
      * ipProxiesList, proxiesList (IP proxies pool)
    * categories.py (the categories required to be scrapered)
    
  * tmallTest
    * countData.py(count data, including category number,parameters number and file number) -> stat/ 
    * tmallListTest.py(test parameter groups) -> categoriesTest

  * proxiesPool
    * getIP_xici.py (get IP proxies from xicidaili)-> proxiesList
    * ipChecker.py (check IP proxies)-> ipProxiesList
 
  * requirements
    * requests,bs4

---

## CHANGELOG
====
* Version 5.1.1: 2016-5-3
  * 数据项目增加goodsID
  
* Version 5.1: 2016-4-30
  * 重构邮件模块
  * tmallCategoryScraper的PageScraper类增加logTime属性，便于排错
  * 重构Tmall脚本

* Version 5.0: 2016-4-24
  * 重构程序
  * 增加辅助统计数据模块
  * 增加辅助测试list模块
  * 增加辅助测试函数模块
  
* Version 4.4：2016-4-22
  * 重写线程池
  * 增加catPara.py模块，加工传入tmallScraper的参数
  
* Version 4.3.1： 2016-4-22
  * 修复tmallScraper.py文件的变量命名的bug
  
* Version 4.3: 2016-4-21
  * 加入邮件模块
  
* Version 4.2：2016-4-19
  * 主模块tmallCategoryScraper.py：修改参数传入，把URL参数改为可选参数传入
  
* Version 4.1: 2016-4-18
  * 增加re_match模块: 对销量和评论数进行处理

* Version 4.0.1：2016-4-18
  * 主模块tmallCategoryScraper.py:beautifulsoup解析器换成html.parser,提高解析稳定性（lxml解析器如果缓存不够会丢失内容）；
  * 辅助模块getIP_xici.py:加入延迟，防止速度过快被封。

* Version 4.0：2016-4-17
  * 放弃2、3兼容；
  * 修改参数传入，增加catNum；
  * 增加写入文件的数据，shopName和shopURL；
  * 更换tmallScraper.py；
  * 重新整理文件逻辑；
  * 说明：新版本中注释掉了显示正常运行的页面信息的语句，做测试可以加入，正式跑的时候注释掉即可。

* Version 3.2：2016-4-1
  * 修正bug；
  * 增加tmallScraper2.py和main.py，增强兼容性；
  * 增加requirements.txt及其说明文档
  * 主函数修改:main.py,tmallScraper.py,tmallScraper2.py都可以做主函数使用，其中main.py最安全

* Version 3.1: 2016-3-29
  * 修改文件写入，删除空行的影响。

* Version 3.0: 2016-3-29
  * 实现2、3兼容；

* Version 2.3: 2016-3-29

  * 修改unparseURL()函数，取消unparse模块的使用，提高2、3兼容性；
  * 优化字符串加法，用join方法代替；

* Version 2.2: 2016-3-28
  * 优化tmallCategoryScraper()函数，创建新函数tmallPageScraper()

* Version 2.1：2016-3-28
  * 针对面向对象修改tmallCategoryScraper.py的参数传入；
  * 修改parsePageHTML函数解析过程的检测；

* Version 2.0：2016-3-27
  * 面向对象的编程重构tmallCategoryScraper.py

* Version 1.2：2016-3-27
  * 修改scraperHeaders.py 的代理IP导入

* Version 1.1：2016-3-27
  * 修改tmallCategoryScraper.py的文件储存


* Version 1.0：2016-3-26
  * 主函数：（安装Python2.7.9后，双击打开即可）tmallScraper.py

  * 主模块（整体）：
    * tmallScraper.py 分类列表下所有分类的函数
    * tmallCategoryScraper.py 单个分类的函数
    * categories.py 分类列表
    * scraperHeaders.py HTTP请求头
    * ip_proxies_list IP列表文件

  * 辅助模块（独立模块）：
    * get_ip_xici.py 从西刺网获取代理IP（生成‘proxies_list文件’）
    * ip_proxy_check.py 检测代理IP（生成‘ip_proxies_list’文件）
