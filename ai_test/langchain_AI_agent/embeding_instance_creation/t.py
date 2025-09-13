import os

from transformers import TRANSFORMERS_CACHE
#
# # 获取 TRANSFORMERS_CACHE 的值（如果存在）
# transformers_cache = os.environ.get('TRANSFORMERS_CACHE')
# print(f"TRANSFORMERS_CACHE: {transformers_cache}")
#
#
#
# model_path = r"E:\model\embedding\Qwen\Qwen3-Embedding-0___6B"
#
# # 检查模型文件是否完整
# required_files = [
#     'config.json',           # 模型配置
#     'pytorch_model.bin',     # 或 model.safetensors
#     'vocab.json',            # 词汇表
#     'tokenizer.json',        # 分词器
#     'tokenizer_config.json', # 分词器配置
#     'special_tokens_map.json' # 特殊token映射
# ]
#
# print("模型目录内容:")
# for file in os.listdir(model_path):
#     print(f"  {file}")
#
# print("\n检查必要文件:")
# for file in required_files:
#     file_path = os.path.join(model_path, file)
#     if os.path.exists(file_path):
#         print(f"✅ {file}")
#     else:
#         print(f"❌ {file} - 缺失")
#
#
# model_path = r"E:\model\embedding\Qwen\Qwen3-Embedding-0___6B"
#
# # 检查所有文件，寻找可能的权重文件
# all_files = os.listdir(model_path)
# print("目录中的所有文件:")
# for file in all_files:
#     print(f"  {file}")
#
# # 检查常见的权重文件格式
# weight_files = [f for f in all_files if any(ext in f for ext in
#                 ['.bin', '.safetensors', '.pt', '.pth', 'model.'])]
# print(f"\n可能的权重文件: {weight_files}")
print(os.environ.get('HF_ENDPOINT'))


# 打印当前设置的缓存路径
print("HF_HOME:", os.environ.get('HF_HOME'))
print("MODELSCOPE_CACHE:", os.environ.get('MODELSCOPE_CACHE'))