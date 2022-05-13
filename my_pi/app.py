import socketio
import time



# create a Socket.IO server
sio = socketio.Server()
# wrap with a WSGI application
app = socketio.WSGIApp(sio, static_files={
    '/': './client/'
})



@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def data(sid, data):
    sio.emit('data', data)
    print('data ', data)

@sio.event
def talk(sid):
    print('talk ', sid)
    while True:
        time.sleep(4)
        print('volume down')
        sio.emit('command', {'command': 'voldown',})