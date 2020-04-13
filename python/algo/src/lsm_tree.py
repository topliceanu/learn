# -*- coding: utf-8 -*-


class LSMTree(object):
    """ Implements a Log Structured Merge Tree data structure.
    They optimise for write throughput

    Resources:
        http://www.quora.com/How-does-the-Log-Structured-Merge-Tree-work
        http://www.benstopford.com/2015/02/14/log-structured-merge-trees/
    """
