import socketio
import asyncio
import time
# standard Python
sio = socketio.Client()

# asyncio
sio = socketio.AsyncClient()
a = 0

async def func():
    await sio.connect('http://localhost:8000')
    print('my sid is', sio.sid)
    return

@sio.event
def my_event(sid, data):
    # handle the message
    return "OK", 123

async def func3 ():
    print('func3')
    await sio.emit('myevent', {'foo': 'bar'})
    return



async def func2 ():
    a = 0
    while True:
        a = a + 1
        if((a % 15) == 0):
            await func3()
        time.sleep(.1)
    return
    
            
asyncio.run(func())
asyncio.run(func2())
# func2()