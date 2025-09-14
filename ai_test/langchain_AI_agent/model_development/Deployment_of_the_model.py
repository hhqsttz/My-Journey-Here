
from modelscope import snapshot_download
from sentence_transformers import SentenceTransformer

from huggingface_hub import snapshot_download
#
# #1.下载huggingface依赖包 pip install -U huggingface_hub
# #2.配置国内镜像网站  HF_ENDPOINT = https://hf_mirror.com
# #3.将缓存目录环境变量修改到你想指定的位置
#
# #huggingface_hub下载
#
# repo_id = "Qwen/Qwen3-Embedding-0.6B"
# # cache_dir = "E:\model\embedding"  #存放缓存目录
# revision = "main"
# resume_download = True    #间断点下载
#
# #modelscope下载
#
# # repo_id = "Qwen/Qwen3-Embedding-0.6B"
# # # cache_dir = "E:\model\embedding"
# # revision = "master"
# # resume_download = True
# #
# model_dir = snapshot_download(
#     repo_id=repo_id,
#     # cache_dir=cache_dir,
#     revision=revision ,
# )
# print(f"✅ 模型已完整下载到: {model_dir}")
#
# #模型的部署
# model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
#
# print("✅ 模型加载成功！")
#
#
