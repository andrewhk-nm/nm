""" Collection of modules that are useful for my
work at Northwestern Mutual.

Andrew Henning-Kolberg
2016-02-14
"""

import datetime

def per_week(goal, have):
    """ Given a Goal of 'goal' units and a current 'have' amount,
    return the average weekly production needed to meet that goal by the
    end of the year.
    """
    return (goal - have) / (52 - datetime.datetime.isocalendar(datetime.datetime.now())[1])
