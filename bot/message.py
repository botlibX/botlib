# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,C0116,W0718,W0702,W0212,C0411,W0613,R0903,E1102
# pylint: disable=C0103,W0125,W0126


"messages"


import threading


from .brokers import Broker
from .default import Default


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
            Broker.say(self.orig, self.channel, txt)

    def wait(self):
        self._ready.wait()
        if self._thr:
            self._thr.join()
