class EventManager(object):

    __slots__ = ('name', 'listeners')
    def __init__(self):
        self.listeners = []

    def register_listener(self, listener):
        
        self.listeners.append(listener)
        
    def post(self, event):

        for listener in self.listeners:
            listener.notify(event)

class BaseEvent(object):

    __slots__ = ('name')
    def __init__(self):
        self.name = 'BaseEvent'
    def __str__(self):
        return self.name

class EventInitialize(BaseEvent):

    __slots__ = ('name')
    def __init__(self):
        self.name = 'Initialize event'
    def __str__(self):
        return self.name

class EventEveryTick(BaseEvent):

    __slots__ = ('name')
    def __init__(self):
        self.name = 'Tick event'
    def __str__(self):
        return self.name

class EventQuit(BaseEvent):

    __slots__ = ('name')
    def __init__(self):
        self.name = 'Quit event'
    def __str__(self):
        return self.name

class EventStateChange(BaseEvent):

    __slots__ = ('name', 'state')
    def __init__(self, state):
        self.name = 'State Change event'
        self.state = state
    def __str__(self):
        return self.name

class EventMove(BaseEvent):

    __slots__ = ('name', 'direction')
    def __init__(self, direction):
        self.name = 'Move event'
        self.direction = direction
    def __str__(self):
        return self.name

class EventMouseMotion(BaseEvent):

    __slots__ = ('name', 'position', 'state')
    def __init__(self, position, state):
        self.name = 'Mouse Motion event'
        self.position = position
        self.state = state
    def __str__(self):
        return self.name

class EventCameraMove(BaseEvent):

    __slots__ = ('name', 'direction')
    def __init__(self, direction):
        self.name = 'Camera Move event'
        self.direction = direction
    def __str__(self):
        return self.name

class EventPickGem(BaseEvent):

    __slots__ = ('name', 'gem')
    def __init__(self, gem):
        self.name = 'Pick Gem event'
        self.gem = gem
    def __str__(self):
        return self.name

class EventMoaiKingRadiation(BaseEvent):

    __slots__ = ('name', 'position')
    def __init__(self, position):
        self.name = 'Moai King Radiation event'
        self.position = position
    def __str__(self):
        return self.name

class EventMoaiKingRotation(BaseEvent):

    __slots__ = ('name', 'position', 'anti_clock')
    def __init__(self, position, anti_clock = True):
        self.name = 'Moai King Rotation event'
        self.position = position
        self.anti_clock = anti_clock
    def __str__(self):
        return self.name
