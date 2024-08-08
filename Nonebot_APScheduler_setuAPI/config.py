from pydantic import BaseSettings

class Config(BaseSettings):
    api_url: str = 'https://api.lolicon.app/setu/v2'
    # 群号,目前只能一个群
    group_id: int = 
    # 时间(时:分)
    hour = '12'
    min = '00'
    # Lolicon.API,配置去看https://api.lolicon.app/#/setu
    # r18: 0关闭 1开启 2混合, 建议修改成0
    data = {
        "r18": 2,
        "num": 1,
        "tag":[
            [],
            ["白丝", "黑丝"],
        ]
    }
config = Config()
