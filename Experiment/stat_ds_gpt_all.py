import json
# 计算原始和扰动后准确率 
def get_accuracy(data):
    data_len = len(data)
    acc_before_count = 0
    acc_after_count = 0
    count = 0
    print ("总样本数：", data_len)
    for i in range(len(data)):
        res = data[i]["res"][0]
        print("原始res：", res)
        if res < 0.5:
            acc_before_count += 1
        for j in range(len(data[i]["reorderRes"])):
            # if len(data[i]["reorderRes"][j]) <= 1:
            #     fail_count += 1
            #     continue
            count += 1
            if data[i]["reorderRes"][j][0] < 0.5:
                acc_after_count += 1
    # print ("原始准确率：", acc_before_count / data_len)
    # print ("扰动后准确率：", acc_after_count / (data_len * 10 - fail_count))
    return acc_before_count / len(data), acc_after_count / count
# 计算翻转比例，
def get_flip_ratio(data):
    data_len = len(data)
    flip_count = 0
    print ("总样本数：", data_len)
    for i in range(len(data)):
        res = data[i]["res"][0]
        print("原始res：", res)
        for j in range(len(data[i]["reorderRes"])):
            flag = -1
            if res > 0.5:
                if data[i]["reorderRes"][j][0] < 0.5:
                    flag = 1
                    print("翻转res：", data[i]["reorderRes"][j][0])
                else:
                    flag = 0
            else:
                if data[i]["reorderRes"][j][0] > 0.5 :
                    flag = 1
                    print("翻转res：", data[i]["reorderRes"][j][0])
                else:
                    flag = 0
            if flag == 1:
                flip_count += 1
                break
    # print ("翻转比例：", flip_count / data_len)
    return flip_count / len(data)

# 计算couple importance
def get_couple_importance(data):
    data_len = len(data)
    count = 0
    print ("总样本数：", data_len)
    diff_sum = 0
    for i in range(len(data)):
        res = data[i]["res"][0]
        print("原始res：", res)
        for j in range(len(data[i]["reorderRes"])):
            diff_sum += abs(data[i]["reorderRes"][j][0] - res)
            count += 1
    # print ("couple importance：", diff_sum / (data_len * 10 - fail_count))
    return diff_sum / count

    
if __name__ == '__main__':
    file_path = 'ds_sst-2_two.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    flip_ratio = get_flip_ratio(data)
    acc_before, acc_after = get_accuracy(data)
    couple_importance = get_couple_importance(data)
    print ("翻转比例：", flip_ratio)
    print ("原始准确率：", acc_before)
    print ("扰动后准确率：", acc_after)
    print ("couple importance：", couple_importance)
