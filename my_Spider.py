import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

class my_spider:
    def __init__(self,key,filename):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          "Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
            "Cookie": "csrfToken=_hAng40EOd6VeE8OQHSsKXqQ; "
                      "jsid=SEO-BING-ALL-SY-000001; "
                      "TYCID=ca17c440620011ec891345a44de732f2; "
                      "aliyungf_tc=fc52fdccb06bf3cc99c855f706e32d720df293870d4e04f959c968fd9a9099e9; "
                      "ssuid=411766719; sajssdk_2015_cross_new_user=1; "
                      "bannerFlag=true; searchSessionId=1640051645.80619050;"
                      " _bl_uid=1kkLCxp9fmng13e8XlCmx4hphRb6; "
                      "tyc-user-phone=%255B%252215890118169%2522%255D; "
                      "tyc-user-info={%22state%22:%220%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2215890118169%22};"
                      "tyc-user-info-save-time=1640051980129; "
                      "auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTg5MDExODE2OSIsImlhdCI6MTY0MDA1MTk4MCwiZXhwIjoxNjcxNTg"
                      "3OTgwfQ.GnHFPJQ9bpVdlEO4JIhWFPapqOjiYXAckhXN88_4nRfEMcq5mLGAZ3fXSFi-oGYs8Xtvqyn5MEBafDx9Qi44dg; "
                      "acw_tc=781bad3e16400538352986637e2a599f868f1e6473d10b6ad5c75d8ead5d55; "
                      "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215890118169%22%2C%22first"
                      "_id%22%3A%2217ddab18a3ebc9-0aa95f891f1ef8-4c607a68-2073600-17ddab18a3fdee%22%2C%22props%22%3A%7B%22%24"
                      "latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24"
                      "latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC"
                      "_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id"
                      "%22%3A%2217ddab18a3ebc9-0aa95f891f1ef8-4c607a68-2073600-17ddab18a3fdee%22%7D",
            "Referer": "https://www.tianyancha.com/"
        }
        self.key = key
        self.filname = filename

        with open(self.filname, 'w', encoding='utf-8') as f:
            f.write('公司名,公司类型,电话,邮箱,地址,基本信息\n')
        with open('info.txt', 'w', encoding='utf-8') as f:
            f.write("\n")
    def run(self):
        for i in range(1, 6):
            url = 'https://www.tianyancha.com/search/p{}?key={}&companyType=normal_company'.format(i, quote(self.key))
            html = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(html.text, 'lxml')
            infos = soup.select('.result-list .content .header a')
            for info in infos:
                company_name = info.text
                company_url = info['href']
                print(company_name, company_url)
                html_detail = requests.get(company_url, headers=self.headers)
                soup_detail = BeautifulSoup(html_detail.text, 'lxml')
                data_type = soup_detail.select('div[tyc-event-ch="CompangyDetail.gongshangxinxin"]'
                                               ' .table.-striped-col tbody tr:nth-child(7) td:first-child+td')
                data_tel = soup_detail.select('._phone')
                data_email = soup_detail.select('.email')
                data_address = soup_detail.select('._address .detail-content')
                data_money = soup_detail.select('div[tyc-event-ch="CompangyDetail.gongshangxinxin"] #_container_baseInfo > '
                                                'table > tbody > tr:nth-child(3) > td:nth-child(2) > div')
                data_info = soup_detail.select('div[tyc-event-ch="CompangyDetail.gongshangxinxin"] #_container_baseInfo > '
                                               'table > tbody > tr:nth-child(11) > td:nth-child(2) > span')
                datas = [data_type,data_tel,data_email,data_address,data_money]
                with open(self.filname, 'a+', encoding='utf-8') as f:
                    f.write(company_name+",")
                    index = 0
                    for i in datas:
                        index += 1
                        if(len(i) == 0):
                            f.write(" ,")
                        else:
                            if(index == len(datas)):
                                f.write(i[0].text)
                            else:
                                f.write(i[0].text+",")

                    f.write('\n')

                with open('info.txt','a+',encoding='utf-8') as f:
                    if (len(data_info) == 0):
                        f.write('\n')
                    else:
                        f.write(data_info[0].text+'\n')