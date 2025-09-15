from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer



# # Load the model
# model = SentenceTransformer(
#     "Qwen/Qwen3-Embedding-0.6B"
# )
# a=model.encode(
# ["我爱你"]*60,
# show_progress_bar = True   #进度条
# )
# print(a)

#     代码示例

# model_kwargs = {'device': 'cpu/cuda'}           #使用Cpu/Gpu 计算
# encode_kwargs = {'normalize_embeddings': True}  #是否归一化
# hf = HuggingFaceEmbeddings(    model_name=model_name,    model_kwargs=model_kwargs,    encode_kwargs=encode_kwargs)
m1 = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-0.6B",
    model_kwargs = {'device': "cpu"},
    encode_kwargs = {'normalize_embeddings': True}
)
m2 = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-0.6B",
    model_kwargs = {'device': "cuda"},
    encode_kwargs = {'normalize_embeddings': True}
)
a=m1.embed_documents(["你好"]*2)
b=m2.embed_documents(["你好"]*2)
print("m1开始打印")
print(len(a))
print("m2开始打印")
print(b)




