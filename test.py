import MivMultiPack, asyncio
from MivMultiPack import ASYNCUTILS
async def main():
    print(await ASYNCUTILS.duration(5000))
    
asyncio.run(main())