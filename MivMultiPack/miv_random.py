import asyncio


class AsyncRandom:
    def __init__(
        self,
    ) -> None:

        self.multiplier = 1664525
        self.increment = 1013904223
        self.modulus = 2**32

    def get_algorithm(
        self,
        seed: any = None
    ) -> int:
        # Если сид не указан создадим его
        if not seed:
            # Инициализация seed на основе текущего времени
            current_time = asyncio.get_event_loop().time()
            seed = int(current_time * 1000)

        # Линейный конгруэнтный метод для генерации псевдослучайных чисел
        return ((self.multiplier * seed + self.increment) % self.modulus)

    async def get_random_number(
        self,
        seed: any = None,
        digits: int = 8
    ) -> int:
        return self.get_algorithm(seed) % (10 ** digits)

    async def get_random_from_array(
        self,
        start_value: int,
        stop_value: int,
        exclude_bounds: bool = False
    ) -> int:
        if start_value < stop_value:
            # Если значение стартовое значение меньше конечного
            # Меняем их местами
            start_value, stop_value = stop_value, start_value

        if exclude_bounds:
            # Если exclude_bounds установлен в True и start_value равно stop_value,
            # возвращаем start_value
            if start_value == stop_value:
                return start_value
            
            start_value += 1
            stop_value -= 1

        return self.get_algorithm() % (stop_value - start_value) + start_value

    async def get_random_element(
        self,
        array: any
    ) -> int:
        current_time = str(asyncio.get_event_loop().time())
        hash = int(current_time[-3:])
        index = int(hash / 1000 * len(array))
        return array[index]
