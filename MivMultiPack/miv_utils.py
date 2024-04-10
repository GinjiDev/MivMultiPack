import aiohttp

class AsyncUtils:
    
    def __init__(
            self
        ) -> None:
        self.translit_dict = {
            'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г',
            'h': 'х', 'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
            'o': 'о', 'p': 'п', 'q': 'к', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у',
            'v': 'в', 'w': 'в', 'x': 'кс', 'y': 'й', 'z': 'з',
            
            'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г',
            'H': 'Х', 'I': 'И', 'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н',
            'O': 'О', 'P': 'П', 'Q': 'К', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У',
            'V': 'В', 'W': 'В', 'X': 'КС', 'Y': 'Й', 'Z': 'З',
        }

    async def translit_to_cyrillic(
            self,
            translit: str
        ) -> None:
        cyrillic_string = ''.join(
            self.translit_dict.get(
                
                    char, char
                )
                for char in translit
            )
        return cyrillic_string

    async def is_image_url(
            self, 
            url: str
        ) -> None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.head(url) as response:
                    content_type = response.headers.get('Content-Type', '').lower()
                    return content_type.startswith(
                            'image/'
                        )
        except aiohttp.ClientError:
            return False

    async def duration(
            ms: int
        ) -> None:
        seconds = ms // 1000
        minutes, seconds = divmod(
                seconds,
                60
            )
        hours, minutes = divmod(
                minutes,
                60
            )
        return hours, minutes, seconds


#псевдоним для класса
ASYNCUTILS = asyncutils = AsyncUtils