# -*- coding: utf-8 -*-


class Cohort(object):
    """ Implements the cohort role in the two-phase commit protocol.

    See: http://en.wikipedia.org/wiki/Two-phase_commit_protocol
    """

    def send_agreement(self):
        pass

    def send_acknoledge(self):
        pass
