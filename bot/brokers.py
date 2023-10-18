# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,C0116,W0718,W0702,W0212,C0411,W0613,R0903,E1102
# pylint: disable=C0103,W0125,W0126


"object management"


from .objects import Object


class Broker(Object):

    "manages objects"

    #:
    objs = []

    @staticmethod
    def add(obj) -> None:
        "add object to broker"
        Broker.objs.append(obj)

    @staticmethod
    def announce(txt):
        "announce to all registered objects"
        for obj in Broker.objs:
            obj.announce(txt)

    @staticmethod
    def byorig(orig):
        "return by orig matching object"
        for obj in Broker.objs:
            if object.__repr__(obj) == orig:
                return obj
        return None

    @staticmethod
    def remove(obj) -> None:
        "remove object from broker"
        try:
            Broker.objs.remove(obj)
        except ValueError:
            pass

    @staticmethod
    def say(orig, channel, txt):
        "say on specific object"
        bot = Broker.byorig(orig)
        if not bot:
            return
        bot.dosay(channel, txt)
