# from openai import OpenAI
# from langchain_openai import OpenAIEmbeddings
# from langchain_huggingface import HuggingFaceEmbeddings
# from env_test import OPENAI_BASE_URL, OPENAI_API_KEY, BASE_URL, BASE_API_KEY
# openai官方版本
# clint = OpenAI(
#     base_url=BASE_URL,
#     api_key=BASE_API_KEY,
# )
#
# a=clint.embeddings.create(
#     model="text-embedding-3-large",  #举例
#     dimensions=256,
#     input="我是人"
# )
#
# print(a.data[0].embedding)
# print(len(a.data[0].embedding))
#
#
#
# langchain集成openai版本
# emb= OpenAIEmbeddings(
#     base_url=OPENAI_BASE_URL,
#     api_key=OPENAI_API_KEY,
#     model="emb.name",
#     dimensions=256 #维度设置
#
# )
# LOCAL_emb= OpenAIEmbeddings(
#     base_url=BASE_URL,
#     api_key=BASE_API_KEY,
#     model="LOCAL_emb.name",
#     dimensions=256 #维度设置
# )
# # emb调用
# a1 = emb.embed_documents(
#     texts=[
#         "文档1",
#         "文档2"
#     ]
# )
# print(a1[0]) #打印文档1的向量
# print(a1[1]) #打印文档2的向量
# print(len(a1[1])) #打印文档2的向量维度大小
#
# langchain集成huggingface的版本
#
# model_name = "sentence-transformers/all-mpnet-base-v2"
# model_kwargs = {'device': 'cpu/cuda'}           #使用Cpu/Gpu 计算
# encode_kwargs = {'normalize_embeddings': True}  #是否归一化
# hf = HuggingFaceEmbeddings(    model_name=model_name,    model_kwargs=model_kwargs,    encode_kwargs=encode_kwargs)
# # hf调用
# a2 = hf.embed_documents(
#     texts=[
#         "文档1",
#         "文档2"
#     ]
# )
# print(a2[0]) #打印文档1的向量
# print(a2[1]) #打印文档2的向量
# print(len(a2[1])) #打印文档2的向量维度大小
