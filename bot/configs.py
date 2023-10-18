# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,R0903


"configuration"


from .default import Default


class Config(Default):

    pass


Cfg = Config()
