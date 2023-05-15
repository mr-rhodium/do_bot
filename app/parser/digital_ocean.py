from settings import HEADERS
import aiohttp


async def get_url(url: str) -> list:
    conn = aiohttp.TCPConnector(limit=8, limit_per_host=8)
    async with aiohttp.ClientSession(connector=conn) as session:
        resp = await session.get(url=url, headers=HEADERS)
        return await resp.json()