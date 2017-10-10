import numpy as np
import random

test_map = {'name': 'shu', 'colLen': 5, 'rowLen': 5, 'map': [[{'unknown': False, 'block': False, 'road': True, 'cao': True, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': True, 'shu2': False, 'shu3': True, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': True}, {'unknown': False, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': True, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': True, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}]]}
test_map1 = {'name': 'shu', 'colLen': 5, 'rowLen': 5, 'map': [[{'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': True, 'shu2': False, 'shu3': True, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': True}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': True, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': False, 'road': True, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': False, 'block': True, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}], [{'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': False, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}, {'unknown': True, 'block': False, 'road': False, 'cao': True, 'shu1': False, 'shu2': False, 'shu3': False, 'shu4': False}]]}

# 定位警察的位置
def loc_shu(map_arry, row_len, col_len):
    shu_list = []
    for row in range(row_len):
        for col in range(col_len):
            # 先列
            if len(shu_list) == 4:
                return shu_list
            if map_arry[col][row]['shu1'] == True:
                shu_list.append((row, col))
            if map_arry[col][row]['shu2'] == True:
                shu_list.append((row, col))
            if map_arry[col][row]['shu3'] == True:
                shu_list.append((row, col))
            if map_arry[col][row]['shu4'] == True:
                shu_list.append((row, col))


    return shu_list

# 判断是否发现小偷
def is_find(game_map):
    row_len = game_map['rowLen']
    col_len = game_map['colLen']
    map_arry = np.array(game_map['map'])
    res = loc_shu(map_arry, row_len, col_len)
    # print(res)
    i = 0
    for item in res:
        i = i+1
        cyc_row = item[0]
        cyc_col = item[1]
        for irow in range(cyc_row-1, cyc_row+2):
            for icol in range(cyc_col-1, cyc_col+2):
                # print(irow,icol)
                if map_arry[irow][icol]['cao'] == True:
                    # print(irow-cyc_row,icol-cyc_col)
                    return (i, irow-cyc_row,icol-cyc_col)



# print(is_find(test_map))
# print(loc_shu(test_map))
resp = {
    "shu1": random.randint(0, 4),
    "shu2": random.randint(0, 4),
    "shu3": random.randint(0, 4),
    "shu4": random.randint(0, 4)
}
result = is_find(test_map)
if result:
    tmp = 'shu%s' % result[0]
    # print(tmp)
    if result[2] == -1:
        resp[tmp] = 3
    elif result[2] == 1:
        resp[tmp] = 2
    elif result[1] == -1:
        resp[tmp] = 0
    elif result[1] == 1:
        resp[tmp] = 1

print(resp)
