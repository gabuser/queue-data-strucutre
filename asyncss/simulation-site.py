import asyncio 

async def requesting_site(time:int, site:str):
    await asyncio.sleep(time)
    print(f'donwloading: {site}')

async def main():
    await asyncio.gather(
        requesting_site(1, 'olamiund.com'),
        requesting_site(1, 'anime.com'),
        requesting_site(3, 'animerool.com')
    )

asyncio.run(main())
