# -*- coding: utf-8 -*-


class Coordinator(object):
    """ Implements the coordinator role of the two-phase commit protocol.
    See: http://en.wikipedia.org/wiki/Two-phase_commit_protocol
    """

    def send_query_to_commit(self):
        pass

    def send_commit(self):
        pass

    def send_rollback(self):
        pass
