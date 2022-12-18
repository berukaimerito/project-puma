import asyncio
from threading import Thread
from Services.supervisor import Supervisor


async def supervisor(bot):
    thread_consume = threading.Thread(target=lambda: asyncio.run(Supervisor.consume_intervals(bot)))
    thread_consume.setName("thread_queue")
    thread_consume.start()

