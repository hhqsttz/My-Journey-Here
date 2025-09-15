import ast
import numpy as np
import pandas as pd

# 全局变量，用于缓存模型实例
model = None


def get_embedding_model():
    """
    完全延迟加载模型，只有在调用时才导入和初始化
    这样可以避免PyCharm在文件打开时就分析大型库
    """
    global model

    # 如果模型已经加载，直接返回
    if m1 is not None:
        return model

    # 延迟导入 - PyCharm不会在打开文件时就分析这些库
    try:
        from langchain_huggingface import HuggingFaceEmbeddings
    except ImportError:
        raise ImportError("请安装langchain-huggingface库: pip install langchain-huggingface")

    print("正在加载嵌入模型...")
    model = HuggingFaceEmbeddings(
        model_name="Qwen/Qwen3-Embedding-0.6B",
        model_kwargs={'device': "cpu"},
        encode_kwargs={'normalize_embeddings': True}
    )
    print("模型加载完成")
    return model



def text_processing(source_file,output_file):
    df = pd.read_csv(source_file)
    df = df[["z1","z2"]]
    df = df.dropna()
    df['text'] = "z1:"+df.z1.str.strip()+"z2:"+df.z2.str.strip()
    m1=get_embedding_model()
    #向量化文件
    #1.少量
    # df["embeddings"] = m1.embed_documents(df.text.tolist())
    #2.少量多次
    batch_size = 32
    embeddings = []
    for i in range(0, len(df), batch_size):
        batch_texts = df.text.tolist()[i:i+batch_size]
        embeddings.extend(m1.embed_documents(batch_texts))
    df["embeddings"]=embeddings
    #向量保存到文件中就变成了字符串了
    df.to_csv(output_file)
def cosine_distance(a,b):
    #计算余弦相似度=向量点积/两个向量欧几里得范数相乘(未使用归一化)
    dot_product = np.dot(a, b)
    # 以下三种写法完全等价：
    magnitude_product = np.linalg.norm(a) * np.linalg.norm(b)
    # 或者：euclidean_norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    # 或者：l2_norm_product = np.linalg.norm(vec1, ord=2) * np.linalg.norm(vec2, ord=2)
    return dot_product / magnitude_product

def cosine_distance1(a,b):
    #使用归一化的方式 encode_kwargs = {'normalize_embeddings': True}
    return  np.dot(a, b)
def search_file(intput,file,top=3):
    a = m1.embed_documents([intput])[0]
    df = pd.read_csv(file)
    df["embeddings_vector"]=df["embeddings"].apply(ast.literal_eval)
    df["cosine_distance"] = df.embeddings_vector.apply(lambda x : cosine_distance1(a,x))
    res=(
    df.sort_values("cosine_distance",ascending=False)
    .head(top)
    .text.str.strip()
    .str.replace("z1:", "", regex=True)
    .str.replace("z2:", "", regex=True)
    )
    for r in res:
        print(r)
        print("-"*30)
if __name__ == '__main__':

    text_processing(source_file="./source.csv",output_file="./output.csv")
    # 文件路径有相对和绝对，
    # 如果在同一个目录下用相对路径
    # 同一个文件夹./source.csv，或者source.csv
    # 上一个文件夹../source.csv
    # 不在一个地方用绝对路径