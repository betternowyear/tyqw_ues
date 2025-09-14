import subprocess
import os
import requests

from http import HTTPStatus
# dashscope sdk >= 1.22.1
from dashscope import VideoSynthesis

def sample_sync_call_t2v():
    # call sync api, will return the result
    print('please wait...')
    rsp = VideoSynthesis.call(model='wan2.2-t2v-plus',
                              prompt='钢琴家在海洋水面上弹钢琴',
                              size='1920*1080')
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print("视频url:",rsp.output.video_url)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    return rsp.output.video_url

def download_video(url, target_folder, file_name):
    # 确保目标文件夹存在
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # 构造目标文件路径
    target_path = os.path.join(target_folder, file_name)
    
    # 下载文件
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        with open(target_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Download completed successfully! File saved to {target_path}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    video_url = sample_sync_call_t2v()
    target_folder = f"video/output_video"  # 替换为你的目标文件夹路径
    file_name = "乡村.mp4"
    download_video(video_url, target_folder, file_name)