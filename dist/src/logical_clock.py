# -*- coding: utf-8 -*-

import copy


class LamportClock(object):
    """ Implements Lamport clock.

    When a message is sent via the network, the clock should be incremented,
    and it should be sent along with the message. When a message is receive,
    the internal counter should be updated with the maximum of the internal
    clock and the received clock.

    See: http://en.wikipedia.org/wiki/Lamport_timestamps

    Attrs:
        counter: int, the internal Lamport counter.
    """

    def __init__(self):
        self.counter = 0

    def increment(self):
        """ Bumps the current clock value. """
        self.counter += 1

    def read(self):
        """ Returns the value of the current clock. """
        return self.counter

    def merge(self, other):
        """ Update the current clock based on the value of the given clock. """
        self.counter = max(self.counter, other.read()) + 1

    def fork(self):
        """ Clone the current clock into a new one. """
        new_clock = LamportClock()
        new_clock.merge(self)


class VectorClock(object):
    """ Vector clock implementation.

    Rules:
    - when a process starts, it initializes it's own vector clock with zeros.
    - when a new revision is received to be merged:
        - increment the logical clock for the current process.
        - update each element in revision to be max(local, received)

    See: http://en.wikipedia.org/wiki/Vector_clock

    Attrs:
        process_name: str, the name of the current process, should be unique!
        revision: dict, holds snapshot of the logical clock maintained
            by the current process.
    """

    def __init__(self, process_name):
        self.process_name = process_name
        self.revision = {process_name: 0}

    def read(self):
        """ Returns a dict representation of the current vector clock. """
        return copy.copy(self.revision)

    def increment(self):
        """ Increment the logical clock for the current vector. """
        self.revision[self.process_name] += 1

    def update(self, new_revision):
        """ Increases the clock timestamp for the current process and updates
        the counters for the other processes, according to the rules.

        Args:
            new_revision: dict, holds a snapshot of a logical clock received
                from another process.
        """
        self.increment()

        keys = self.revision.keys()
        keys.extend(new_revision.keys())
        for key in keys:
            if key in self.revision and key in new_revision:
                self.revision[key] = max(self.revision[key], new_revision[key])
            elif key not in self.revision and key in new_revision:
                self.revision[key] = new_revision[key]

    def __cmp__(self, other):
        """ Used to compare two vector clocks.

        Args:
            other: object, instance of src.logical_clock.VectorClock

        Returns:
            -1, if self < other, ie. at least one of the common processes has a
                clock strictly smaller in self, the rest are all smaller or equal.
            0, if self == other, ie. values of all common processes are equal.
            1, if self > other, ie. at least one of the common processes has a
                clock strictly larger in self, the rest are all larger or equal.

        Raises:
            Exception, when the two vector clocks are not comparable, ie. no common processes.
        """
        local = self.read()
        remote = other.read()
        common_keys = set(local.keys()).intersection(set(remote.keys()))

        if len(common_keys) == 0:
            raise Exception('VectorClock instances are not comparable')

        (local_larger, remote_larger) = (0, 0)
        for key in common_keys:
            if local[key] > remote[key]:
                local_larger += 1
            elif local[key] < remote[key]:
                remote_larger += 1

        if local_larger > 0 and other_larger == 0:
            return 1
        if local_larger == 0 and other_larger > 0:
            return -1
        if local_larger == 0 and other_larger == 0:
            return 0

        raise Exception('Incorrect vector clocks')
