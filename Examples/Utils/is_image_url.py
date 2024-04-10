import asyncio
from MivMultiPack import ASYNCUTILS

async def main():
    var = await ASYNCUTILS().is_image_url(url="ссылка на картинку")
    print(var)
    
asyncio.run(main())