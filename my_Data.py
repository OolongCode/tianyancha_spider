# data operate
def bar_data(money_temp, types):
    money = []
    for i in money_temp:
        money.append(float(i[:-4]))

    money.sort()

    dict_money_type = {
        'A': [],
        'B': [],
        'C': [],
        'D': []
    }
    dict_money_data = {
        'A': [],
        'B': [],
        'C': [],
        'D': []
    }
    for i in range(len(types)):
        if types[i][:4] == "股份有限":
            dict_money_type['A'].append(money[i])
        elif types[i][:4] == "有限责任":
            dict_money_type['B'].append(money[i])
        elif types[i][:4] == "其他股份":
            dict_money_type['C'].append(money[i])
        elif types[i][:4] == "其他有限":
            dict_money_type['D'].append(money[i])

    for i in dict_money_type:
        temp_dict = {}
        for j in dict_money_type[i]:
            if j < 1000.0:
                if 'A' in temp_dict:
                    temp_dict['A'] += 1
                else:
                    temp_dict['A'] = 1
            elif 10000.0 > j > 1000.0:
                if 'B' in temp_dict:
                    temp_dict['B'] += 1
                else:
                    temp_dict['B'] = 1
            elif 100000.0 > j > 10000.0:
                if 'C' in temp_dict:
                    temp_dict['C'] += 1
                else:
                    temp_dict['C'] = 1
            elif 1000000.0 > j > 100000.0:
                if 'D' in temp_dict:
                    temp_dict['D'] += 1
                else:
                    temp_dict['D'] = 1
            else:
                if 'E' in temp_dict:
                    temp_dict['E'] += 1
                else:
                    temp_dict['E'] = 1
        for k in temp_dict:
            dict_money_data[i].append(temp_dict[k])

    for i in dict_money_data:
        if len(dict_money_data[i]) < 5:
            diff = 5 - len(dict_money_data[i])
            for j in range(diff):
                dict_money_data[i].append(0)
    return dict_money_data


def map_data(addresses):
    dict_address = {}

    for i in addresses:
        if i[:6] == '中国（上海）' or i[:2] == '嘉定':
            if '上海' in dict_address:
                dict_address['上海'] += 1
            else:
                dict_address['上海'] = 1
        elif i[:4] == '华苑产业':
            if '天津' in dict_address:
                dict_address['天津'] += 1
            else:
                dict_address['天津'] = 1
        elif i[:6] == '中国（四川）' or i[:2] == '成都':
            if '四川' in dict_address:
                dict_address['四川'] += 1
            else:
                dict_address['四川'] = 1
        elif i[:2] == '哈尔':
            if '哈尔滨' in dict_address:
                dict_address['黑龙江'] += 1
            else:
                dict_address['黑龙江'] = 1
        elif i[:2] == '广州' or i[:2] == '深圳':
            if '广东' in dict_address:
                dict_address['广东'] += 1
            else:
                dict_address['广东'] = 1
        elif i[:2] == '福州' or i[:2] == '厦门':
            if '福建' in dict_address:
                dict_address['福建'] += 1
            else:
                dict_address['福建'] = 1
        elif i[:2] == '合肥':
            if '安徽' in dict_address:
                dict_address['安徽'] += 1
            else:
                dict_address['安徽'] = 1
        elif i[:2] == '长沙':
            if '湖南' in dict_address:
                dict_address['湖南'] += 1
            else:
                dict_address['湖南'] = 1
        elif i[:2] == '温州' or i[:2] == '杭州' or i[:2] == '上城':
            if '浙江' in dict_address:
                dict_address['浙江'] += 1
            else:
                dict_address['浙江'] = 1
        elif i[:2] == '昆山' or i[:2] == '南京':
            if '江苏' in dict_address:
                dict_address['江苏'] += 1
            else:
                dict_address['江苏'] = 1
        elif i[:2] == '荆门':
            if '湖北' in dict_address:
                dict_address['湖北'] += 1
            else:
                dict_address['湖北'] = 1
        elif i[:2] == '济南' or i[:2] == '烟台':
            if '山东' in dict_address:
                dict_address['山东'] += 1
            else:
                dict_address['山东'] = 1
        else:
            if i[:2] in dict_address:
                dict_address[i[:2]] += 1
            else:
                dict_address[i[:2]] = 1

    address_data = list(zip(dict_address.keys(), dict_address.values()))
    return address_data


def pie_data(types):
    dict_type = {}
    for i in types:
        if i[:4] in dict_type:
            dict_type[i[:4]] += 1
        else:
            dict_type[i[:4]] = 1
    dict_type_data = [list(z) for z in zip(dict_type.keys(), dict_type.values())]
    return dict_type_data
