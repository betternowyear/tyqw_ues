import os
import requests
import dashscope

text = "你在逗我啊！"
response = dashscope.audio.qwen_tts.SpeechSynthesizer.call(
    model="qwen-tts",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    text=text,
    voice="Ethan",
)
audio_url = response.output.audio["url"]
save_path = r"audio\output_audio\你在逗我3.wav"  # 自定义保存路径

try:
    response = requests.get(audio_url)
    response.raise_for_status()  # 检查请求是否成功
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print(f"音频文件已保存至：{save_path}")
except Exception as e:
    print(f"下载失败：{str(e)}")