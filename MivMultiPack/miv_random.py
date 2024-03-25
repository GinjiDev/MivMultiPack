import asyncio


class AsyncRandom:
    def __init__(self) -> None:
        self.multiplier = 1664525
        self.increment = 1013904223
        self.modulus = 2**32

    async def get_algorithm(
        self,
        seed: any = None
    ) -> int:
        # If seed is not provided, create it based on the
        # current event loop time
        if not seed:
            current_time = asyncio.get_event_loop().time()
            seed = int(current_time * 1000)

        # Linear congruential method for generating pseudo-random numbers
        return ((self.multiplier * seed + self.increment) % self.modulus)

    async def get_random_number(
        self,
        seed: any = None,
        digits: int = 8
    ) -> int:
        return await self.get_algorithm(seed) % (10 ** digits)

    async def get_random_from_array(
        self,
        start_value: int,
        stop_value: int,
        exclude_bounds: bool = False
    ) -> int:
        # Ensure start_value is less than or equal to stop_value
        if start_value > stop_value:
            start_value, stop_value = stop_value, start_value

        # Adjust for excluding bounds
        if exclude_bounds:
            if start_value < 0:
                start_value += 1
            if stop_value > 0:
                stop_value -= 1

        # Calculate the range and generate a random number within it
        range_size = stop_value - start_value + 1
        return (await self.get_algorithm() % range_size) + start_value

    async def get_random_element(
        self,
        array: any
    ) -> int:
        current_time = str(asyncio.get_event_loop().time())
        hash = int(current_time[-3:])
        index = int(hash / 1000 * len(array))
        return array[index]
