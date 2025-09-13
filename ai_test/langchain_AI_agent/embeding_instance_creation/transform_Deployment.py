

from sentence_transformers import SentenceTransformer

# from embeding_instance_creation.Deployment_of_the_model import model_dir

# Load the model
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
a=model.encode(
["我爱你"]*60,
show_progress_bar = True
)
print(a)
print(f"模型默认输出维度: {model.get_sentence_embedding_dimension()}")


# 看起来你在查看 `SentenceTransformer.encode()` 方法的参数定义。这是一个非常强大的方法，提供了很多选项来控制嵌入生成的过程。让我为你详细解释每个参数的作用和用法：
#
# # 🎯 SentenceTransformer.encode() 方法参数详解
#
# ## 📋 参数概述
#
# ```python
# def encode(
#     sentences: str | list[str] | ndarray,           # 要编码的文本
#     prompt_name: str | None = None,                 # 预定义提示模板名称
#     prompt: str | None = None,                      # 自定义提示文本
#     batch_size: int = 32,                           # 批处理大小
#     show_progress_bar: bool | None = None,          # 是否显示进度条
#     output_value: Literal["sentence_embedding", "token_embeddings"] | None = "sentence_embedding",  # 输出类型
#     precision: Literal["float32", "int8", "uint8", "binary", "ubinary"] = "float32",  # 精度格式
#     convert_to_numpy: bool = True,                  # 转换为numpy数组
#     convert_to_tensor: bool = False,                # 转换为PyTorch张量
#     device: str | list[str | device] | None = None, # 输出设备
#     normalize_embeddings: bool = False,             # 是否标准化嵌入
#     truncate_dim: int | None = None,                # 截断维度
#     pool: dict[Literal["input", "output", "processes"], Any] | None = None,  # 多进程池
#     chunk_size: int | None = None,                  # 分块大小
#     **kwargs: Any                                   # 其他参数
# ) -> list[Tensor] | ndarray | Tensor | dict[str, Tensor] | list[dict[str, Tensor]]:
# ```
#
# ## 🎪 核心参数详解
#
# ### 1. `sentences` - 输入文本
# ```python
# # 单句文本
# embeddings = model.encode("这是一个句子")
#
# # 多句文本列表
# embeddings = model.encode(["句子1", "句子2", "句子3"])
#
# # numpy数组（包含字符串）
# sentences_array = np.array(["文本1", "文本2"])
# embeddings = model.encode(sentences_array)
# ```
#
# ### 2. `batch_size` - 批处理大小
# ```python
# # 小批量（内存较少时）
# embeddings = model.encode(sentences, batch_size=16)
#
# # 大批量（性能优化）
# embeddings = model.encode(sentences, batch_size=64)
#
# # 自动调整（根据硬件）
# embeddings = model.encode(sentences, batch_size="auto")
# ```
#
# ### 3. `output_value` - 输出类型
# ```python
# # 默认：句子嵌入（推荐）
# sentence_embeddings = model.encode(sentences, output_value="sentence_embedding")
#
# # 获取所有token的嵌入（用于特定任务）
# token_embeddings = model.encode(sentences, output_value="token_embeddings")
# # 返回格式：{"input_ids": [...], "token_embeddings": [...]}
# ```
#
# ### 4. 输出格式控制
# ```python
# # 默认返回numpy数组（推荐）
# embeddings = model.encode(sentences, convert_to_numpy=True)
#
# # 返回PyTorch张量
# tensor_embeddings = model.encode(sentences, convert_to_tensor=True)
#
# # 指定输出设备
# gpu_embeddings = model.encode(sentences, device="cuda")
# ```
#
# ### 5. 嵌入后处理
# ```python
# # 标准化嵌入向量（单位长度）
# normalized_embeddings = model.encode(sentences, normalize_embeddings=True)
#
# # 截断到指定维度
# truncated_embeddings = model.encode(sentences, truncate_dim=256)
# ```
#
# ### 6. 进度和性能控制
# ```python
# # 显示进度条（处理大量文本时）
# embeddings = model.encode(sentences, show_progress_bar=True)
#
# # 使用多进程加速
# embeddings = model.encode(sentences, pool={"processes": 4})
#
# # 分块处理超大文本
# embeddings = model.encode(sentences, chunk_size=1000)
# ```
#
# ## 🚀 实用示例组合
#
# ### 示例1：基础用法
# ```python
# # 最简单的用法
# sentences = ["今天天气真好", "人工智能很有趣", "机器学习正在改变世界"]
# embeddings = model.encode(sentences)
#
# print(f"嵌入形状: {embeddings.shape}")  # (3, 1024)
# ```
#
# ### 示例2：高性能处理
# ```python
# # 处理大量文本的优化配置
# large_corpus = ["文本{}".format(i) for i in range(1000)]
#
# embeddings = model.encode(
#     large_corpus,
#     batch_size=64,              # 合适的批处理大小
#     show_progress_bar=True,     # 显示进度
#     normalize_embeddings=True,  # 标准化便于相似度计算
#     device="cuda" if torch.cuda.is_available() else "cpu"
# )
# ```
#
# ### 示例3：高级功能
# ```python
# # 获取token级嵌入用于特定分析
# text = "自然语言处理很有趣"
# result = model.encode(
#     text,
#     output_value="token_embeddings",  # 获取token嵌入
#     convert_to_tensor=True           # 返回张量
# )
#
# print("Token IDs:", result["input_ids"])
# print("Token嵌入形状:", result["token_embeddings"].shape)
# ```
#
# ### 示例4：内存优化
# ```python
# # 内存受限环境下的配置
# embeddings = model.encode(
#     sentences,
#     batch_size=8,                   # 小批量减少内存使用
#     precision="int8",               # 使用8位整数节省空间
#     truncate_dim=512,               # 截断到较小维度
#     convert_to_numpy=True           # 使用numpy而非PyTorch
# )
# ```
#
# ## 📊 参数选择指南
#
# | 场景 | 推荐参数配置 |
# | :--- | :--- |
# | **常规使用** | `batch_size=32, convert_to_numpy=True` |
# | **相似度计算** | `normalize_embeddings=True` |
# | **大规模处理** | `batch_size=64, show_progress_bar=True, pool={"processes": 4}` |
# | **内存优化** | `batch_size=16, precision="int8", truncate_dim=256` |
# | **GPU加速** | `device="cuda", convert_to_tensor=True` |
# | **详细分析** | `output_value="token_embeddings"` |
#
# ## ⚠️ 注意事项
#
# 1.  **内存管理**：大批量处理会占用更多内存，请根据硬件调整 `batch_size`
# 2.  **精度权衡**：降低精度（如 `int8`）可以节省空间但可能损失一些精度
# 3.  **标准化时机**：如果后续要进行余弦相似度计算，建议设置 `normalize_embeddings=True`
# 4.  **设备一致性**：确保输入设备和模型设备一致，避免不必要的数据传输
#
# 这些参数让你能够精细控制嵌入生成过程，适应不同的应用场景和硬件环境。根据你的具体需求选择合适的参数组合！