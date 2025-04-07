import requests
import re
import json
import time
import os

def call_deepseek_api(message):
    # 设置 DeepSeek API Key
    API_KEY = "" 

    # DeepSeek API 端点
    API_URL = "https://api.deepseek.com/v1/chat/completions"
    # 定义请求头
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"""请判断以下评论的情感（只能是‘正面’或‘负面’），并按照以下格式输出：\n\n"
            "正面: XX%\n负面: XX%\n\n"
            "评论：{message}"""
    # 发送请求到 DeepSeek API
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个文本分类助手"},
            {"role": "user", "content":prompt
            }
        ],
        "max_tokens": 20,  # 生成足够的输出
        "temperature": 0    # 设为 0，确保输出稳定
    }

    # 发送 API 请求
    response = requests.post(API_URL, headers=headers, json=payload)
    response_data = response.json()

    # 提取 DeepSeek 返回的文本
    output_text = response_data["choices"][0]["message"]["content"].strip()

    # 使用正则表达式提取正面和负面的概率
    match = re.findall(r"(正面|负面):\s*(\d+)%", output_text)

    # 解析概率
    probabilities = {label: int(prob) / 100 for label, prob in match}

    # 输出最终结果
    print("DeepSeek 预测类别概率:")
    positive_probability = probabilities.get('正面', 'N/A')
    negative_probability = probabilities.get('负面', 'N/A')
    return positive_probability, negative_probability

if __name__ == "__main__":
    file_path = 'lstm_imdb_two.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for i in range(20):
        start_time = time.time()
        print("=====第", i, "条数据=====")
        myinput = data[i]['input']
        pos_res, neg_res = call_deepseek_api(myinput)
        time.sleep(0.5)
        reorderRes = []
        for j in range(len(data[i]["reorderList"])):
            print("=====第", j, "条=====")
            # if len(data[i]["reorderRes"][j]) <= 1:
            #     continue
            message = data[i]["reorderList"][j]["chosenText"]
            pos_res1, neg_res1 = call_deepseek_api(message)
            reorderRes.append([pos_res1, neg_res1])
        write_data = {"index": i, "input":myinput,"res":[pos_res, neg_res],"reorderRes":reorderRes}
        out_file = 'ds_imdb_two.json'
        if os.path.exists(out_file):
            with open(out_file, 'r', encoding='utf-8') as f:
                Write_data = json.load(f)
        else:
            Write_data = []
        Write_data.append(write_data)
        with open(out_file, 'w', encoding='utf-8') as f:
                json.dump(Write_data, f, ensure_ascii=False, indent=4)
        print("耗时：", time.time()-start_time)
        print("=========================================")
