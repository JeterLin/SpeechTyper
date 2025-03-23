import sherpa_onnx
import time

# 假设模型文件路径如下
model_path = "models/bi-punct-ct-transformer-zh-en/model.onnx"
model_config = sherpa_onnx.OfflinePunctuationModelConfig(
    ct_transformer=model_path,  # 指定模型路径
)
# 创建模型配置
config = sherpa_onnx.OfflinePunctuationConfig(
    model=model_config,
)

# 创建模型实例
punctuator = sherpa_onnx.OfflinePunctuation(config)

# 输入文本
text = "你知道这个句子是什么god is a girl do you believe it can you receive it"

# 进行推理
punctuated_text = punctuator.add_punctuation(text)

# 输出结果
print("原始文本:", text)
print("加标点后的文本:", punctuated_text)

time.sleep(5)