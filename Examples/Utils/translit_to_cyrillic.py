import asyncio
from MivMultiPack import ASYNCUTILS

async def main():
    print(await ASYNCUTILS().translit_to_cyrillic(translit="wow"))
    
asyncio.run(main())