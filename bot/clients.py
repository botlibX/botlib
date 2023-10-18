# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116,E0402,W0613


"clients"


from .brokers import Broker
from .handler import Handler, command


def __dir__():
    return (
            'Client',
           )


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
