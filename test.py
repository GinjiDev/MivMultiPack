import MivMultiPack, asyncio
from MivMultiPack import Utils
async def main():
    print(await Utils.duration(5000))
    
asyncio.run(main())