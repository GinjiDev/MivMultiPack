import asyncio
from MivMultiPack import ASYNCUTILS

async def main():
    print(await ASYNCUTILS().duration(ms=307000))
    
    var = await ASYNCUTILS().duration(ms=307000)
    
    hour, min, sec = var
    print(f"часов - {hour}, минут - {min}, секунд - {sec}")
    
asyncio.run(main())