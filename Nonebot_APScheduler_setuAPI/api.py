import httpx
from .config import config
# 获取json的图片链接
async def handle_image():
    image_data = config.data
    response = httpx.post(config.api_url, params=image_data)
    if response.status_code == 200:
            data = response.json()
            print('连接成功,正在分析json文件')
            image_url = data['data'][0]['urls']['original']
            print(image_url)
            return image_url
    else:
        error = "网络错误,错误码:{response.status_code}"
        print(error)
