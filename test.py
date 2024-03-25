import MivMultiPack, asyncio, time

module = MivMultiPack.AsyncRandom()



async def main():
    random_from_array = await module.get_random_from_array(-10, 10)
    print("Random number from array:", random_from_array)
    
    random_from_array = await module.get_algorithm()
    print("Random number from array:", random_from_array)
    
asyncio.run(main())