
from test1 import tt
from test_data import test_date
from selenium import webdriver
# import time
# import time   #导入time模块---Python自带的

driver = webdriver.Chrome()
driver.implicitly_wait(60)

url=test_date.url["url"]
user= test_date.login_date['username']
pwd=test_date.login_date["password"]
s_key= test_date.s_key["s_key"]
print(url,user,pwd,s_key)
res=tt.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)
if s_key in res:
    print("搜索结果是正确的！")
else:
    print("搜索结果是错误的！")