# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,C0116,W0718,W0702,W0212,C0411,W0613,R0903,E1102
# pylint: disable=C0103,W0125,W0126


"handler"


import inspect
import queue
import threading
import _thread


from .brokers import Broker, BroadCast
from .errored import Errors
from .objects import Default, Object
from .storage import Storage
from .threads import launch
from .utility import spl


class Event(Default):

    __slots__ = ('_ready', "_thr")

    def __init__(self, *args, **kwargs):
        Default.__init__(self, *args, **kwargs)
        self._ready = threading.Event()
        self.channel = ""
        self.orig = ""
        self.result = []
        self.txt = ""
        self.type = "command"

    def ready(self):
        self._ready.set()

    def reply(self, txt) -> None:
        self.result.append(txt)

    def show(self) -> None:
        for txt in self.result:
            BroadCast.say(self.orig, self.channel, txt)

    def wait(self):
        self._ready.wait()
        if self._thr:
            self._thr.join()


class Handler(Object):

    cmds = {}

    def __init__(self):
        Object.__init__(self)
        self.cbs = Object()
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.end = threading.Event()

    @staticmethod
    def add(func):
        Handler.cmds[func.__name__] = func

    def event(self, txt):
        evt = Event()
        evt.txt = txt
        evt.orig = object.__repr__(self)
        return evt

    def forever(self):
        self.stopped.wait()

    def dispatch(self, evt):
        func = getattr(self.cbs, evt.type, None)
        if not func:
            evt.ready()
            return
        try:
            evt._thr = launch(func, evt)
        except Exception as ex:
            exc = ex.with_traceback(ex.__traceback__)
            Errors.errors.append(exc)
            evt.ready()

    def loop(self) -> None:
        while not self.stopped.is_set():
            try:
                self.dispatch(self.poll())
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()

    def poll(self) -> Event:
        return self.queue.get()

    def put(self, evt):
        self.queue.put_nowait(evt)

    @staticmethod
    def scan(mod) -> None:
        for key, cmd in inspect.getmembers(mod, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmd.__code__.co_varnames:
                Handler.add(cmd)

    def register(self, typ, cbs):
        self.cbs[typ] = cbs

    def start(self):
        launch(self.loop)

    def stop(self):
        self.stopped.set()


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.register("command", command)
        Broker.add(self)

    def announce(self, txt):
        self.raw(txt)

    def dosay(self, channel, txt):
        self.raw(txt)

    def raw(self, txt):
        pass


def command(evt):
    func = Handler.cmds.get(evt.cmd, None)
    if not func:
        evt.ready()
        return
    try:
        func(evt)
        evt.show()
    except Exception as ex:
        exc = ex.with_traceback(ex.__traceback__)
        Errors.errors.append(exc)
    evt.ready()


def scan(pkg, modnames="", initer=False, dowait=False) -> []:
    if not pkg:
        return []
    inited = []
    scanned = []
    threads = []
    for modname in spl(modnames):
        module = getattr(pkg, modname, None)
        if not module:
            continue
        scanned.append(modname)
        Handler.scan(module)
        Storage.scan(module)
        if initer:
            try:
                module.init
            except AttributeError:
                continue
            inited.append(modname)
            threads.append(launch(module.init, name=f"init {modname}"))
    if dowait:
        for thread in threads:
            thread.join()
    return inited


def scandir(path, modnames="", initer=False, dowait=False) -> []:
    if not os.path.exists(path):
        return []
    inited  = []
    scanned = []
    threads = []
    fnames  = os.listdir(path)
    for modname in spl(modnames):
        if modname not in fnames:
            continue
        module = importlib.import_module(f"modules.{modname}")
        if not module:
            continue
        scanned.append(modname)
        Handler.scan(module)
        Storage.scan(module)
        if initer:
            try:
                module.init
            except AttributeError:
                continue
            inited.append(modname)
            threads.append(launch(module.init, name=f"init {modname}"))
    if dowait:
        for thread in threads:
            thread.join()
    return inited
