from nonebot.plugin import PluginMetadata
# 插件数据
__plugin_meta__ = PluginMetadata(
    name="Nonebot_APScheduler_setuAPI",
    description="114514",
    usage="1145141919810"
)
from nonebot.adapters.onebot.v11 import MessageSegment, Message
from nonebot import require, get_bot
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
import io
import base64
import httpx
from PIL import Image
from .api import handle_image
from .config import config

@scheduler.scheduled_job("cron", hour=config.hour, minute=config.min)
async def send_image(message=Message):
    bot = get_bot()
    wait_send_url = await handle_image()
    async with httpx.AsyncClient() as client:
        # 把链接转成字符串
        wait_send_url = str(wait_send_url)
        # 获取url的图片
        get_image = await client.get(wait_send_url)
        # 打开图片并存到内存中
        image = Image.open(io.BytesIO(get_image.content))
        img_bytes = io.BytesIO()
        # 保存image字节为png格式
        image.save(img_bytes, format='PNG')
        # base64编码图片
        image_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
        image_handle = MessageSegment.image(f"base64://{image_base64}")
        # 指针归零
        img_bytes.seek(0)
        # 发送图片
        await bot.send_group_msg(
            group_id=config.group_id,
            message=image_handle
)