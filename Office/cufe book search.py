from selenium import webdriver
from pyquery import PyQuery as pq
import requests
from mail import sendmail



def getdetailurl(bookname):
    try:
        driver = webdriver.PhantomJS()
        driver.get('http://202.205.213.113:8080/opac/search.php')
        driver.find_element_by_xpath('//*[@id="strText"]').send_keys(bookname)
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/fieldset/div/form/div/input[3]').click()
        doc = pq(driver.page_source)
        if doc('.book_list_info'):
            info = doc('.book_list_info')
            # shujia = info('h3').text()
            # status = info('p span').text()
            detailurl = 'http://202.205.213.113:8080/opac/' + info('p a').attr('href')
            return detailurl
        else:
            return '没有此书'
    except:
        pass


def getinfo(url):
    result = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    detail = pq(res.text)
    binformation = []
    bookinfo = detail('.booklist').items()
    for b in bookinfo:
        binformation.append(b.text())
    dinformation = []
    for d in detail('#item tr').items():
        dinformation.append(d.text().replace('\n', ''))
    result.append(binformation[0].replace('\n', ''))
    result.append(binformation[1].replace('\n', ''))
    result = result + dinformation[1:]
    return result


def booklist(i):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    wsbook = 'http://www.allsagesbooks.com/top10/index.asp?reno={page}'
    url = wsbook.format(page=i)
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    doc = pq(r.text)
    book = [x.replace('《', '').replace('》', '') for x in
            doc.text().replace('排行榜', '').replace('排名', '').replace('书\xa0 名', '').split('\n') if x][1::2]
    return book



# booknamelist = pd.read_excel('wsbook.xls')[:20]
# book = [x[0].strip('(精)') for x in booknamelist.values]
# for b in book:
#     url = getdetailurl(b)
#     if url == '没有此书':
#         li = '%s  没有找到'%b
#         with open('wsbooknotfind.txt','a+') as f:
#             f.write(li)
#     else:
#         res = getinfo(url)
#         with open('wsbook.txt','a+') as f:
#             content = '---'.join(res)
#             f.write(content)

while True:
    putinbook = input('请输入要发送的书籍信息，若有多本，以逗号隔开')
    booknamelist = [x for x in putinbook.split('，') if x]
    for b in booknamelist:
        url = getdetailurl(b)
        if url == '没有此书':
            res = '%s  没有找到'%b
        else:
            res = getinfo(url)
        data = '\n'.join(res)
        result = sendmail('%s'%b, data)
        print(result)

