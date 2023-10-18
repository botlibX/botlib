# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,R0903


"configuration"


from .default import Default


def __dir__():
    return (
            'Config',
            'Cfg'
           )


class Config(Default):

    pass


Cfg = Config()
