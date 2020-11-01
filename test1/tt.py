# from selenium import webdriver
# import time   #导入time模块---Python自带的
# # # #选择Chrome这个浏览器，初始化driver--可以和浏览器沟通 sessi
# driver = webdriver.Chrome()
# driver.implicitly_wait(60)

def login_page(username,password,driver):
    driver.find_element_by_id("username").send_keys("test123")  #找到有username这个id元素
    driver.find_element_by_id("password").send_keys("123456") #登录ERP演示
    driver.find_element_by_id("btnSubmit").click()

def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    import time
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(10)
    P_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    print(P_id)
    time.sleep(3)
    x_id= P_id+"-frame"
    print(x_id)
    time.sleep(3)
    # 方法一：
    driver.switch_to.frame(x_id)
    time.sleep(10)
    driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys(s_key)
    driver.find_element_by_xpath('//span[text()="查询"]').click()
    num= driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text

    return num






# # 1，打开一个网址
# driver.get("http://erp.lemfix.com/login.html")
# # 2. 浏览器窗口最大化
# driver.maximize_window()
# # 3. 打开一个新的页面
# # time.sleep(2)   #等待2秒  ---默认单位为秒
# # driver.get("https://www.baidu.com/")
# # 4.向前 向后  刷新
# # time.sleep(2)
# driver.back()  #退回上一个页面
# # time.sleep(2)
# driver.forward() #前进到下一页页面
# # time.sleep(2)
# driver.refresh()  #刷新页面
# # 5.退出
# # driver.close()  # 关闭当前窗口，不会退出session会话
# # driver.quit()  # 关闭驱动  session关闭   即关闭浏览器
# # 以上浏览器的常规操作
# # 基础知识：web页面=HTML+CSS+JavaScript
# # HTML：标签语言  <标签名>值<\标签名>    呈现页面内容
# # CSS：页面布局 ，字体颜色 大小 样式
# # JavaScript：实现不同的效果
# # 元素的特征：根据页面设计规则，有些特征是唯一的-----需要开发遵守这个规则
# # 元素八大定位方法，常用的有id,name,xpath,css,class,tag,link,partial_link，前三个用的多
# # id:仅限于当前页面的特征----如果没有，找开发
# #   对页面做对应的操作：点击 --click  输入内容：send_keys
# #                     获取文本：text  获取属性：attribute
#
# # time.sleep(5)
# page_title=driver.title
# print("这个页面的标题是：{}".format(page_title))
# # driver.find_element_by_xpath('//input[@id="username"]').send_keys("test123")
# time.sleep(10)
# tt= driver.find_element_by_xpath('//div[@class="login-logo"]//b').text
# if tt=="柠檬ERP":
#     print("这个页面的内容是：{}".format(tt))
# else:
#     print("这个条件测试用例不通过！")
#
# driver.find_element_by_id("username").send_keys("test123")  #找到有username这个id元素
# driver.find_element_by_id("password").send_keys("123456") #登录ERP演示
# driver.find_element_by_id("btnSubmit").click()
#
# # log1 = driver.find_element_by_xpath('//div[@class="pull-left info"]//p').text
# # if log1 == "测试用户":
# #     print("这个页面的内容是：{}".format(log1))
# # else:
# #     print("这个条件测试用例不通过！")
# # time.sleep(5)
# driver.find_element_by_xpath("//span[text()='零售出库']").click()
# # time.sleep(10)
# # P_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
# # print(P_id)
# # time.sleep(3)
# # x_id= P_id+"-frame"
# # print(x_id)
# # time.sleep(3)
# #方法一：
# # driver.switch_to.frame(x_id)
# time.sleep(10)
# # driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys("841")
# # time.sleep(3)
# #方法二：
# # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(x_id)))
# # driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys("841")
# # driver.find_element_by_xpath('//span[text()="查询"]').click()
# # pri = driver.title
# # print("这个页面的标题是：{}".format(pri))
# # 方法三：通过iframe下标来切换，一个页面只有一个html，一个HTML只有一个iframe，序号是从0开始。
# driver.switch_to.frame(1)
# time.sleep(10)
# driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys("841")
# time.sleep(3)
# driver.find_element_by_xpath('//span[text()="查询"]').click()