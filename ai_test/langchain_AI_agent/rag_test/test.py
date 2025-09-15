import numpy as np
import psutil

def cosine_distance(a,b):
    #计算余弦相似度=向量点积/两个向量欧几里得范数相乘(未使用归一化)
    dot_product = np.dot(a, b)
    # 以下三种写法完全等价：
    magnitude_product = np.linalg.norm(a) * np.linalg.norm(b)
    # 或者：euclidean_norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    # 或者：l2_norm_product = np.linalg.norm(vec1, ord=2) * np.linalg.norm(vec2, ord=2)
    return dot_product / magnitude_product

if __name__ == '__main__':
    # a1 = cosine_distance([0,1],[1,0])
    # print(a1)
    # # 查看CPU占用最高的进程
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        if proc.info['cpu_percent'] > 10:
            print(proc.info)