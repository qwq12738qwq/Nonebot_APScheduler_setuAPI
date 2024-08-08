from pydantic import BaseSettings

class Config(BaseSettings):
    api_url: str = 'https://api.lolicon.app/setu/v2'
    # 群号,目前只能一个群
    group_id: int = 976025391
    # 时间(时:分)
    hour = '12'
    min = '00'
    # Lolicon.API,配置去看https://api.lolicon.app/#/setu
    data = {
        "r18": 2,
        "num": 1,
        "tag":[
            [],
            ["白丝", "黑丝"],
        ]
    }
config = Config()
