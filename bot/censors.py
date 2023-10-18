# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116,C0103,E0402,E1102,R0903


"at the gate"


import sys


from .configs import Cfg
from .objects import Object


def __dir__():
    return (
            'Censor',
            'cprint',
            'debug',
            'output'
           ) 


output = None


class Censor(Object):

    words = []

    @staticmethod
    def skip(txt) -> bool:
        for skp in Censor.words:
            if skp in str(txt):
                return True
        return False


def cprint(txt):
    if output is None:
        return
    if Censor.skip(txt):
        return
    output(txt)
    sys.stdout.flush()


def debug(txt):
    if "v" in Cfg.opts:
        cprint(txt)
