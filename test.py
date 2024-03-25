import MivMultiPack, asyncio

async def main():
    module = MivMultiPack.miv_lavapi.lavapi()
    go = await module.get_track_info(identifier="ytsearch:dabstep", password="1029384756r", full_error=True)
    print(go)
    
asyncio.run(main())