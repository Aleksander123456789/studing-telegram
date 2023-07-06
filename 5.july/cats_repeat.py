import asyncio
import aiohttp

url: str = 'https://api.thecatapi.com/v1/images/search?limit=10'

def delete_cats():
    for file in 

async def download_cat(session: aiohttp.ClientSession, url: str, n:int):


    format = url[-3:]

    response = await session.get(url)
    response_bytes = await response.read()

    with open(f'cats/cat{n}.jpg', 'wb') as file:
        file.write(response_bytes)

    print(f'cat{n}.{format}')




async def get_cats():
    async with aiohttp.ClientSession as session: #даёт гарантию на закрытие сессии
        response = await session.get(url)
        json: list[dict[str, str]] = await response.json

        url_cats = []
        for data in json:
            url_cats.append

        tasks = []
        for i in range(len(url_cats)):
            tasks.append(download(session, url_cats[i], i))
def main():
    delete_cats()
    asyncio.run(get_cats())


asyncio.run(main())


