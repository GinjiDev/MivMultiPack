import aiohttp

class lavapi:
    def __init__(
            self
        ) -> None:
        pass
    
    async def get_track_info(
            self,
            identifier: str,
            password: str,
            lavalink_adress='localhost',
            lavalink_port=2333,
            info=True,
            full_error=False
        ) -> None:
        url = f"http://{lavalink_adress}:{lavalink_port}/v4/loadtracks"
        params = {'identifier': identifier}
        headers = {
            'Authorization': password,
            'Accept': 'application/json'
        }

        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(url, headers=headers, params=params) as response:
                    if response.status == 200:
                        if info == True:
                            print(f'["INFO HOST"] lavalink_host -> {lavalink_adress} | lavalink_port -> {lavalink_port}')
                        data = await response.json()
                        return data.get('data', [])
                    else:
                        print(f"Ошибка при получении данных: {response.status}, {response.text}")
                        return []
        except aiohttp.ClientConnectorError as error:
            error_message = f"Ошибка подключения: {error}"
            if full_error:
                raise ValueError(error_message)
            else:
                print(error_message)
                return []
        except Exception as error:
            error_message = f"Ошибка: {error}"
            if full_error:
                raise ValueError(error_message)
            else:
                print(error_message)
                return []
    
#--------------------------------------------------------------------------------------