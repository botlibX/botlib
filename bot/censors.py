# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,C0116,W0718,W0702,W0212,C0411,W0613,R0903,E1102
# pylint: disable=C0103,W0125,W0126


"at the gate"


from .configs import Cfg
from .objects import Object


output = None


class Censor(Object):

    words = []

    @staticmethod
    def skip(txt) -> bool:
        for skp in Censor.words:
            if skp in str(txt):
                return True
        return False


def debug(txt):
    if output is None:
        return
    if Censor.skip(txt):
        return
    if "v" in Cfg.opts:
        output(txt)
