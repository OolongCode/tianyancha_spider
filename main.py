import time
import pandas as pd
import sys
from my_Spider import my_spider
from my_Data import *
from my_Graph import my_graph
from my_Word import word_cut
start = time.time()
# spider = my_spider('信息','company.csv')
# spider.run()

data = pd.read_csv('company.csv')
names = data['公司名'].values
types = data['公司类型'].values
addresses = data['地址'].values
money_temp = data['资金'].values

word_data = word_cut("info.txt")

obj_graph = my_graph(bar_data(money_temp,types),map_data(addresses),pie_data(types),word_data)
obj_graph.bar_graph("企业注册资金")
obj_graph.pie_graph("企业类型分布")
obj_graph.map_graph("企业区域分布","企业数")
obj_graph.wd_graph("企业经营范围词云")
# obj_graph.page_init("index.html")
obj_graph.page_build("index.html","chart_config.json","my_index.html")
end = time.time()
print(end - start)
