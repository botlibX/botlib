# This file is placed in the Public Domain.
#
# pylint: disable=C0112,C0115,C0116,W0105,R0902,R0903,E0402,C0411,W0622,W0102


"default attributes"


from .objects import Object


class Default(Object):

    __slots__ = ("__default__",)

    def __init__(self):
        Object.__init__(self)
        self.__default__ = ""

    def __getattr__(self, key):
        return self.__dict__.get(key, self.__default__)
