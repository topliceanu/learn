# -*- coding: utf-8 -*-

class StateBasedIncrementOnlyCounter(object):
  """ Supports increments.

  See: https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type
  """

  def __init__(self, replica_id):
    self.state = {}
    self.replica_id

  def increment(self):
    if not replica_id in self.state:
      self.state[replica_id] = 0
    self.state[replica_id] += 1

  def value(self):
    return sum(counter for _, counter in self.state.iteritems())

  def __cmp__(self, other):
    """ self is smaller than other if corresponding counters are strictly smaller. """
    is_self_smaller = False
    is_other_smaller = False

    for k, v in self.state.iteritems():
      if k in other.state and self.state[k] > other.state[k]:
        is_other_smaller = True

    for k, v in other.state.iteritems():
      if k in self.state and self.state[k] < other.state[k]:
        is_self_smaller = True

    if is_self_smaller == True and is_other_smaller == False:
      return -1
    elif is_self_smaller == False and is_other_smaller == True:
      return 1
    else:
      return 0

  def merge(self, other):
    """ The counts of the other Counter are merged into the current counter. """
    for k, _ in self.state.iteritems():
      if k in other.state:
        self.state[k] = max(self.state[k], other.state[k])

    for k, _ in other.state.iteritems():
      if k not in self.state:
        self.state[k] = other.state[k]

class StateBasedPNCounter(self):
  """ Supports both increments and decrements. """

  def __init__(self, replica_id):
    self.replica_id
    self.p = StateBasedIncrementOnlyCounter(replica_id)
    self.n = StateBasedIncrementOnlyCounter(replica_id)

  def increment(self):
    self.p.increment()

  def decrement(self):
    self.n.increment()

  def value(self):
    return self.p.value() - self.n.value()

  def __cmp__(self, other):
    for k, _ in self.p.state.iteritems():
      pass

  def merge(self, other):
    self.p.merge(other.p)
    self.n.merge(other.n)

class StateBasedGrowOnlySet(self):

  def __init__(self):
    self.state = set()

  def add(self, e):
    self.state.add(e)

  def lookup(self, e):
    return e in self.state

  def compare(self, other):
    """ ie. subset. """
    return self.state <= other.state

  def merge(self, other):
    self.state = self.state.union(other.state)

class StateBased2PSet(self):

  def __init__(self):
    self.a = StateBasedGrowOnlySet()
    self.r = StateBasedGrowOnlySet()

  def add(e):
    self.a.add(e)

  def remove(e):
    self.r.add(e)

  def compare(self, other):
    return self.a.state <= other.a.state and self.r.state <= other.r.state

  def merge(self, other):
    self.a.merge(other.a)
    self.r.merge(other.r)

