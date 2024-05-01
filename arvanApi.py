datacenter_keys = {
    'hamrah_aval': 'mci',
    'mobin_net': 'mobinnet',
    'afranet': 'afranet',
    'pars_online': 'parsonline',
    'host_iran': 'hostiran',
    'tehran_1': 'tehran-1',
    'tehran_2': 'tehran-2',
    'tehran_3': 'tehran-3',
}

from abc import ABC, abstractmethod
import asyncio
import aiohttp


class AbstractRadar(ABC):
    pass


class ArvanRequest:
    @staticmethod
    async def make_request(url):
        try:

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise ConnectionError(f'status code: {response.status}')
                    if hasattr(response, 'json'):
                        return await response.json()
                    return None

        except aiohttp.ClientConnectorError:
            return None


async def main():
    a = await ArvanRequest.make_request('https://radar.arvasncloud.ir/api/v1/internet-monitoring?isp=mci')
    print(a)

asyncio.run(main())




class ArvanRadar(AbstractRadar):
    def __init__(self):
        pass

    def get_data(self, *args):
        for datacenter in args:
            pass
