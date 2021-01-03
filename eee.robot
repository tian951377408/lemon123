*** Settings ***
Library           DateTime
Library           Collections
Library           SeleniumLibrary

*** Test Cases ***
rrr
    [Tags]    asdfgbn
    ${LOG_FILE}    中文方法    WARN    #测试行号见客户
    Should Be Equal    100    100
    ${date}    Get Current Date

addq
    ${var_name}=    Set Variable    我们的    #变量，赋值
    Log    ${var_name}
    @{var_n}    Create List    1    2    3    4
    log    ${var_n}
    Append To List    ${var_n}    5
    log    ${var_n}
    Insert Into List    ${var_n}    0    Q
    log    ${var_n}
    ${var_n}    Get Length    ${var_n}

ddd
    Open Browser    http://erp.lemfix.com/login.html    GC
    Maximize Browser Window    #浏览器最大化
    ${title}    Get Title    #获取页面标题
    Comment    Title Should Be    柠檬ERP    #只用于标题的断言
    Comment    Should Be Equal    ${title}    柠檬ERP    #常用的断言
    Run Keyword If    '${title}'=='柠檬ERP'    log    测试通过
    ...    ELSE     log    测试不通过
    ${page_text}    Get Text    xpath=/html/body/div/div/div[1]/a/b
    Should Be Equal    ${page_text}    柠檬ERP
    ${page_text2}    Get Text    xpath=/html/body/div/div/div[1]/a/small
    Should Be Equal    ${page_text2}    V1.3
    Click Element    xpath=//*[@id="username"]    #点击用户名输入框    #Click Button必须是按钮属性，所以这个也不好用
    Comment    Click Element    username    #http页面语言规定，id和name是唯一的，所以这里可以直接写值，但因为有些是没有这个属性的元素，只能用其他方式定位，所以这个不太可靠
    Input Text    xpath=//*[@id="username"]    test123
    Click Element    xpath=//*[@id="password"]
    Input Password    xpath=//*[@id="password"]    123456
    Click Element    xpath=//button[@id="btnSubmit"]
    Wait Until Element Is Visible    xpath=//div[1]/div[2]/p    #等待元素可见，默认等待5S，一般是一直等，直到出现
    ${user_name}    Get Text    xpath=//div[1]/div[2]/p
    Should Be Equal    ${user_name}    测试用户
    Run Keyword If    '${user_name}'=='测试用户'    log    测试通过
    ...    ELSE    log    测试不通过

QQ
    ${tab-count}    Get Element Count    xpath=//*[@id="leftMenu"]/ul/li
    ${tab_relname}    Create List    零售管理    采购管理    销售管理    仓库管理    财务管理    报表查询    商品管理    基本资料
    ${tab-ex}    Create List    #做一个空列表
    FOR    ${num}    IN RANGE    ${tab-count}
        ${tab_name}    Get Text    xpath=//*[@id="leftMenu"]/ul/li[${num}+1]/a/span[1]
        Comment    Should Be Equal    ${tab_name}    ${tab_relname}[${num}]
        Comment    Run Keyword If    '${tab_name}'=='${tab_relname}[${num}]'    log    测试通过
        Comment    ...
        ...    ELSE    log    测试不通过
        Append To List    ${tab-ex}    ${tab_name}
    END
    log    ${tab-ex}
    Should Be Equal    ${tab_relname}    ${tab-ex}
    Click Element    xpath=//*[@id="leftMenu"]/ul/li[1]/ul/li[1]/a/span
    ${get-text}    Get Text    xpath=//*[@id="tabpanel"]/div/div[1]/div[3]/ul/li[2]/div[1]    #id是变化的，只能通过父节点定位
    Should Be Equal    ${get-text}    零售出库
    ${id}    Get Element Attribute    xpath=//*[@id="tabpanel"]/div/div[2]/div[2]/iframe    id
    ${frame_id}    Set Variable    ${id}
    log    ${frame_id}
    Select Frame    ${frame_id}
    ${ge}    Get Element Count    xpath=//*[@id="tablePanel"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr
    Click Element    xpath=//*[@id="searchBtn"]/span/span
    Input Text    xpath=//*[@id="searchNumber"]    ${EMPTY}    #这个是固定变量，表示为空
    ${geshu}    Get Element Count    xpath=//*[@id="tablePanel"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr
    Should Be Equal    ${geshu}    ${ge}
    Input Text    searchNumber    841
