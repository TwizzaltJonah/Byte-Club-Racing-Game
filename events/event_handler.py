from __future__ import annotations
import pygame

pygameEventListeners: dict[int, list[PygameEventListener]] = dict()

class PygameEventListener:
    """a wrapper class for a function that should be called when its corresponding pygameEvent occurs

    note: if an instance is instantiated directly, it will not successfully listen for events
          to make it successfully listen for events use the createPygameEventListener function instead"""
    def __init__(self, eventToListenFor: int, onEvent: callable, *args):
        self.eventToListenFor = eventToListenFor
        self.onEvent = onEvent
        self.onEventArgs = args

    def executeFunction(self):
        self.onEvent(*self.onEventArgs)

    def add(self):
        """add this PygameEventListener to the pygmeEventListeners dict

        this will allow self's onEvent function to be called when the event is broadcasted
        """
        if self.eventToListenFor not in pygameEventListeners.keys():
            pygameEventListeners[self.eventToListenFor] = [self]
        else:
            pygameEventListeners[self.eventToListenFor].append(self)

    def remove(self):
        """remove this PygameEventListener from the pygameEventListeners dict

        this should be done whenever it is done being used, otherwise it will just sit in the dict until the program terminates
        """
        if self in pygameEventListeners[self.eventToListenFor]:
            pygameEventListeners[self.eventToListenFor].remove(self)

def broadcastPygameEvents(events: list[pygame.event.EventType]):
    """broadcast all events to their listeners

    uses the 'pygameEventListeners' dict to execute the functions of all PygameEventListeners for all pygame events
    """
    for event in events:
        if event.type in pygameEventListeners.keys():
            for listener in pygameEventListeners[event.type]:
                listener.executeFunction()
