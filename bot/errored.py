# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,C0116,W0718,W0702,W0212,C0411,W0613,R0903,E1102
# pylint: disable=C0103,W0125,W0126


"errors"


import io
import traceback


from .censors import output
from .objects import Object


class Errors(Object):

    errors = []

    @staticmethod
    def format(exc):
        res = ""
        stream = io.StringIO(
                             traceback.print_exception(
                                                       type(exc),
                                                       exc,
                                                       exc.__traceback__
                                                      )
                            )
        for line in stream.readlines():
            res += line + "\n"
        return res

    @staticmethod
    def handle(exc):
        if output:
            output(Errors.format(exc))

    @staticmethod
    def show():
        for exc in Errors.errors:
            Errors.handle(exc)
