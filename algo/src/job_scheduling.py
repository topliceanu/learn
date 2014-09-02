# -*- coding: utf8 -*-

from operator import itemgetter


def schedule(jobs):
    """ Schedules a given batch of jobs.

    This algorithm computes a score for each job: weight/length. Then it
    sorts the jobs given each score.

    Args:
        jobs: list of tuples, format [(key, weight, length)]

    Returns:
        A list of jobs keys which minimizes sum(weight*completion_time)
    """
    scores = []
    for job in jobs:
        scores.append((job[0], job[1]/job[2]))

    scores = sorted(scores, key=itemgetter(1))
    return map(itemgetter(0), scores)
