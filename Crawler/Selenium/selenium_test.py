
# import time

# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.set_page_load_timeout(30)

# browser.get('https://www.amazon.cn/b/ref=amb_link_12?ie=UTF8&node=1916018071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-leftnav&pf_rd_r=GW32ANNMAZYRHJHX59XA&pf_rd_r=GW32ANNMAZYRHJHX59XA&pf_rd_t=101&pf_rd_p=c9eb3ba4-9554-4577-a26d-83f14c5be7c4&pf_rd_p=c9eb3ba4-9554-4577-a26d-83f14c5be7c4&pf_rd_i=658390051')

# page_info = browser.find_element_by_css_selector("#pagn > span.pagnDisabled")

# print(page_info)



from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.get('http://www.17huo.com/search.html?sq=2&keyword=%E7%BE%8A%E6%AF%9B')
page_info = browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')
# print(page_info.text)
pages = int((page_info.text.split('，')[0]).split(' ')[1])
for page in range(pages):
    if page > 2:
        break
    url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)   # 不然会load不完整
    goods = browser.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')
    print('Page: %d has %d goods' % ((page + 1), len(goods)))
    
    for good in goods:
        try:
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            price = good.find_element_by_css_selector('div > a > span').text
            #print(title, price)
            with open("selenium.txt",'a') as f:
            	f.write(title+"--"+price)
        except:
            #print(good.text)
            with open("selenium_error.txt",'a') as f:
            	f.write(good.text)

