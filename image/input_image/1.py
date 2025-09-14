from http import HTTPStatus
import re
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
import os

prompt = '''
校园里，小猫在奔跑
''' 
# 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
api_key = os.getenv("DASHSCOPE_API_KEY")

print('----同步调用，请等待任务执行----')
rsp = ImageSynthesis.call(api_key=api_key,
                          model="qwen-image",
                          prompt=prompt,
                          n=1,
                          size='1328*1328',
                          prompt_extend=True,
                          watermark=True)
print('response: %s' % rsp)
if rsp.status_code == HTTPStatus.OK:
    # 在当前目录下保存图片
    for result in rsp.output.results:
        file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
        file_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', file_name)
        file_name = "小猫.png"
        save_directory = 'image/output_image'
        save_path = f'{save_directory}/{file_name}'
        with open(save_path, 'wb+') as f:
            f.write(requests.get(result.url).content)
else:
    print('同步调用失败, status_code: %s, code: %s, message: %s' %
          (rsp.status_code, rsp.code, rsp.message))

