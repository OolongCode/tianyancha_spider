import jieba
import re

def word_cut(filename):
    word_dict = {}
    stop_word = {}.fromkeys(['的','经','后','依','不得','依法','须经','批准','和','不','超过','除外','中'])
    with open("info.txt",'r',encoding='utf-8') as f:
        word_lines = f.readlines()
        for word_line in word_lines:
            word_line = re.sub('\W*', '',word_line)
            if word_line != '':
                word_list = []
                word_temp = jieba.lcut(word_line,cut_all=True)
                for i in word_temp:
                    if i not in stop_word:
                        word_list.append(i)
                for i in word_list:
                    if i in word_dict:
                        word_dict[i] += 1
                    else:
                        word_dict[i] = 1

    word_dict_data = list(zip(word_dict.keys(),word_dict.values()))
    return word_dict_data