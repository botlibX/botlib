# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,C0116,W0718,W0702,W0212,C0411,W0613,R0903,E1102
# pylint: disable=C0103,W0125,W0126


"clientele"


from .brokers import Broker
from .handler import Handler, command


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
