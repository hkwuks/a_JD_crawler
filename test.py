from selenium import webdriver
import time, csv


# 查询商品
def get_product(keyword):
    driver.find_element_by_css_selector('#key').send_keys(keyword)
    driver.find_element_by_css_selector(
        '#search > div > div.form > button').click()
    driver.implicitly_wait(10)  # 等待渲染


# 模拟鼠标滚动
def drop_down():
    for i in range(1, 10):
        time.sleep(0.5)
        j = i / 10
        js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %s' % j
        driver.execute_script(js)


# 解析数据
def analyse_date():
    with open('data.csv','w',encoding='utf-8') as f:
        lis = driver.find_elements_by_css_selector('.gl-item')
        for li in lis:
            try:
                name = li.find_element_by_css_selector('.p-name a em').text
                name = name.replace('京东超市',
                                    '').replace('京品数码',
                                                '').replace('京品电脑',
                                                            '').replace('\n', '')

                price = li.find_element_by_css_selector(
                    ' .p-price > strong > i').text + '元'
                comment = li.find_element_by_css_selector(
                    '.p-commit strong a').text
                shop = li.find_element_by_css_selector('.p-shop span a').text
                print(name, price, comment, shop, sep=' | ')
                csv.writer(f).writerow([name,price,comment,shop])
            except:
                pass

def nextpage():
    driver.find_element_by_css_selector(
        '#J_bottomPage > span.p-num > a.pn-next > em').click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    # driver.maximize_window()  # 最大化窗口
    driver.get('https://jd.com')
    get_product('硬盘')
    for i in range(0, 99):
        drop_down()
        analyse_date()
        nextpage()