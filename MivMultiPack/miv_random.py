import asyncio, time

class async_random:
    
    def __init__(self, seed=None, digits=8):
        if seed is None:
            self.seed = int(time.time() * 1000)  # Инициализация seed на основе текущего времени
        else:
            self.seed = seed
        self.digits = digits
        self.multiplier = 1664525
        self.increment = 1013904223
        self.modulus = 2**32

    async def _generate_random_number(self):
        
        #линейный конгруэнтный метод для генерации псевдослучайных чисел
        
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulus
        random_number = self.seed % (10 ** self.digits)
        return random_number
        
    async def generate_random_number_async(self):
        return await self._generate_random_number()

    def generate_random_number(self):
        return asyncio.run(self.generate_random_number_async())