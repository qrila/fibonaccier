import asyncio
from random import random
import argparse

finished_tasks = []


async def fib(n):
    return n if n in [0, 1] else await fib(n - 1) + await fib(n - 2)


async def work_task(id, number):
    rand = random()
    await asyncio.sleep(rand)

    result = await asyncio.create_task(fib(number), name=id)
    finished_tasks.append(id)

    return [id, result]


async def main():
    finished_tasks.clear

    parser = argparse.ArgumentParser(
        prog="fibonaccier",
        description="Use Fibonaccier script to find out fibonacci value for a number and which of two created async functions complete first.",
        epilog='Use syntax: "python fibonaccier.py <positive integer>".',
    )
    parser.add_argument(
        "number", metavar="N", type=int, help="Positive integer"
    )
    args = parser.parse_args()
    number = args.number
    if number < 0:
        parser.print_help()
        exit(1)

    result = await asyncio.gather(
        work_task("first", number), work_task("second", number)
    )

    quickest = list(filter(lambda t: t[0] == finished_tasks[0], result))[0]
    print(
        f"Fibonacci number for {number} is {quickest[1]}. The {quickest[0]} function completed first."
    )


asyncio.run(main())
