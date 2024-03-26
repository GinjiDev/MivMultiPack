import MivMultiPack, asyncio

async def main():
    print(await MivMultiPack.utils.ms_to_hours_minutes_seconds(ms=3661000))
    
asyncio.run(main())