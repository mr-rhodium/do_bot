import asyncio
import aiocron


class RedisClaent:

    def get(self):
        pass
    def set(self):
        pass


async def test(param):
    print(f"I test {param}")

    
async def tags():
    pass 

async def content():
    print("I am content")


async def check():
    pass

async def updade():
    pass


async def cron(redis_client):
    cron_min = aiocron.crontab('*/1 * * * *', func=test, args=("At every minute",), start=True)

