import asyncio


async def put_q(q: asyncio.Queue):
    for x in range(100):
        await q.put(x)
        print("put ", x)
    await q.put(None)
    await q.put(None)


async def calc_squares(task_name: str, q: asyncio.Queue, result_q: asyncio.Queue):
    while True:
        x = await q.get()
        if x is None:
            break
        print(task_name, x)
        await result_q.put(f"{task_name}: {x * x } ")
        await asyncio.sleep(0)


q = asyncio.Queue(5)
res_q = asyncio.Queue()
loop = asyncio.get_event_loop()
# tasks = [
#     put_q(q),
#     loop.create_task(calc_squares('t1', q, res_q)),
#     loop.create_task(calc_squares('t2', q, res_q)),
# ]

# wait_tasks = asyncio.wait(tasks)

# loop.run_until_complete(wait_tasks)
loop.run_until_complete(asyncio.gather(
    put_q(q),
    calc_squares('t1', q, res_q),
    calc_squares('t2', q, res_q)
))

loop.close()

while not res_q.empty():
    print(res_q.get_nowait())
