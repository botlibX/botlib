# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116,E0402


"errors"


import io
import traceback


from .censors import output
from .objects import Object


def shutdown():
    Errors.show()


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
    