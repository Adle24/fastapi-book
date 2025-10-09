import asyncio


async def q():
    print("why can't programmers tell joke?")
    await asyncio.sleep(3)


async def a():
    print("timing")


async def main():
    await asyncio.gather(q(), a())


asyncio.run(main())
