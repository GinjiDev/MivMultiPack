import MivMultiPack, asyncio

module = MivMultiPack

async def main():
    #генерация случайного числа
    #seed -> инициализации начального состояния генератора, если не назначено то число генерируется случайно
    #digits -> управляет количеством цифр в случайном числе
    generate = module.AsyncRandom(seed=8, digits=3)
    var = await generate.generate_random_number_async()
    print(var)

    #генерация случайного диапозонного числа
    #start -> Начальное число
    #stop -> Конечное число
    #exclude_bounds -> определяет, исключать ли граничные значения из диапазона, например при True -39 и 39, при False -40 и 40
    generate_range = module.AsyncRandomRange(start=-40, stop=40, exclude_bounds=False)
    var = await generate_range.generate_random_number_async()
    print(var)

asyncio.run(main())