import MivMultiPack, asyncio
from MivMultiPack import *
async def main():
    print(await utils.duration(5000))
    
asyncio.run(main())