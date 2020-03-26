# Implements several algorithms for triggering timeout.
# TODO add tests to these implementations.

class Timer(object):
    """ Abstract class for the implementation of timers. """

    def __init__(self):
        pass

    def start_timer(self, timeout, callback):
        """ Returns a timer_id int """
        pass

    def stop_timer(self, timer_id):
        """ Removes the timer including the callback from the internal storage. """
        pass

    def per_tick_bookkeeping(self):
        """ Executes every tick interval """

    def process_expiry(self, timer_id):
        """ Executed by sweep when a timeout expires and a callback needs to
        be executed.
        """

class UnorderedListTimer(Timer):
    """ Stores timers in a simple linked list emulated by an array in python.
    Complexity: O(1) - start_timer; O(n) - per_tick_bookkeeping.
    """

    def __init__(self):
        Timer.__init__(self)
        self.timer_list = []

    def start_timer(self, timeout, callback):
        self.timer_list.append({'timeout': timeout, 'callback': callback})
        return len(self.timer_list) - 1

    def stop_timer(self, timer_id):
        del self.timer_list[timer_id]

    def per_tick_bookkeeping(self):
        for (timer_id, timer) in enumerate(self.timer_list):
            timer['timeout'] -= 1
            if timer['timeout'] == 0:
                self.process_expiry(timer_id)

    def process_expiry(self, timer_id):
        timer = self.timer_list[timer_id]
        self.stop_timer(timer_id)
        timer['callback']()

class OrderedListTimer(Timer):
    """ Stores timers in a sorted array.
    Complexity: O(n) - start_timer; O(1) - per_tick_bookkeeping.
    """
    def __init__(self):
        self.timer_list = []
        self.inserted_timers = {}
        self.last_timer_id = 0

    def start_timer(self, timeout, callback):
        absolute_timeout = int(time.time()) + timeout
        timer = {'timeout': absolute_timeout, 'callback': callback}
        self.inserted_timers[self.last_timer_id] = timer

        return self.last_timer_id
