# -*- coding: utf8 -*-

from operator import itemgetter


KEY = 0
WEIGHT = 1
LENGTH = 2
SCORE = 3
COMPLETION_TIME = 4

def schedule(jobs, score='ratio'):
    """ Schedules a given batch of jobs.

    Two variants of computing scores are possible: weight/length or
    weight-length. On the second variant, if two jobs have the same score, the
    one with higher weight gets in front.

    Args:
        jobs: list of tuples, format [[key, weight, length]]
        score: str, either 'ratio' or 'diff'

    Returns:
        dict, format {sorted_jobs, sum_completion_time}
            sorted_job: list, of jobs sorted by score, format [[key, weight, length, score, completion_time]]
            sum_completion_time: int, weighted sum of all completion times.
    """
    if score is 'ratio':
        for job in jobs:
            job.append(float(job[WEIGHT])/job[LENGTH])
        sorted_jobs = sorted(jobs, key=itemgetter(SCORE), reverse=True)
    elif score is 'diff':
        for job in jobs:
            job.append(float(job[WEIGHT]) - job[LENGTH])
        def cmp_jobs(j1, j2):
            if j1[SCORE] == j2[SCORE]:
                return cmp(j1[WEIGHT], j2[WEIGHT])
            return cmp(j1[SCORE], j2[SCORE])
        sorted_jobs = sorted(jobs, cmp=cmp_jobs, reverse=True)
    else:
        raise Exception('Score strategy unknown {score}'.format(score=score))

    sum_completion_time = 0
    completion_time_so_far = 0
    for job in sorted_jobs:
        completion_time_so_far += job[LENGTH]
        job.append(completion_time_so_far)
        sum_completion_time += job[WEIGHT] * job[COMPLETION_TIME]

    return {
        'sum_completion_time': sum_completion_time,
        'sorted_jobs': sorted_jobs
    }
