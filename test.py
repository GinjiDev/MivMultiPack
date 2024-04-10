import MivMultiPack, asyncio
from MivMultiPack import *
async def main():
    print(await UTILS.duration(5000))
    
asyncio.run(main())