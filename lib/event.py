from .delegate import Delegate

class Event(property):
    '''Class event notifier
    Usage:
        class C:
            TheEvent = Event()
            def OnTheEvent(self):
                self.TheEvent(self, context)

        instance = C()
        instance.TheEvent += callback
        instance.OnTheEvent()
        instance.TheEvent -= callback
    '''
    def __init__(self):
        self.attrName = attrName = "__Event_" + str(id(self))
        def getEvent(subject):
            if not hasattr(subject, attrName): 
                setattr(subject, attrName, Delegate())
            return getattr(subject, attrName)
        super(Event, self).__init__(getEvent)

    def call(self, subject, *args, **kw):
        if hasattr(subject, self.attrName):
            getattr(subject, self.attrName)(subject, *args, **kw)