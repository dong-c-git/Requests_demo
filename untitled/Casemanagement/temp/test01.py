import asyncio


async def buy_potatos():
    bucket = []
    for p in range(1000):
        bucket.append(p)
        print(f'Got potato {id(p)}...')
    test = "this is async compleate"
    return test

class ThreeTwoOne:

    def __init__(self):
        test = asyncio.get_event_loop().run_until_complete(buy_potatos())
        print(test)



if __name__ == "__main__":
    ThreeTwoOne()