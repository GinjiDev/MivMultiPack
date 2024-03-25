import MivMultiPack, asyncio, time

module = MivMultiPack.AsyncRandom()



async def main():
    while True:
        random_from_array = await module.get_random_from_array(-10, 10)
        print("Random number from array:", random_from_array)
        time.sleep(1)
    
asyncio.run(main())