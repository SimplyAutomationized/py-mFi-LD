import asyncio

class Py3Resource:

    def __init__(self, poll_func, sleep_timer):
        self.poll_func = poll_func
        self.sleep_timer = sleep_timer

        asyncio.get_event_loop().create_task(self.poll())

    @asyncio.coroutine
    def poll(self):
        while True:
            self.poll_func()
            yield from asyncio.sleep(self.sleep_timer)



class Py3PollWhileTrue:

    def __init__(self, poll_func, sleep_timer):
        self.poll_func = poll_func
        self.sleep_timer = sleep_timer

        asyncio.get_event_loop().create_task(self.poll())

    @asyncio.coroutine
    def poll(self):
        if callable(self.poll_func):
            while self.poll_func():
                yield from asyncio.sleep(self.sleep_timer)
        else:
            while self.poll_func:
                yield from asyncio.sleep(self.sleep_timer)